"""Use Case 7: Collaboration Network Mapping

Highlights how a CrewAI agent might build a graph of researchers and
organizations. With Ollama providing the language model, the agent could suggest
new partnerships based on shared topics. This mock-up adds nodes and edges to a
simple networkx graph.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Tuple, List
import networkx as nx

@dataclass
class Collaboration:
    researcher: str
    institution: str

class CollaborationAgent:
    def __init__(self) -> None:
        self.graph = nx.Graph()

    def ingest(self, records: Iterable[Collaboration]) -> None:
        for rec in records:
            self.graph.add_node(rec.researcher, type="researcher")
            self.graph.add_node(rec.institution, type="institution")
            self.graph.add_edge(rec.researcher, rec.institution)

    def find_institutions(self, researcher: str) -> List[str]:
        if researcher not in self.graph:
            return []
        return [n for n in self.graph.neighbors(researcher) if self.graph.nodes[n]["type"] == "institution"]


def main() -> None:
    records = [
        Collaboration("Alice", "University A"),
        Collaboration("Bob", "University B"),
        Collaboration("Alice", "Research Lab X"),
    ]
    agent = CollaborationAgent()
    agent.ingest(records)
    print("Institutions for Alice:", agent.find_institutions("Alice"))


if __name__ == "__main__":
    main()
