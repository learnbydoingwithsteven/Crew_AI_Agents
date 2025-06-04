
"""Portfolio Optimization example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Portfolio Optimization",
    goal="Optimize investment portfolios using AI agents.",
    backstory="Agent for portfolio optimization.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Optimize investment portfolios using AI agents.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
