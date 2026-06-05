# Procedure: SLM Model Update

## Objective
Deploy verified Gemma 4 family models (`12b` and `e4b`).

## Procedure
1.  **Download verified GGUF models:**
    Use `aria2c` to download verified GGUF files to `/external/models/`. Example:
    `aria2c -x 4 <huggingface_url>`

2.  **Verify file integrity:**
    Compare file SHA256 checksums against verified repository hashes:
    `sha256sum <model_file>`
