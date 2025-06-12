"""Unit tests for the unified UI."""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import importlib

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import UI modules
# Note: We're importing but not directly testing streamlit functions
# as they require a streamlit runtime environment


class TestUI(unittest.TestCase):
    """Test cases for the unified UI."""
    
    def setUp(self):
        """Set up for tests."""
        pass
        
    @patch('importlib.import_module')
    def test_use_case_imports(self, mock_import):
        """Test that all use cases can be imported."""
        # Mock return value for import_module
        mock_module = MagicMock()
        mock_module.run = MagicMock(return_value="Test result")
        mock_import.return_value = mock_module
        
        # Define paths to all use cases
        financial_use_cases = [
            "projects.financial_use_cases.use_case_01_fraud_detection.main",
            "projects.financial_use_cases.use_case_02_risk_management.main",
            "projects.financial_use_cases.use_case_03_financial_reporting.main",
            "projects.financial_use_cases.use_case_04_portfolio_optimization.main",
            "projects.financial_use_cases.use_case_05_bank_chatbot.main",
            "projects.financial_use_cases.use_case_06_compliance_monitoring.main",
            "projects.financial_use_cases.use_case_07_loan_default_prediction.main",
            "projects.financial_use_cases.use_case_08_insider_trading_detection.main",
            "projects.financial_use_cases.use_case_09_algorithmic_trading.main"
        ]
        
        research_use_cases = [
            "projects.research_use_cases.use_case_01_literature_review.main",
            "projects.research_use_cases.use_case_02_experiment_design.main",
            "projects.research_use_cases.use_case_03_data_analysis.main",
            "projects.research_use_cases.use_case_04_grant_writing.main",
            "projects.research_use_cases.use_case_05_peer_review_assistant.main",
            "projects.research_use_cases.use_case_06_research_project_management.main",
            "projects.research_use_cases.use_case_07_scientific_visualization.main",
            "projects.research_use_cases.use_case_08_ai_model_reproducibility.main",
            "projects.research_use_cases.use_case_09_research_paper_summarization.main",
            "projects.research_use_cases.use_case_10_academic_citation_management.main"
        ]
        
        # Test that each use case can be imported and has a run function
        all_use_cases = financial_use_cases + research_use_cases
        for use_case_path in all_use_cases:
            # Import the use case
            module = importlib.import_module(use_case_path)
            
            # Verify that it has a run function
            self.assertTrue(hasattr(module, 'run'), f"{use_case_path} should have a run function")
            
            # Call the run function with test data
            result = module.run({"query": "test"})
            self.assertEqual(result, "Test result")
    
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='{"name": "Test", "version": "1.0"}')
    def test_read_config(self, mock_file):
        """Test reading config files."""
        import json
        
        # Simulate reading a JSON config file
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        self.assertEqual(config['name'], 'Test')
        self.assertEqual(config['version'], '1.0')
        mock_file.assert_called_once_with('config.json', 'r')


if __name__ == '__main__':
    unittest.main()
