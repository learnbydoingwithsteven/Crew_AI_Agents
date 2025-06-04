"""Research Paper Summarization example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Research Paper Summarization",
    goal="Create concise paper summaries.",
    backstory="Agent for Research Paper Summarization.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Create concise paper summaries.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
