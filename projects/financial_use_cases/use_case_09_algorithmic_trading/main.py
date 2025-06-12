"""Algorithmic Trading Assistant example using CrewAI with Ollama."""

from typing import Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from projects.utils import UseCase
from crewai import Agent, Task

class AlgorithmicTradingUseCase(UseCase):
    """Algorithmic Trading use case implementation."""
    
    def setup_agents(self):
        """Set up the specialist agents for the Algorithmic Trading use case."""
        
        # Market Research Analyst
        self.market_analyst = Agent(
            role="Market Research Analyst",
            goal="Analyze market trends and patterns for trading opportunities",
            backstory="A seasoned market researcher with expertise in identifying trading patterns "
                     "and market inefficiencies. You have years of experience analyzing various "
                     "financial instruments and can spot potential trading opportunities.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Quantitative Strategy Developer
        self.quant_developer = Agent(
            role="Quantitative Strategy Developer",
            goal="Design and implement algorithmic trading strategies based on market analysis",
            backstory="You are a brilliant quantitative analyst with a background in mathematics "
                     "and computer science. You excel at translating market insights into precise "
                     "algorithmic trading strategies with clearly defined rules.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Backtesting Engineer
        self.backtest_engineer = Agent(
            role="Backtesting and Risk Management Engineer",
            goal="Test trading strategies against historical data and evaluate risk metrics",
            backstory="With deep expertise in statistical analysis and risk management, you evaluate "
                     "trading strategies to ensure their robustness across different market conditions. "
                     "You're known for your thorough approach to risk assessment.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Add agents to the list
        self.agents = [self.market_analyst, self.quant_developer, self.backtest_engineer]
    
    def setup_tasks(self, input_data: Dict[str, Any]):
        """Set up tasks for the Algorithmic Trading use case.
        
        Args:
            input_data (Dict[str, Any]): Input data containing query and market_data.
        """
        query = input_data.get("query", "")
        market_data = input_data.get("market_data", {})
        
        # Market Research Task
        task_market_research = Task(
            description=f"Analyze current market conditions and identify potential trading opportunities for '{query}'. \n\n"
                      f"Market Data: {market_data}\n\n"
                      f"Identify key patterns, trends, and market inefficiencies that could be exploited. "
                      f"Consider different timeframes and relevant market factors.",
            agent=self.market_analyst
        )
        
        # Strategy Development Task
        task_strategy_development = Task(
            description=f"Develop an algorithmic trading strategy for '{query}' based on the market analysis. \n\n"
                      f"Design a comprehensive strategy that includes: \n"
                      f"1. Entry and exit rules\n"
                      f"2. Position sizing methodology\n"
                      f"3. Risk management parameters\n"
                      f"4. Technical indicators or fundamental factors to monitor",
            agent=self.quant_developer,
            context=[task_market_research]
        )
        
        # Backtesting and Risk Analysis Task
        task_backtesting = Task(
            description=f"Evaluate the proposed algorithmic trading strategy for '{query}'. \n\n"
                      f"Perform a theoretical backtest analysis that includes: \n"
                      f"1. Expected performance metrics (Sharpe ratio, max drawdown, win rate)\n"
                      f"2. Risk assessment under various market conditions\n"
                      f"3. Optimization suggestions\n"
                      f"4. Implementation recommendations",
            agent=self.backtest_engineer,
            context=[task_market_research, task_strategy_development]
        )
        
        # Add tasks to the list
        self.tasks = [task_market_research, task_strategy_development, task_backtesting]


def run(input_data: Dict[str, Any]) -> str:
    """Run the Algorithmic Trading use case.
    
    Args:
        input_data (Dict[str, Any]): Input data containing query and optionally market_data.
        
    Returns:
        str: The result of the use case execution.
    """
    use_case = AlgorithmicTradingUseCase()
    use_case.setup_agents()
    use_case.setup_tasks(input_data)
    use_case.setup_crew()
    return use_case.crew.kickoff()
    

if __name__ == "__main__":
    # Example usage
    result = run({
        "query": "Mean reversion strategy for tech stocks",
        "market_data": {"AAPL": [150, 155, 153], "MSFT": [250, 248, 255]}
    })
    print(result)
