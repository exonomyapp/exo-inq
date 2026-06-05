# Tool Procedure: aria2c

## Purpose
`aria2c` is the authorized, persistent tool for reliable, high-performance, and resumable downloads of large third-party artifacts (e.g., model weights, datasets) into the `/external/` directory.

## Best Practices
- **Resumption:** Always use `aria2c` for large file downloads to leverage its built-in resumption capabilities.
- **Parallelization:** Use the `-x` flag (e.g., `aria2c -x 4`) to parallelize downloads for increased efficiency.
- **Location:** All downloads must be saved to `/home/exocrat/exo-inq/external/`.
- **Transparency:** When executing, run the command clearly and inform the user of the target location and expected outcome.
