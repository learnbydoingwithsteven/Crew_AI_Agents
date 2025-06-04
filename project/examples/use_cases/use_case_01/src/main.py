"""Use Case 1: Knowledge Graph Creation

Demonstrates how a CrewAI-powered agent could ingest documents using a local
Ollama model and store key terms in a lightweight knowledge graph. The example
uses ``networkx`` as a placeholder for the graph and omits real model calls for
simplicity.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
import networkx as nx

@dataclass
class Document:
    title: str
    content: str

class KnowledgeGraphAgent:
    def __init__(self) -> None:
        self.graph = nx.Graph()

    def ingest(self, docs: Iterable[Document]) -> None:
        for doc in docs:
            self.graph.add_node(doc.title, type="document")
            for word in set(doc.content.lower().split()):
                self.graph.add_node(word, type="keyword")
                self.graph.add_edge(doc.title, word)


def main() -> None:
    docs = [
        Document(title="LLM Knowledge Graphs", content="using llms to build knowledge graphs"),
        Document(title="Research Agents", content="agents automate research tasks"),
    ]
    agent = KnowledgeGraphAgent()
    agent.ingest(docs)
    print("Nodes:", list(agent.graph.nodes()))
    print("Edges:", list(agent.graph.edges()))


if __name__ == "__main__":
    main()
