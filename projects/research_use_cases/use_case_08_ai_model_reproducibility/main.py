"""AI Model Reproducibility example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="AI Model Reproducibility",
    goal="Check reproducibility of AI models.",
    backstory="Agent for AI Model Reproducibility.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Check reproducibility of AI models.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
