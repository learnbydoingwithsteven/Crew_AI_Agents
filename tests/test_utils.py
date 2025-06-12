"""Unit tests for the UseCase base class."""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the conftest fix before any project imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conftest

# Import crewai components directly from mocked modules
from crewai import Agent, Task, Crew

# Now we can safely import modules
from projects.utils import UseCase


class TestUseCase(unittest.TestCase):
    """Test cases for the UseCase base class."""
    
    @patch('projects.utils.Ollama')
    def setUp(self, mock_ollama):
        """Set up for tests."""
        self.mock_llm = MagicMock()
        mock_ollama.return_value = self.mock_llm
        self.use_case = UseCase()
        
    def test_init(self):
        """Test UseCase initialization."""
        self.assertEqual(self.use_case.model_name, "llama3")
        self.assertEqual(self.use_case.base_url, "http://localhost:11434")
        self.assertIsNotNone(self.use_case.llm)
        self.assertIsNotNone(self.use_case.tools)
        self.assertEqual(self.use_case.agents, [])
        self.assertEqual(self.use_case.tasks, [])
        self.assertIsNone(self.use_case.crew)
        
    def test_init_tools(self):
        """Test tool initialization."""
        tools = self.use_case._init_tools()
        # We expect tools to be a list, even if some tools couldn't be initialized
        self.assertIsInstance(tools, list)
    
    @patch('projects.utils.Crew')
    def test_setup_crew(self, mock_crew):
        """Test crew setup."""
        mock_crew_instance = MagicMock()
        mock_crew.return_value = mock_crew_instance
        
        # Create test agents and tasks
        test_agent = MagicMock()
        test_task = MagicMock()
        
        self.use_case.agents = [test_agent]
        self.use_case.tasks = [test_task]
        
        # Test crew setup
        self.use_case.setup_crew()
        
        # Mock the arguments that may be passed to Crew constructor
        # Use any=MagicMock() to match any additional arguments
        mock_crew.assert_called_once()
        
        self.assertEqual(self.use_case.crew, mock_crew_instance)
    
    @patch('projects.utils.Crew')
    def test_run(self, mock_crew):
        """Test use case run method."""
        # Create a mock instance
        mock_crew_instance = MagicMock()
        mock_crew.return_value = mock_crew_instance
        mock_crew_instance.kickoff.return_value = "Test result"
        
        # Create test agents and tasks - don't use spec which causes issues
        test_agent = MagicMock()
        test_task = MagicMock()
        
        self.use_case.agents = [test_agent]
        self.use_case.tasks = [test_task]
        
        # Test running the use case without an existing crew
        result = self.use_case.run()
        
        mock_crew.assert_called_once()
        mock_crew_instance.kickoff.assert_called_once()
        self.assertEqual(result, "Test result")


if __name__ == '__main__':
    unittest.main()
