"""Fraud Detection example using CrewAI with Ollama."""

from typing import Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from projects.utils import UseCase
from crewai import Agent, Task

class FraudDetectionUseCase(UseCase):
    """Fraud Detection use case implementation."""
    
    def setup_agents(self):
        """Set up the specialist agents for the Fraud Detection use case."""
        
        # Fraud Analyst Agent
        self.fraud_analyst = Agent(
            role="Fraud Analyst",
            goal="Identify suspicious financial transactions",
            backstory="You are an experienced fraud analyst with years of experience in detecting unusual patterns and "
                     "suspicious activities in financial data. Your expertise helps protect organizations from "
                     "financial crimes and losses.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Risk Assessment Agent
        self.risk_assessor = Agent(
            role="Risk Assessment Specialist",
            goal="Evaluate the severity and impact of potential fraud cases",
            backstory="With a background in financial risk management, you excel at determining the potential "
                     "impact of fraud incidents and recommending appropriate responses based on risk levels.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Investigation Agent
        self.investigator = Agent(
            role="Fraud Investigator",
            goal="Investigate suspected fraud cases and gather evidence",
            backstory="Your keen investigative skills help connect the dots in complex fraud schemes. "
                     "You know how to follow the trail of suspicious activities to uncover the full scope of fraud.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Add agents to the list
        self.agents = [self.fraud_analyst, self.risk_assessor, self.investigator]
    
    def setup_tasks(self, input_data: Dict[str, Any]):
        """Set up tasks for the Fraud Detection use case.
        
        Args:
            input_data (Dict[str, Any]): Input data containing transaction_data and query.
        """
        query = input_data.get("query", "")
        transaction_data = input_data.get("transaction_data", {})
        
        # Task 1: Detect Suspicious Patterns
        task_detect = Task(
            description=f"Analyze the following financial transactions for potential fraud: '{query}'. \n\n"
                      f"Transaction Data: {transaction_data}\n\n"
                      f"Identify patterns that may indicate fraudulent activity such as unusual transaction amounts, "
                      f"suspicious timing, abnormal frequency, or unexpected geographical locations.",
            agent=self.fraud_analyst
        )
        
        # Task 2: Assess Risk
        task_assess = Task(
            description=f"Evaluate the risk level of the identified suspicious patterns in '{query}'. \n\n"
                      f"Determine the potential financial impact, likelihood of fraud, and urgency of response. "
                      f"Categorize each suspicious activity by risk level (High, Medium, Low).",
            agent=self.risk_assessor,
            context=[task_detect]
        )
        
        # Task 3: Investigate and Recommend
        task_investigate = Task(
            description=f"Conduct a detailed investigation of the high-risk suspicious activities in '{query}'. \n\n"
                      f"Provide evidence supporting the fraud determination, potential fraud schemes involved, "
                      f"and recommended actions to address the situation and prevent future occurrences.",
            agent=self.investigator,
            context=[task_detect, task_assess]
        )
        
        # Add tasks to the list
        self.tasks = [task_detect, task_assess, task_investigate]
    
    def setup_crew(self):
        self.crew = Crew(agents=self.agents, tasks=self.tasks)


def run(input_data: Dict[str, Any]) -> str:
    """Run the Fraud Detection use case.
    
    Args:
        input_data (Dict[str, Any]): Input data containing transaction_data and optionally query.
        
    Returns:
        str: The result of the use case execution.
    """
    use_case = FraudDetectionUseCase()
    use_case.setup_agents()
    use_case.setup_tasks(input_data)
    use_case.setup_crew()
    return use_case.crew.kickoff()


if __name__ == "__main__":
    # Example usage
    result = run({
        "query": "Recent credit card transactions for account #12345",
        "transaction_data": {
            "transactions": [
                {"date": "2023-06-01", "amount": 50.00, "merchant": "Local Coffee Shop", "location": "New York"}, 
                {"date": "2023-06-01", "amount": 2500.00, "merchant": "Electronics Store", "location": "New York"},
                {"date": "2023-06-01", "amount": 2500.00, "merchant": "Electronics Store", "location": "Los Angeles"},
                {"date": "2023-06-01", "amount": 2500.00, "merchant": "Electronics Store", "location": "Miami"}
            ]
        }
    })
    print(result)
