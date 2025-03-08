from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import PiaicStudentCard, FeesUpdate

@CrewBase

class CardGenerator:
    '''Card Generator'''
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def piaic_card_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["piaic_card_generator"],
            tools=[PiaicStudentCard(), FeesUpdate()]
        )

    @task
    def card_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['card_generation_task']
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,  
            process=Process.sequential,
        )