# Agent Operational Agreement

## Core Principles
- **Persistent Instructions:** Whenever an instruction is given to perform a task regularly or causally, it must be documented here in `agent.md`.
- **Documentation Maintenance:** I must actively manage the curation of all files under `docs/` and ensure all documentation is kept up-to-date, including accurately reflecting the Git repository status and tracking current project progress.

## Current Known Issues
- **Repository Creation Failure:** Attempt to create 'exo-inq' via `gh` failed due to insufficient token permissions.
  - **Fix:** Fine-grained PAT requires "Read and write" access for both **Administration** and **Code** (Contents) repository permissions. Update settings on GitHub and re-run.
