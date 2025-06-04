"""Use Case 10: Interdisciplinary Connection Finder

Search the knowledge graph for links between distinct research fields.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List
import networkx as nx

@dataclass
class Document:
    title: str
    content: str
    field: str

class ConnectionAgent:
    def __init__(self) -> None:
        self.graph = nx.Graph()

    def ingest(self, docs: Iterable[Document]) -> None:
        for doc in docs:
            self.graph.add_node(doc.title, field=doc.field)
            self.graph.add_node(doc.field, type="field")
            self.graph.add_edge(doc.title, doc.field)

    def cross_field_links(self) -> List[tuple[str, str]]:
        fields = [n for n, d in self.graph.nodes(data=True) if d.get("type") == "field"]
        links = []
        for doc1, data1 in self.graph.nodes(data=True):
            if data1.get("type") == "field":
                continue
            for doc2, data2 in self.graph.nodes(data=True):
                if data2.get("type") == "field" or doc1 == doc2:
                    continue
                if data1["field"] != data2["field"]:
                    links.append((doc1, doc2))
        return links


def main() -> None:
    docs = [
        Document("Graph Mining", "techniques", "Computer Science"),
        Document("Protein Analysis", "biology", "Biology"),
    ]
    agent = ConnectionAgent()
    agent.ingest(docs)
    print("Cross-field document pairs:", agent.cross_field_links())


if __name__ == "__main__":
    main()
