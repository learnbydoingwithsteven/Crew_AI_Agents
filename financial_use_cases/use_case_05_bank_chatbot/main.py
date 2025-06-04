
"""Bank Customer Service Chatbot example using CrewAI with Ollama."""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

agent = Agent(
    role="Bank Customer Service Chatbot",
    goal="Provide customer support for banking queries.",
    backstory="Agent for bank customer service chatbot.",
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Provide customer support for banking queries.",
    expected_output="Result of the task.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
