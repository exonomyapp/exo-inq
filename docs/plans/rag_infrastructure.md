# Local RAG Research Infrastructure

## Overview
As determined in our sessions, we are shifting our research approach from unreliable web scraping to a structured, local RAG system to maintain a persistent "shadow index" of relevant information.

## Architectural Components
- **Archon:** Knowledge Hub / MCP Server for intelligent content ingestion.
- **BMAD:** Agentic workflow orchestrator to manage research tasks.
- **Qdrant:** Vector database acting as our local semantic search engine.

## Implementation Path
1. **Infrastructure Directory:** Establish `/infrastructure/` to centralize service configurations (e.g., docker-compose for Qdrant).
2. **Component Setup:**
    - Initialize Qdrant via Docker.
    - Setup Archon and BMAD environments.
3. **Integration:** Connect Archon to Qdrant to start populating our shadow index.

## Tracking
- **Status:** Phase 1 (Setup)
- **Next Step:** Initialize infrastructure directory and Qdrant container.
