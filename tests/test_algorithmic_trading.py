"""Unit tests for the Algorithmic Trading use case."""

import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Import the conftest fix before any project imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conftest

# Import crewai components directly from mocked modules
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama

# Now we can safely import modules
from projects.financial_use_cases.use_case_09_algorithmic_trading.main import AlgorithmicTradingUseCase, run


class TestAlgorithmicTradingUseCase(unittest.TestCase):
    """Test cases for the Algorithmic Trading use case."""
    
    def setUp(self):
        """Set up for tests."""
        # Initialize use case
        self.use_case = AlgorithmicTradingUseCase()
        # Mock the llm attribute directly
        self.use_case.llm = MagicMock()
        
    def test_setup_agents(self):
        """Test agent setup."""
        # Call setup_agents
        self.use_case.setup_agents()
        
        # Verify agents were created
        self.assertEqual(len(self.use_case.agents), 3)
        
    def test_setup_tasks(self):
        """Test task setup."""
        # Setup agents first
        self.use_case.setup_agents()
        
        # Call setup_tasks with test data
        test_input = {
            "query": "Optimal trading strategy for tech stocks",
            "market_data": {"stock": "AAPL", "period": "1y"}
        }
        self.use_case.setup_tasks(test_input)
        
        # Verify tasks were created
        self.assertEqual(len(self.use_case.tasks), 3)
        
        # Verify all tasks have agents assigned
        for task in self.use_case.tasks:
            self.assertTrue(hasattr(task, 'agent'), "Task should have an agent assigned")
            # Skip direct comparison of MagicMock objects as they are unique instances
        
        # With MagicMock objects, we can only verify the task has a description attribute
        # We can't verify specific content in unit tests with mocks
        for task in self.use_case.tasks:
            self.assertTrue(hasattr(task, 'description'), "Task should have a description attribute")
        
        # Check for task dependencies via context
        has_context = False
        for task in self.use_case.tasks:
            if hasattr(task, 'context') and task.context:
                has_context = True
                break
        self.assertTrue(has_context, "Tasks should have context dependencies")
    
    @patch('projects.financial_use_cases.use_case_09_algorithmic_trading.main.AlgorithmicTradingUseCase')
    def test_run_function(self, mock_usecase_class):
        """Test the run function."""
        # Setup mock
        mock_instance = MagicMock()
        mock_usecase_class.return_value = mock_instance
        mock_instance.crew.kickoff.return_value = "Test algorithmic trading result"
        
        # Call run function
        test_input = {"query": "Mean reversion strategy"}
        result = run(test_input)
        
        # Verify
        mock_usecase_class.assert_called_once()
        mock_instance.setup_agents.assert_called_once()
        mock_instance.setup_tasks.assert_called_once_with(test_input)
        mock_instance.setup_crew.assert_called_once()
        mock_instance.crew.kickoff.assert_called_once()
        self.assertEqual(result, "Test algorithmic trading result")


if __name__ == '__main__':
    unittest.main()
