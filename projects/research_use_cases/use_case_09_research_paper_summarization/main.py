"""Research Paper Summarization example using CrewAI with Ollama."""

from typing import Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from projects.utils import UseCase
from crewai import Agent, Task

class ResearchPaperSummarizationUseCase(UseCase):
    """Research Paper Summarization use case implementation."""
    
    def setup_agents(self):
        """Set up the specialist agents for the Research Paper Summarization use case."""
        
        # Content Analysis Agent
        self.content_analyst = Agent(
            role="Research Content Analyst",
            goal="Analyze research papers for key findings, methodologies, and contributions",
            backstory="As an expert in research content analysis with years of experience across multiple disciplines, "
                      "you excel at extracting the critical information from complex academic papers and understanding "
                      "their methodological approaches.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Literature Contextualization Agent
        self.literature_contextualizer = Agent(
            role="Literature Context Specialist",
            goal="Place research papers within the broader context of their field",
            backstory="You have an encyclopedic knowledge of academic literature across multiple disciplines and "
                      "can quickly identify how new research relates to existing knowledge, highlighting its "
                      "significance within the field.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Summary Writing Agent
        self.summary_writer = Agent(
            role="Academic Summary Writer",
            goal="Create concise, accurate summaries of research papers that capture their essence",
            backstory="With a talent for clear academic writing, you can distill complex research into accessible "
                      "summaries that preserve the core message and importance of the original work.",
            verbose=True,
            llm=self.llm,
            tools=self.tools
        )
        
        # Add agents to the list
        self.agents = [self.content_analyst, self.literature_contextualizer, self.summary_writer]
    
    def setup_tasks(self, input_data: Dict[str, Any]):
        """Set up tasks for the Research Paper Summarization use case.
        
        Args:
            input_data (Dict[str, Any]): Input data containing query and paper_content.
        """
        query = input_data.get("query", "")
        paper_content = input_data.get("paper_content", "")
        
        # Task 1: Analyze Paper Content
        task_analyze = Task(
            description=f"Analyze the following research paper: '{query}'. \n\n"
                      f"Paper Content: {paper_content}\n\n"
                      f"Extract key findings, methodologies, research questions, and contributions. "
                      f"Identify the main arguments and evidence presented.",
            agent=self.content_analyst
        )
        
        # Task 2: Contextualize Research
        task_contextualize = Task(
            description=f"Based on the analysis of '{query}', place this research within its broader academic context. \n\n"
                      f"Identify related work, research gaps it addresses, and its significance to the field. "
                      f"Evaluate how this paper contributes to or challenges existing knowledge.",
            agent=self.literature_contextualizer,
            context=[task_analyze]
        )
        
        # Task 3: Write Summary
        task_summarize = Task(
            description=f"Create a comprehensive yet concise summary of the research paper '{query}' \n\n"
                      f"Include: (1) Main research questions and objectives, "
                      f"(2) Methodology and approach, "
                      f"(3) Key findings and results, "
                      f"(4) Significance and implications, "
                      f"(5) Limitations and future research directions. "
                      f"Make the summary accessible while preserving academic rigor.",
            agent=self.summary_writer,
            context=[task_analyze, task_contextualize]
        )
        
        # Add tasks to the list
        self.tasks = [task_analyze, task_contextualize, task_summarize]


def run(input_data: Dict[str, Any]) -> str:
    """Run the Research Paper Summarization use case.
    
    Args:
        input_data (Dict[str, Any]): Input data containing query and optionally paper_content.
        
    Returns:
        str: The result of the use case execution.
    """
    use_case = ResearchPaperSummarizationUseCase()
    use_case.setup_agents()
    use_case.setup_tasks(input_data)
    use_case.setup_crew()
    return use_case.crew.kickoff()
    

if __name__ == "__main__":
    # Example usage
    result = run({
        "query": "Recent Advances in Natural Language Processing",
        "paper_content": "Sample paper content about NLP advancements..."
    })
    print(result)
