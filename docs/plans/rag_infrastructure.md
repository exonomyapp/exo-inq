# RAG Research Infrastructure

## Overview
Shift research approach from unreliable web scraping to a structured, local RAG system, maintaining a persistent "shadow index" of relevant information.

## Architectural Components
- **Qdrant:** Persistent vector storage for our semantic shadow index. (Active service in `/infra/`)
- **Archon:** Knowledge management and ingestion hub. (Installed in `/external/`)
- **BMAD:** Orchestration framework for autonomous research tasks. (Installed in `/external/`)
## Tiered SLM Intelligence
  - **Primary Researcher Agent:** `gemma4:12b` (4-bit quantized - Q4_K_M)
  - **Task Orchestrator/Subagent:** `gemma4:e4b` (4-bit quantized - Q4_K_M)


## Roadmap
| Phase | Task | Details | Status |
| :--- | :--- | :--- | :--- |
| **1** | **Infrastructure** | Deploy Qdrant container. | Completed |
| **2** | **Component Setup** | Install Archon & BMAD dependencies. | Completed |
| **3** | **Model Setup** | Deploy Tiered SLMs (Gemma 4 family). | Completed |
| **4** | **Configuration** | Connect Archon/BMAD to Qdrant/Ollama. | Completed |
| **5** | **Ingestion Pipeline** | Develop agentic workflow to crawl/ingest data. | In Progress |

## Tracking
- **Status:** Phase 5 (Ingestion Pipeline)
- **Next Step:** Implement data ingestion pipeline for shadow index.
