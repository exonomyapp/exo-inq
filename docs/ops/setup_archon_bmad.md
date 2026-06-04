# Procedure: Archon & BMAD Component Setup (Corrected)

## Objective
Install and configure the Archon Knowledge Hub and BMAD orchestration framework.

## Prerequisites
- Docker (running Qdrant)
- Node.js 20+
- Bun (https://bun.sh/)

## Procedure
1. **Archon Setup**:
   - Navigate: `cd external/Archon`
   - Install dependencies: `bun install`
2. **BMAD Setup**:
   - Navigate: `cd external/bmad`
   - Install dependencies: `npm install`
3. **Configuration**:
   - Configure environment variables to point to the Qdrant instance (http://localhost:6333).

## Verification
- Test connection: Run the initial health check script for Archon/BMAD.

## Awaiting Approval
- Review this corrected procedure. Do you confirm these steps?
