
"""Loan Default Prediction example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Loan Default Prediction",
    goal="Predict potential loan defaults.",
    backstory="Agent for loan default prediction.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Predict potential loan defaults.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
