# Procedure: Setup Ollama & Hybrid Orchestration

## Objective
Install Ollama, deploy the Gemma SLM, and configure Archon/BMAD for hybrid research (Local SLM + Gemini API).

## Procedure
1. **Install Ollama**:
   - Execute: `curl -fsSL https://ollama.com/install.sh | sh`
2. **Deploy Gemma**:
   - Execute: `ollama run gemma:2b` (or your preferred Gemma version)
3. **Configure Archon/BMAD**:
   - Locate Archon/BMAD config (e.g., `~/.archon/config.yaml`).
   - Configure "default" model to use Ollama endpoint (`http://localhost:11434/v1`).
   - Configure a fallback/complex agent persona to use the Gemini API (API key required).

## Verification
- Test local SLM: `curl http://localhost:11434/api/generate -d '{"model": "gemma", "prompt": "Hello"}'`
- Test bridge: Ensure Archon can trigger a local task via the configured Ollama endpoint.

## Awaiting Approval
- Review this procedure. Do you confirm these steps?
