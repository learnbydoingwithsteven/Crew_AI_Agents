"""Configuration and patching for test environment."""

import sys
import unittest.mock as mock

# Create mock classes for pydantic compatibility
class MockInstanceOf:
    """Mock class for pydantic InstanceOf validator."""
    def __init__(self, *args, **kwargs):
        pass
        
class MockBaseModel:
    """Mock class for pydantic BaseModel."""
    def __init__(self, *args, **kwargs):
        pass

# Apply the patch before any imports
mock_pydantic = mock.MagicMock()
mock_pydantic.Field = mock.MagicMock()
mock_pydantic.InstanceOf = MockInstanceOf
mock_pydantic.PrivateAttr = mock.MagicMock()
mock_pydantic.model_validator = mock.MagicMock()
mock_pydantic.BaseModel = MockBaseModel

# Apply pydantic patches
sys.modules['pydantic'] = mock_pydantic
sys.modules['pydantic_v1'] = mock_pydantic

# Mock langchain modules (legacy)
mock_langchain = mock.MagicMock()
sys.modules['langchain'] = mock_langchain

# Mock common langchain submodules (legacy)
langchain_submodules = [
    'pydantic_v1',
    'schema',
    'tools',
    'agents',
    'callbacks',
    'load',
    'llms',
    'chat_models',
    'utilities',
    'prompts',
    'chains'
]

# Create all common submodules (legacy)
for submodule in langchain_submodules:
    mock_submodule = mock.MagicMock()
    sys.modules[f'langchain.{submodule}'] = mock_submodule
    
    # Add nested submodules for common patterns
    if submodule in ['tools', 'agents', 'callbacks', 'chains', 'llms', 'prompts']:
        # Common pattern: langchain.tools.xyz
        sys.modules[f'langchain.{submodule}.base'] = mock.MagicMock()
        sys.modules[f'langchain.{submodule}.loading'] = mock.MagicMock()

# Add special case BaseModel to pydantic_v1
sys.modules['langchain.pydantic_v1'].BaseModel = MockBaseModel
sys.modules['langchain.pydantic_v1'].Field = mock.MagicMock()
sys.modules['langchain.pydantic_v1'].PrivateAttr = mock.MagicMock()

# Create the Ollama class in langchain.llms
mock_ollama = mock.MagicMock()
sys.modules['langchain.llms'].Ollama = mock_ollama

# Mock langchain_core package
mock_langchain_core = mock.MagicMock()
sys.modules['langchain_core'] = mock_langchain_core

# Mock common langchain_core submodules
core_submodules = [
    'outputs',
    'language_models',
    'messages',
    'prompts',
    'tools',
    'agents',
    'callbacks',
    'documents',
    'embeddings',
    'pydantic_v1',
    'runnables',
    'utils',
    'caches'
]

# Create all common langchain_core submodules
for submodule in core_submodules:
    mock_submodule = mock.MagicMock()
    sys.modules[f'langchain_core.{submodule}'] = mock_submodule
    
    # Create common nested modules
    sys.modules[f'langchain_core.{submodule}.base'] = mock.MagicMock()

# Create specific nested modules for langchain_core
sys.modules['langchain_core.outputs.generation'] = mock.MagicMock()
sys.modules['langchain_core.language_models.llms'] = mock.MagicMock()
sys.modules['langchain_core.language_models.chat_models'] = mock.MagicMock()

# Add special classes needed
sys.modules['langchain_core.outputs'].Generation = mock.MagicMock()
sys.modules['langchain_core.language_models.llms'].BaseLLM = mock.MagicMock()
sys.modules['langchain_core.pydantic_v1'].BaseModel = MockBaseModel
sys.modules['langchain_core.caches'].BaseCache = mock.MagicMock()

# Mock langchain_community package
mock_langchain_community = mock.MagicMock()
sys.modules['langchain_community'] = mock_langchain_community

# Mock common langchain_community submodules
community_submodules = [
    'llms',
    'chat_models',
    'embeddings',
    'tools',
    'utilities',
    'vectorstores',
    'document_loaders'
]

# Create all common langchain_community submodules
for submodule in community_submodules:
    mock_submodule = mock.MagicMock()
    sys.modules[f'langchain_community.{submodule}'] = mock_submodule

# Add Ollama to langchain_community
mock_community_ollama = mock.MagicMock()
sys.modules['langchain_community.llms'].Ollama = mock_community_ollama
sys.modules['langchain_community.utilities'].WikipediaAPIWrapper = mock.MagicMock()

# Now we can safely import crewai and related modules for testing
mock_crewai = mock.MagicMock()
mock_crewai.Agent = mock.MagicMock()
mock_crewai.Task = mock.MagicMock()
mock_crewai.Crew = mock.MagicMock()
mock_crewai.Process = mock.MagicMock()
sys.modules['crewai'] = mock_crewai
sys.modules['crewai.agent'] = mock.MagicMock()
sys.modules['crewai.task'] = mock.MagicMock()
sys.modules['crewai.crew'] = mock.MagicMock()

# Mock other dependencies
sys.modules['ollama'] = mock.MagicMock()
