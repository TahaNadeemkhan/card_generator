#main.py
import chainlit as cl
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai.flow import Flow, start
import asyncio
import os
from dotenv import load_dotenv
from crews.piaic_card.piaic_card import CardGenerator
load_dotenv()

#setting api
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

# initiliazing model
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")  

# Model settings
settings = {
    "temperature": 0.7,
    "max_output_tokens": 500,
    "top_p": 1,
}

class GenerateCard(Flow):
    @start()
    def generate_piaic_card(self, card_generate_prompt):
        """Calls CrewAI to create piaic student card."""
        return CardGenerator().crew().kickoff(inputs={"query": card_generate_prompt})
@cl.on_chat_start
def on_chat_start():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are helpful assistant"}]
    )
    cl.user_session.set("flow", GenerateCard())

@cl.on_message
async def on_message(message: cl.Message):
    """Handles incoming messages and generates responses."""
    message_history = cl.user_session.get("message_history")
    flow = cl.user_session.get("flow")

    message_history.append({"role": "user", "content": message.content})

    thinking_msg = cl.Message(content="Processing your request...")
    await thinking_msg.send()

    crew_output = await asyncio.to_thread(flow.generate_piaic_card, message.content)

    if crew_output:
        response_text = getattr(crew_output, "text", str(crew_output)) 
    else:
        gemini_response = await asyncio.to_thread(model.generate_content, message_history, **settings)
        response_text = gemini_response.text.strip()

    formatted_result = response_text.replace("\\n", "\n")

    # Save response to conversation history
    message_history.append({"role": "assistant", "content": formatted_result})

    # Remove processing message and send final response
    await thinking_msg.remove()
    await cl.Message(content=formatted_result).send()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "plot":
        plot()
    else:
        print("To use the UI, run with: chainlit run main.py")






