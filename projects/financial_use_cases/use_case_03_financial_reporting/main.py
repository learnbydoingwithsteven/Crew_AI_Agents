
"""Automated Financial Reporting example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Automated Financial Reporting",
    goal="Generate periodic financial reports automatically.",
    backstory="Agent for automated financial reporting.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Generate periodic financial reports automatically.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
