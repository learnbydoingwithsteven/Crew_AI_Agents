
"""Algorithmic Trading Assistant example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Algorithmic Trading Assistant",
    goal="Assist in developing algorithmic trading strategies.",
    backstory="Agent for algorithmic trading assistant.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Assist in developing algorithmic trading strategies.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
