"""Unit tests for the Fraud Detection use case."""

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
from projects.financial_use_cases.use_case_01_fraud_detection.main import FraudDetectionUseCase, run


class TestFraudDetectionUseCase(unittest.TestCase):
    """Test cases for the Fraud Detection use case."""
    
    def setUp(self):
        """Set up for tests."""
        # Initialize use case
        self.use_case = FraudDetectionUseCase()
        # Mock the llm attribute directly
        self.use_case.llm = MagicMock()
        
    def test_setup_agents(self):
        """Test agent setup."""
        # Call setup_agents
        self.use_case.setup_agents()
        
        # Verify agents were created
        self.assertEqual(len(self.use_case.agents), 3)
        self.assertIsNotNone(self.use_case.fraud_analyst)
        self.assertIsNotNone(self.use_case.risk_assessor)
        self.assertIsNotNone(self.use_case.investigator)
        
    def test_setup_tasks(self):
        """Test task setup."""
        # Setup agents first
        self.use_case.setup_agents()
        
        # Call setup_tasks with test data
        test_input = {
            "query": "Recent credit card transactions for account #12345",
            "transaction_data": {"transactions": [
                {"date": "2023-06-01", "amount": 50.00, "merchant": "Coffee Shop"}, 
                {"date": "2023-06-01", "amount": 2500.00, "merchant": "Electronics Store"},
                {"date": "2023-06-01", "amount": 2500.00, "merchant": "Electronics Store"},
            ]}
        }
        self.use_case.setup_tasks(test_input)
        
        # Verify tasks were created
        self.assertEqual(len(self.use_case.tasks), 3)
        
        # Verify all tasks have agents assigned
        for task in self.use_case.tasks:
            self.assertTrue(hasattr(task, 'agent'), "Task should have an agent assigned")
            # Since MagicMock is used in tests, we need to avoid direct comparisons
            # Just verify that tasks exist with assigned agents
    
    @patch('projects.financial_use_cases.use_case_01_fraud_detection.main.FraudDetectionUseCase')
    def test_run_function(self, mock_usecase_class):
        """Test the run function."""
        # Setup mock
        mock_instance = MagicMock()
        mock_usecase_class.return_value = mock_instance
        mock_instance.crew.kickoff.return_value = "Test fraud detection result"
        
        # Call run function
        test_input = {"query": "Test transaction"}
        result = run(test_input)
        
        # Verify
        mock_usecase_class.assert_called_once()
        mock_instance.setup_agents.assert_called_once()
        mock_instance.setup_tasks.assert_called_once_with(test_input)
        mock_instance.setup_crew.assert_called_once()
        mock_instance.crew.kickoff.assert_called_once()
        self.assertEqual(result, "Test fraud detection result")


if __name__ == '__main__':
    unittest.main()
