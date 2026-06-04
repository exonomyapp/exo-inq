# Procedure: Setup Ollama & Hybrid Orchestration

## Objective
Install Ollama, deploy the Gemma 2:9B and Gemma 4:E4B SLMs, and configure Archon/BMAD for hybrid research (Local SLM + Gemini API).

## Procedure
1. **Install Ollama**:
   - Execute: `curl -fsSL https://ollama.com/install.sh | sh`
2. **Deploy SLMs**:
   - Primary Researcher: `ollama run gemma2:9b`
   - Task Orchestrator: `ollama run gemma4:e4b`
3. **Configure Archon/BMAD**:
   - Locate Archon/BMAD config.
   - Configure to use Ollama endpoint (`http://localhost:11434/v1`).
   - Configure fallback persona to use Gemini API.

## Verification
- Confirm models: `ollama list`
- Test connectivity: `curl http://localhost:11434/api/tags`
