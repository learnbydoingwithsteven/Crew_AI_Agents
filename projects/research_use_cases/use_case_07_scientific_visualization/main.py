"""Scientific Visualization example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Scientific Visualization",
    goal="Generate visualizations for publications.",
    backstory="Agent for Scientific Visualization.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Generate visualizations for publications.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
