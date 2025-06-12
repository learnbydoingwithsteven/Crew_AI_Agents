"""Core module for Crew AI Agents UI application."""

import importlib
import os
import sys
import json
from typing import Dict, List, Any, Optional

# Add the parent directory to sys.path to allow importing from projects
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class UseCaseManager:
    """Manages the loading and execution of use cases."""
    
    def __init__(self):
        self.financial_use_cases = self._load_use_cases('financial_use_cases')
        self.research_use_cases = self._load_use_cases('research_use_cases')
        
    def _load_use_cases(self, category: str) -> Dict[str, Dict[str, Any]]:
        """Load use case metadata from a specific category."""
        use_cases = {}
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'projects', category))
        
        if not os.path.exists(base_dir):
            return use_cases
            
        for item in os.listdir(base_dir):
            if item.startswith('use_case_') and os.path.isdir(os.path.join(base_dir, item)):
                try:
                    # Try to load README.md for description
                    readme_path = os.path.join(base_dir, item, 'README.md')
                    description = "No description available"
                    if os.path.exists(readme_path):
                        with open(readme_path, 'r', encoding='utf-8') as f:
                            content = f.read().strip()
                            # Extract title from first heading
                            title_line = next((line for line in content.split('\n') 
                                            if line.startswith('# ')), None)
                            title = title_line[2:] if title_line else item.replace('_', ' ').title()
                            
                            # Extract description from content
                            desc_lines = [line for line in content.split('\n') 
                                        if line and not line.startswith('#')]
                            description = ' '.join(desc_lines) if desc_lines else "No description available"
                    
                    # Create use case metadata
                    use_cases[item] = {
                        'id': item,
                        'title': title,
                        'description': description[:200] + '...' if len(description) > 200 else description,
                        'category': category,
                        'module_path': f"projects.{category}.{item}.main"
                    }
                except Exception as e:
                    print(f"Error loading use case {item}: {str(e)}")
                    
        return use_cases
        
    def get_all_use_cases(self) -> Dict[str, Dict[str, Any]]:
        """Get all use cases from both categories."""
        all_cases = {}
        all_cases.update(self.financial_use_cases)
        all_cases.update(self.research_use_cases)
        return all_cases
        
    def run_use_case(self, use_case_id: str, input_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run a specific use case with optional input data."""
        # Find the use case in either category
        use_case = self.financial_use_cases.get(use_case_id) or self.research_use_cases.get(use_case_id)
        
        if not use_case:
            return {"error": f"Use case {use_case_id} not found"}
            
        try:
            # Dynamically import the module
            module = importlib.import_module(use_case['module_path'])
            
            # Reset any module level state to ensure clean execution
            importlib.reload(module)
            
            # Execute the use case with input_data
            # Store current stdout to capture output
            import io
            from contextlib import redirect_stdout
            
            # Create buffer to capture stdout
            buffer = io.StringIO()
            
            # Run with captured stdout
            with redirect_stdout(buffer):
                # Check if the module has a run function that accepts input_data
                if hasattr(module, 'run') and callable(module.run):
                    result = module.run(input_data)
                else:
                    # Fall back to standard main execution
                    if hasattr(module, 'crew') and hasattr(module.crew, 'kickoff'):
                        result = module.crew.kickoff()
                    else:
                        result = "Module executed but no result available"
                        
            # Get captured output
            output = buffer.getvalue()
            
            return {
                "result": result,
                "output": output,
                "success": True
            }
            
        except Exception as e:
            import traceback
            return {
                "error": str(e),
                "traceback": traceback.format_exc(),
                "success": False
            }
