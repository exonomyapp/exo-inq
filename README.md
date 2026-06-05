# Exo-Inq: Knowledge Management & Research Infrastructure

## Overview
Exo-Inq is the foundational repository for our autonomous knowledge management and RAG-based research infrastructure. It orchestrates local-first AI agents, persistent vector storage, and autonomous agents to maintain a "shadow index" of research data.

## Documentation
- **[Agent Operational Agreement (`agent.md`)](agent.md):** The core principles, prime directive, and operational procedures for agent interaction. *Must be read first.*
- **[Documentation Overview (`docs/README.md`)](docs/README.md):** Organizational guidelines and structure of this repository's comprehensive documentation.

## Core Components
- **Orchestration:** [BMAD](/external/)
- **Ingestion/Hub:** [Archon](/external/)
- **Vector Storage:** Qdrant (deployed via `/infra/`)
- **Intelligence:** Gemma 4 (Tiered SLMs via Ollama)

## Getting Started
1. Review `agent.md` to understand operational mandates.
2. Review `docs/README.md` for project structure.
3. Consult `docs/plans/rag_infrastructure.md` for current deployment status and architectural roadmap.
