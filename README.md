# PIAIC Student Card Generator

A Python-based application that generates digital ID cards for PIAIC (Presidential Initiative for Artificial Intelligence and Computing) students using CrewAI, Chainlit, and Google Gemini API. This project allows users to input their details via a chat interface and generates a customizable ID card based on the message content.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Generate PIAIC student ID cards directly from chat messages.
- Supports natural language input (e.g., "generate card for Taha with rollno 66").
- Includes customizable fields with default values.
- Integrates CrewAI for task automation and Google Gemini API for fallback responses.
- Real-time chat-based UI using Chainlit.

## Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Required libraries: chainlit, crewai, google-generative-ai, langchain-google-genai, pydantic

## Installation
1. Clone the Repository
   git clone https://github.com/TahaNadeemkhan/card_generator.git
   cd card_generator

2. Create a Virtual Environment (Optional)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
   pip install chainlit crewai google-generative-ai langchain-google-genai pydantic pillow

4. Set Up Environment Variables
   - Create a .env file in the project root.
   - Add: GEMINI_API_KEY=your_api_key_here
   - Do not commit .env to version control.

5. Verify Installation
   - Check for errors in dependency installation.
   - Ensure crews/ directory exists.

## Usage
1. Run the Application
   chainlit run main.py

2. Access the UI
   - Open http://localhost:8000 in your browser.
   - Use the chat interface to input commands.

3. Generate a Card
   - Type: generate card for <name> with rollno <number>
     - Example: generate card for Taha with rollno 66
   - The app processes the message and generates a card.

4. Example Output
   - Includes: Name, Roll No, City, Center, Campus, Days/Time, Batch, Fees Status
   - Downloadable PNG file of the card.

## Project Structure
card_generator/
├── crews/
│   └── piaic_card/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── piaic_card.py
├── main.py
├── .env
├── README.md

## Configuration
- Set GEMINI_API_KEY in .env file.
- Default values are in main.py or crew files.
- Fees status uses dummy data; update as needed.

## Contributing
1. Fork the repository.
2. Create a branch: git checkout -b feature-branch
3. Commit changes: git commit -m "Add feature"
4. Push: git push origin feature-branch
5. Open a Pull Request.
- Report issues for bugs or suggestions.

## License
MIT License (see LICENSE file if applicable).

## Contact
- Author: [Your Name]
- Email: [tahak6884@gmail.com]
- GitHub: [https://github.com/TahaNadeemkhan](https://github.com/TahaNadeemkhan)
