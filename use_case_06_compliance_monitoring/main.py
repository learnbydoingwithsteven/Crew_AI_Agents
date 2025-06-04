
"""Compliance Monitoring example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Compliance Monitoring",
    goal="Monitor transactions for regulatory compliance.",
    backstory="Agent for compliance monitoring.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Monitor transactions for regulatory compliance.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
