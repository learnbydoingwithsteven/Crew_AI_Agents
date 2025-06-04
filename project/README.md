# Crew_AI_Agents

This repository contains examples and documentation for using `crewai` agents with a local model via **Ollama**. The focus is on knowledge graph workflows that can accelerate research tasks.

## Contents

- **[USE_CASES.md](USE_CASES.md)** – Ten sample research workflows demonstrating how agents leverage a knowledge graph.
- **examples/basic/knowledge_graph_example.py** – Minimal script showing how agents might build and query a lightweight knowledge graph.
- **examples/use_cases/** – Folders with code for each use case. Each has a `src/` directory containing a simple Python script.

## Usage

1. Install Python 3 with `networkx` and optionally `crewai`.
2. Ensure you have a local model configured for **Ollama** if you want to integrate language model responses.
3. Run any script directly, e.g.:
   ```bash
   python project/examples/basic/knowledge_graph_example.py
   ```
   Each use case script functions independently and can be adapted to your own research projects.
