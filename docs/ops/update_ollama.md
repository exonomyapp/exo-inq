# Procedure: Update Ollama

## Objective
Update the Ollama binary to the latest version to support Gemma 4 manifest schemas.

## Procedure
1.  **Run the official installation script:**
    `curl -fsSL https://ollama.com/install.sh | sh`

2.  **Verify the new version:**
    `ollama --version`

3.  **Resume SLM model update (from `docs/ops/update_slm_models.md`):**
    `ollama pull gemma4:12b`
    `ollama pull gemma4:e4b`
