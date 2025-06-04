
"""Insurance Claim Processing example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Insurance Claim Processing",
    goal="Automate processing of insurance claims.",
    backstory="Agent for insurance claim processing.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Automate processing of insurance claims.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
