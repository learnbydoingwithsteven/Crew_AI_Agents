"""Use Case 8: Data Integration with Ontologies

Demonstrates merging terms from multiple datasets into a unified ontology. A
CrewAI agent paired with an Ollama model could handle entity resolution and
ontology alignment. Here we simply connect dataset names with shared terms in a
networkx graph.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
import networkx as nx

@dataclass
class DataEntry:
    id: str
    term: str
    dataset: str

class OntologyAgent:
    def __init__(self) -> None:
        self.graph = nx.Graph()

    def ingest(self, entries: Iterable[DataEntry]) -> None:
        for entry in entries:
            self.graph.add_node(entry.term, dataset=entry.dataset)
            self.graph.add_node(entry.dataset, type="dataset")
            self.graph.add_edge(entry.dataset, entry.term)


def main() -> None:
    entries = [
        DataEntry("1", "protein", "bio"),
        DataEntry("2", "protein", "chem"),
    ]
    agent = OntologyAgent()
    agent.ingest(entries)
    print("Nodes:", list(agent.graph.nodes(data=True)))


if __name__ == "__main__":
    main()
