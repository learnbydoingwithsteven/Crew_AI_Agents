"""Unit tests for the Research Paper Summarization use case."""

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
from projects.research_use_cases.use_case_09_research_paper_summarization.main import ResearchPaperSummarizationUseCase, run


class TestResearchPaperSummarizationUseCase(unittest.TestCase):
    """Test cases for the Research Paper Summarization use case."""
    
    def setUp(self):
        """Set up for tests."""
        # Initialize use case
        self.use_case = ResearchPaperSummarizationUseCase()
        # Mock the llm attribute directly
        self.use_case.llm = MagicMock()
        
    def test_setup_agents(self):
        """Test agent setup."""
        # Call setup_agents
        self.use_case.setup_agents()
        
        # Verify agents were created
        self.assertTrue(hasattr(self.use_case, 'content_analyst'))
        self.assertTrue(hasattr(self.use_case, 'literature_contextualizer'))
        self.assertTrue(hasattr(self.use_case, 'summary_writer'))
        self.assertEqual(len(self.use_case.agents), 3)
    
    @patch('crewai.Task')
    def test_setup_tasks(self, mock_task):
        """Test task setup."""
        # Setup mock for Task creation
        mock_task_instance = MagicMock()
        mock_task.return_value = mock_task_instance
        
        # Setup agents first
        self.use_case.agents = [MagicMock() for _ in range(3)]
        self.use_case.content_analyst = self.use_case.agents[0]
        self.use_case.literature_contextualizer = self.use_case.agents[1]
        self.use_case.summary_writer = self.use_case.agents[2]
        
        # Setup tasks
        test_input = {
            "paper_url": "https://example.com/paper.pdf",
            "query": "Summarize this research paper"
        }
        self.use_case.setup_tasks(test_input)
        
        # Verify tasks were created
        self.assertEqual(len(self.use_case.tasks), 3)
        
        # Check for task dependencies via context
        context_tasks = []
        for task in self.use_case.tasks:
            if hasattr(task, 'context') and task.context:
                context_tasks.append(task)
        self.assertGreaterEqual(len(context_tasks), 1, "At least one task should have context dependencies")
    
    @patch('projects.research_use_cases.use_case_09_research_paper_summarization.main.ResearchPaperSummarizationUseCase')
    def test_run_function(self, mock_usecase_class):
        """Test the run function."""
        # Setup mock
        mock_instance = MagicMock()
        mock_usecase_class.return_value = mock_instance
        mock_instance.crew.kickoff.return_value = "Test paper summarization result"
        
        # Call run function
        test_input = {"query": "AI ethics paper"}
        result = run(test_input)
        
        # Verify
        mock_usecase_class.assert_called_once()
        mock_instance.setup_agents.assert_called_once()
        mock_instance.setup_tasks.assert_called_once_with(test_input)
        mock_instance.setup_crew.assert_called_once()
        mock_instance.crew.kickoff.assert_called_once()
        self.assertEqual(result, "Test paper summarization result")


if __name__ == '__main__':
    unittest.main()
