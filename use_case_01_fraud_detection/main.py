"""Fraud Detection example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

# Connect to local Ollama model
llm = Ollama(model="llama3", base_url="http://localhost:11434")

fraud_agent = Agent(
    role="Fraud Analyst",
    goal="Identify suspicious financial transactions",
    backstory="You analyze transaction logs to find patterns of fraud.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Analyze the latest transactions for fraudulent behavior.",
    expected_output="A list of suspicious transactions with explanation.",
    agent=fraud_agent,
)

crew = Crew(agents=[fraud_agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
