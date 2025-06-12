"""Common utilities for Crew AI use cases."""

import os
from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_community.llms import Ollama

class UseCase:
    """Base class for all use cases."""
    
    def __init__(self, model_name: str = "llama3", base_url: str = "http://localhost:11434"):
        """Initialize the use case with a model.
        
        Args:
            model_name: Name of the Ollama model to use
            base_url: Base URL for the Ollama API
        """
        self.model_name = model_name
        self.base_url = base_url
        self.llm = self._init_llm()
        self.tools = self._init_tools()
        self.agents = []
        self.tasks = []
        self.crew = None
        
    def _init_llm(self):
        """Initialize the language model."""
        return Ollama(model=self.model_name, base_url=self.base_url)
    
    def _init_tools(self):
        """Initialize tools for agents."""
        tools = []
        
        # Add search tools
        try:
            search_tool = DuckDuckGoSearchRun()
            tools.append(search_tool)
        except:
            pass
            
        # Add Wikipedia tool
        try:
            wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
            tools.append(wikipedia_tool)
        except:
            pass
            
        return tools
        
    def setup_agents(self):
        """Set up agents for the use case. Override in subclasses."""
        pass
        
    def setup_tasks(self):
        """Set up tasks for the use case. Override in subclasses."""
        pass
        
    def setup_crew(self, process: Process = Process.sequential):
        """Set up the crew with configured agents and tasks.
        
        Args:
            process: Process type for the crew
        """
        if not self.agents:
            self.setup_agents()
            
        if not self.tasks:
            self.setup_tasks()
            
        self.crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=process,
            verbose=True
        )
        
    def run(self, input_data: Optional[Dict[str, Any]] = None) -> str:
        """Run the use case with optional input data.
        
        Args:
            input_data: Optional dictionary of input data
            
        Returns:
            The result of running the crew
        """
        # Set up crew if not already done
        if not self.crew:
            self.setup_crew()
            
        # Kickoff the crew and return the result
        result = self.crew.kickoff()
        return result
