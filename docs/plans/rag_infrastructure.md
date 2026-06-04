# RAG Research Infrastructure

## Overview
Shift research approach from unreliable web scraping to a structured, local RAG system, maintaining a persistent "shadow index" of relevant information.

## Architectural Components
- **Qdrant:** Persistent vector storage for our semantic shadow index. (Active service in `/infra/`)
- **Archon:** Knowledge management and ingestion hub. (Installed in `/external/`)
- **BMAD:** Orchestration framework for autonomous research tasks. (Installed in `/external/`)
- **Tiered SLM Intelligence:**
  - **Primary Researcher Agent:** `gemma2:9b` (High reasoning capability)
  - **Task Orchestrator/Subagent:** `gemma4:e4b` (Edge-optimized efficiency)

## Roadmap
| Phase | Task | Details | Status |
| :--- | :--- | :--- | :--- |
| **1** | **Infrastructure** | Deploy Qdrant container. | Completed |
| **2** | **Component Setup** | Install Archon & BMAD dependencies. | Completed |
| **3** | **Model Setup** | Deploy Tiered SLMs (Gemma2:9B/E4B). | In Progress |
| **4** | **Configuration** | Connect Archon/BMAD to Qdrant/Ollama. | Pending |
| **5** | **Ingestion Pipeline** | Develop agentic workflow to crawl/ingest data. | Pending |

## Tracking
- **Status:** Phase 3 (Model Setup)
- **Next Step:** Download and configure Gemma2:9B and Gemma4:E4B.
