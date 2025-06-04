"""Example knowledge graph workflow using crewai with a local model via Ollama.

This script parses a few documents and builds a very simple knowledge graph.
It then performs a trivial query to demonstrate how the graph could be used to
speed up research tasks.

The example avoids heavy dependencies and serves as an outline for integrating
crewai agents with a local language model. Replace the placeholder logic with
actual calls to `crewai` and your model of choice.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List
import networkx as nx

@dataclass
class Document:
    """Simple document structure."""
    title: str
    content: str

class KnowledgeGraphAgent:
    """Stores a lightweight knowledge graph of documents and keywords."""

    def __init__(self) -> None:
        self.graph = nx.Graph()

    def ingest(self, docs: Iterable[Document]) -> None:
        """Add documents to the graph linking titles to keywords."""
        for doc in docs:
            self.graph.add_node(doc.title, type="document")
            for word in set(doc.content.lower().split()):
                self.graph.add_node(word, type="keyword")
                self.graph.add_edge(doc.title, word)

    def query(self, keyword: str) -> List[str]:
        """Return document titles related to a keyword."""
        if keyword not in self.graph:
            return []
        return [nbr for nbr in self.graph.neighbors(keyword) if self.graph.nodes[nbr]["type"] == "document"]


def main() -> None:
    docs = [
        Document(title="LLM Knowledge Graphs", content="using llms to build knowledge graphs"),
        Document(title="Research Agents", content="agents automate research tasks"),
    ]

    agent = KnowledgeGraphAgent()
    agent.ingest(docs)

    related = agent.query("research")
    print("Documents related to 'research':", related)


if __name__ == "__main__":
    main()
