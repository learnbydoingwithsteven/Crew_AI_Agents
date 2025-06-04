"""Peer Review Assistant example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Peer Review Assistant",
    goal="Provide feedback on draft manuscripts.",
    backstory="Agent for Peer Review Assistant.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Provide feedback on draft manuscripts.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
