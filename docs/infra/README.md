# Infrastructure: Local RAG Mission

## Mission
Our mission is to establish a deterministic, autonomous, and private research environment. We are moving away from unreliable, transient web search scraping in favor of building a permanent, local "shadow index."

## Purpose
This infrastructure allows us to:
1. **Control:** Own our data ingestion pipeline and index.
2. **Persistence:** Retain knowledge that search engines may opt not to index or that may become unreachable over time.
3. **Intelligence:** Empower an agentic system (BMAD) to navigate our local knowledge graph, performing structured research that builds relevance over time.

## Components
- **Qdrant:** Persistent vector storage for our semantic shadow index.
- **Archon:** Knowledge management and ingestion hub.
- **BMAD:** Orchestration framework for autonomous research tasks.
- **Local Model Registry:** Managed via `~/.pi/agent/models.json` for connectivity between orchestrators and local Ollama inference service.

## Verified Model Storage
Verified GGUF models are maintained in `/external/models/`. Currently deployed:
- `gemma-4-E2B-it-Q4_K_M-3GB.gguf`: Verified 3.11 GB E2B model.
