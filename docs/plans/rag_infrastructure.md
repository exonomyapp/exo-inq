# RAG Research Infrastructure

## Overview
As determined in our sessions, shift our research approach from unreliable web scraping to a structured, local RAG system to maintain a persistent "shadow index" of relevant information.

## Architectural Components
- **Qdrant:** Persistent vector storage for our semantic shadow index. (Active service in `/infra/`)
- **Archon:** Knowledge management and ingestion hub. (Installed in `/external/`)
- **BMAD:** Orchestration framework for autonomous research tasks. (Installed in `/external/`)

## Roadmap
| Phase | Task | Details | Status |
| :--- | :--- | :--- | :--- |
| **1** | **Infrastructure** | Deploy Qdrant container. | Completed |
| **2** | **Component Setup** | Install Archon & BMAD dependencies. | In Progress |
| **3** | **Configuration** | Connect Archon/BMAD to Qdrant (http://localhost:6333). | Pending |
| **4** | **Ingestion Pipeline** | Develop agentic workflow to crawl/ingest data. | Pending |

## Tracking
- **Status:** Phase 2 (Component Setup)
- **Next Step:** Configure Archon/BMAD connection to Qdrant and verify health.
