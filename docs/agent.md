# Agent Operational Agreement

## Core Principles
- **Persistent Instructions:** Whenever an instruction is given to perform a task regularly or causally, it must be documented here in `agent.md`.
- **Documentation Maintenance:** I must actively manage the curation of all files under `docs/` and ensure all documentation is kept up-to-date, including accurately reflecting the Git repository status and tracking current project progress.
- **Commit Protocol:** I must perform a Git commit at the close of every successful task. I will await user confirmation of task completion before finalizing the commit.

## Prime Directive: Interaction Protocol
- **Questions:** Any prompt containing a '?' is exclusively a question. You must NOT perform any repository mutations (edits, file creations, commands that alter system state) in response to such a prompt. You must pause all ongoing work, address the question immediately, and await further explicit instructions for any action.

## Session Context Recovery
If session context is lost, I must:
1. Run `gemini --list-sessions` to view past sessions.
2. Use `gemini --resume <UUID>` or `/resume` to load relevant past context into the current session.
3. Incorporate key information from recovered sessions into project documentation.
