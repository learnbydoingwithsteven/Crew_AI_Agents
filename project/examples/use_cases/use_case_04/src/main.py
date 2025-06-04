"""Use Case 4: Automated Literature Review

Shows how an agent could produce concise summaries of papers stored in the
knowledge graph. Integrating CrewAI with Ollama would allow the agent to
generate natural language abstracts; here we simply return text snippets from
each document for demonstration.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Dict
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
            self.graph.add_node(doc.title, type="document", content=doc.content)

    def summarize(self) -> Dict[str, str]:
        return {n: self.graph.nodes[n]["content"][:50] for n, d in self.graph.nodes(data=True) if d["type"] == "document"}


def main() -> None:
    docs = [
        Document(title="LLM Knowledge Graphs", content="using llms to build knowledge graphs"),
        Document(title="Research Agents", content="agents automate research tasks"),
    ]
    agent = KnowledgeGraphAgent()
    agent.ingest(docs)
    summaries = agent.summarize()
    for title, snippet in summaries.items():
        print(f"{title}: {snippet}")


if __name__ == "__main__":
    main()
