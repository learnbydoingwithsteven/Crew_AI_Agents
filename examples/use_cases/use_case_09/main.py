"""Use Case 9: Real-time Research Updates

Simulate monitoring new documents and automatically adding them to the knowledge graph.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
import networkx as nx

@dataclass
class Document:
    title: str
    content: str

class UpdateAgent:
    def __init__(self) -> None:
        self.graph = nx.Graph()

    def ingest(self, docs: Iterable[Document]) -> None:
        for doc in docs:
            self.graph.add_node(doc.title, type="document")

    def monitor_and_add(self, new_doc: Document) -> None:
        self.ingest([new_doc])
        print(f"Added {new_doc.title}")


def main() -> None:
    initial = [Document("Start", "baseline")]
    agent = UpdateAgent()
    agent.ingest(initial)
    agent.monitor_and_add(Document("New Research", "latest findings"))
    print("Documents:", [n for n in agent.graph.nodes()])


if __name__ == "__main__":
    main()
