"""Research Project Management example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Research Project Management",
    goal="Track tasks for a research project.",
    backstory="Agent for Research Project Management.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Track tasks for a research project.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
