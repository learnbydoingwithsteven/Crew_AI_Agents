"""Use Case 2: Accelerated Querying

Illustrates how a CrewAI agent might query the knowledge graph built from
Ollama-powered document ingestion. The agent returns titles of documents linked
to a given keyword. Networkx is used instead of a full graph database to keep
the example lightweight.
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

    def query(self, keyword: str) -> List[str]:
        if keyword not in self.graph:
            return []
        return [n for n in self.graph.neighbors(keyword) if self.graph.nodes[n]["type"] == "document"]


def main() -> None:
    docs = [
        Document(title="LLM Knowledge Graphs", content="using llms to build knowledge graphs"),
        Document(title="Research Agents", content="agents automate research tasks"),
    ]
    agent = KnowledgeGraphAgent()
    agent.ingest(docs)
    print("Documents related to 'research':", agent.query("research"))


if __name__ == "__main__":
    main()
