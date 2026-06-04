# Archon & BMAD Configuration

## Objective
Connect Archon and BMAD components to the persistent Qdrant instance.

## Procedure
1. **Locate Configuration Files**:
   - For Archon: Identify `.env` or configuration files within `external/Archon`.
   - For BMAD: Identify configuration within `external/bmad`.
2. **Apply Connection Settings**:
   - Set vector database URL to: `QDRANT_URL=http://localhost:6333`
3. **Health Check**:
   - Run health check scripts:
     - Archon: `bun run health-check` (verify commands in Archon README)
     - BMAD: `npm run health-check` (verify commands in BMAD README)

## Verification
- Confirm 200 OK or equivalent from connectivity tests to Qdrant.

## Awaiting Approval
- Review this procedure. Do you confirm these steps?
