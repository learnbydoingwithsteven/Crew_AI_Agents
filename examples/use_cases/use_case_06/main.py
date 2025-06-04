"""Use Case 6: Grant Proposal Support

Gather references from the knowledge graph to incorporate into a grant proposal.
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
                self.graph.add_node(word, type="keyword")
                self.graph.add_edge(doc.title, word)

    def collect_references(self, topic: str) -> List[str]:
        if topic not in self.graph:
            return []
        return [n for n in self.graph.neighbors(topic) if self.graph.nodes[n]["type"] == "document"]


def main() -> None:
    docs = [
        Document(title="Funding Strategies", content="grant writing research"),
        Document(title="Knowledge Graph Benefits", content="knowledge graph research"),
    ]
    agent = KnowledgeGraphAgent()
    agent.ingest(docs)
    print("References for 'research':", agent.collect_references("research"))


if __name__ == "__main__":
    main()
