"""Academic Citation Management example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Academic Citation Management",
    goal="Manage references and citations.",
    backstory="Agent for Academic Citation Management.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Manage references and citations.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
