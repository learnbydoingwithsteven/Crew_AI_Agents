"""Use Case 5: Experiment Design Assistance

Illustrates how a CrewAI agent might mine the knowledge graph for previously
used techniques. When paired with a local Ollama model, the agent could suggest
relevant experimental procedures. This script simply extracts unique method
keywords from the stored documents.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List
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
                self.graph.add_node(word, type="method")
                self.graph.add_edge(doc.title, word)

    def recommend_methods(self) -> List[str]:
        methods = [n for n, d in self.graph.nodes(data=True) if d["type"] == "method"]
        return sorted(set(methods))


def main() -> None:
    docs = [
        Document(title="Image Classification", content="use cnn and torch"),
        Document(title="Graph Analysis", content="apply networkx and centrality"),
    ]
    agent = KnowledgeGraphAgent()
    agent.ingest(docs)
    print("Suggested methods:", agent.recommend_methods())


if __name__ == "__main__":
    main()
