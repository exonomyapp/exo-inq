# Agent Operational Agreement

## Core Principles
- **Persistent Instructions:** Whenever an instruction is given to perform a task regularly or causally, document it here in `agent.md`.
- **Documentation Maintenance:** Actively manage the curation of all files under `docs/` and ensure all documentation is kept up-to-date, including accurately reflecting the Git repository status and tracking current project progress.
- **Commit Protocol:** Perform a Git commit at the close of every successful task. Await user confirmation of task completion before finalizing the commit.
- **Imperative Mood:** Use the imperative mood (direct commands) for all documentation instructions to ensure clarity and avoid ambiguity.
- **Verify-Before-Assume:** Never assume the technology stack, installation procedures, or configuration requirements of incoming technologies. Always interrogate the project structure, documentation, and source code to establish factual baseline before planning or execution.

## Prime Directive: Interaction Protocol
- **Questions:** Any prompt containing a '?' is exclusively a question. Do NOT perform any repository mutations (edits, file creations, commands that alter system state) in response to such a prompt. Pause all ongoing work, address the question immediately, and await further explicit instructions for any action.
- **Interview Protocol:** All technical inquiries directed at the user MUST be framed to empower an informed response.
    - Provide necessary context and educational background for technical terminology (e.g., explaining "tags" or "variants").
    - Clearly state the purpose, implications, and alternatives for any decision requiring user input.
    - If the user lacks necessary background, prioritize providing it *before* asking for a decision.

## Session Context Recovery
If session context is lost:
1. Run `gemini --list-sessions` to view past sessions.
2. Use `gemini --resume <UUID>` or `/resume` to load relevant past context into the current session.
3. Incorporate key information from recovered sessions into project documentation.

## Naming Conventions
- **Conciseness:** Prefer concise naming conventions for directories and files to maintain project clarity. For example, use `infra` instead of `infrastructure`.

## Operational Procedure
- **Workspace:** Immediately upon session startup, switch to the project directory: `cd /home/exocrat/exo-inq/`. All operations must be executed within this directory unless explicitly required otherwise.
- **Validation:** Before executing any complex or state-altering infrastructure commands, draft the procedure in a file within `docs/ops/`. Await confirmation that the command sequence is robust and permission-aware before executing it.
- **Dependency Management:** Use an `external/` directory for all third-party downloads, repositories, and build artifacts. Ensure this directory is listed in `.gitignore` to prevent it from being tracked in the repository.
- **Staging:** All git staging operations must use the command `git add .` to ensure no unstaged files are inadvertently left out of commits.
- **Search:** Always update the repository-scoped search database *immediately* before every search: `updatedb --localpaths='/home/exocrat/exo-inq' --output='/home/exocrat/exo-inq/.repo.db'`. Perform searches using: `locate -d /home/exocrat/exo-inq/.repo.db <pattern>`.
- **Memory Constraint:** Never simultaneously load more than three local SLMs. Monitor resource usage when running concurrent agent processes.

## Bootstrap Checklist (Resume State)
Upon session startup, identify project state by:
1. Reading the root `README.md` to understand project scope.
2. Following instructions in `README.md` to read `docs/README.md` for operational and organizational context.
3. Checking `git log` for the latest successful task.
4. If missing context, follow "Session Context Recovery" above.
