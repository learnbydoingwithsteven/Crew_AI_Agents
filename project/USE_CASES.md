# CrewAI Research Use Cases with Ollama

The following use cases demonstrate how `crewai` agents running with a local model via **Ollama** can accelerate research workflows. A central theme is leveraging **knowledge graphs** to organize information and employing agents to explore new ideas and manage tasks.

1. **Knowledge Graph Creation**
   - Parse research papers, web articles, or datasets using the local model and ingest key entities (authors, topics, methods) into a knowledge graph.
   - Agents continuously expand the graph with new data sources, ensuring up-to-date context for research questions.
   - Example: `examples/use_cases/use_case_01/src/main.py`

2. **Accelerated Querying**
   - Use the knowledge graph to answer complex research queries rapidly.
   - Agents traverse the graph to surface relevant papers, datasets, or relationships, providing short summaries.
   - Example: `examples/use_cases/use_case_02/src/main.py`

3. **Idea Incubation**
   - Deploy a brainstorming agent that examines the graph to discover gaps or unexplored connections.
   - The agent suggests new project ideas or hypotheses based on relationships found within the knowledge graph.
   - Example: `examples/use_cases/use_case_03/src/main.py`

4. **Automated Literature Review**
   - Agents scan the graph for recent publications and generate concise literature reviews.
   - By analyzing citation networks, they highlight influential works and trends.
   - Example: `examples/use_cases/use_case_04/src/main.py`

5. **Experiment Design Assistance**
   - Agents analyze existing methods stored in the knowledge graph to recommend experiment designs or analytical approaches.
   - This includes identifying standard protocols, datasets, or software libraries relevant to the research topic.
   - Example: `examples/use_cases/use_case_05/src/main.py`

6. **Grant Proposal Support**
   - Agents gather background research from the knowledge graph to craft persuasive grant proposals.
   - They provide references and evidence of research needs directly from the graph's curated information.
   - Example: `examples/use_cases/use_case_06/src/main.py`

7. **Collaboration Network Mapping**
   - Agents map relationships between researchers, institutions, and projects.
   - This helps identify potential collaborators or experts in a specific domain.
   - Example: `examples/use_cases/use_case_07/src/main.py`

8. **Data Integration with Ontologies**
   - Agents merge data from various sources into the knowledge graph using domain-specific ontologies.
   - This keeps terminology consistent and makes cross-dataset queries more effective.
   - Example: `examples/use_cases/use_case_08/src/main.py`

9. **Real-time Research Updates**
   - Monitoring agents watch for new publications or datasets, ingesting them into the graph automatically.
   - Researchers receive alerts when new, relevant work appears.
   - Example: `examples/use_cases/use_case_09/src/main.py`

10. **Interdisciplinary Connection Finder**
    - Agents explore the knowledge graph to find links between seemingly unrelated fields.
    - This can reveal opportunities for novel collaborations or cross-domain insights.
    - Example: `examples/use_cases/use_case_10/src/main.py`

These use cases illustrate how combining `crewai` agents with a knowledge graph—powered by a local model through Ollama—can streamline research tasks, from idea generation to ongoing literature monitoring.
