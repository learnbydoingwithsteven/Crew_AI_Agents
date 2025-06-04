"""Use Case 3: Idea Incubation

Analyze the knowledge graph to identify potential research ideas based on
missing connections between topics.
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

    def suggest_new_links(self) -> List[tuple[str, str]]:
        suggestions = []
        keywords = [n for n, d in self.graph.nodes(data=True) if d["type"] == "keyword"]
        for i, kw1 in enumerate(keywords):
            for kw2 in keywords[i + 1 :]:
                if not self.graph.has_edge(kw1, kw2):
                    suggestions.append((kw1, kw2))
        return suggestions


def main() -> None:
    docs = [
        Document(title="LLM Knowledge Graphs", content="using llms to build knowledge graphs"),
        Document(title="Research Agents", content="agents automate research tasks"),
    ]
    agent = KnowledgeGraphAgent()
    agent.ingest(docs)
    ideas = agent.suggest_new_links()
    print("Possible new topic links:", ideas)


if __name__ == "__main__":
    main()
