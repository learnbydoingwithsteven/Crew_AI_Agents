
"""Risk Management example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Risk Management",
    goal="Use a crew to assess risk in derivative portfolios.",
    backstory="Agent for risk management.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Use a crew to assess risk in derivative portfolios.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
