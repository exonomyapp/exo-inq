# Specification: Work Environment

## Overview
This document defines the current state and requirements of the local development environment for the RAG infrastructure project.

## Current System
- **OS:** Linux
- **Project Directory:** `/home/exocrat`
- **Temporary Directory:** `/home/exocrat/.gemini/tmp/exocrat`
- **Search Capability:** Existing `search_tool.py` (Playwright-based) - to be deprecated/replaced by RAG ingestors.

## Requirements for RAG Infrastructure
- **Docker:** Required for Qdrant containerization.
- **Python Environment:** Managed via virtual environments (`search_venv` exists).
- **Core Components:**
  - **Archon:** Knowledge ingestion and management.
  - **BMAD:** Orchestration framework.
  - **Qdrant:** Vector database for semantic storage.
