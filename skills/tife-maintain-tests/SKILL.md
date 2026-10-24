---
name: tife-maintain-tests
description: "Create or update a feature test plan and execution record linked to requirements. Use when planning checks, recording test results, changing feature behavior, or identifying coverage gaps. Run tests when requested or necessary for authorized implementation."
---

# Maintain Tests

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Testing](references/testing.md)
- [Documents](references/documents.md)

Maintain a useful test plan and an honest record of verification.

1. Read the relevant feature requirements and technical contracts. Create minimal context first
   if missing, using established facts; do not invent expected behavior from a desired test result.
2. Find the existing test document or create one. Use stable scenario IDs and requirement links.
   Cover representative normal flows and relevant permissions, boundaries, failures, and recovery.
3. Record reproducible setup, action, expectation, and method. Map existing automated tests when
   possible. Label exploratory or operational checks by their actual purpose.
4. If the task includes execution, run appropriate authorized checks and capture their evidence,
   environment, time, and tested version. If only planning or documenting, leave checks Not run.
5. Add execution records without erasing important failures or prior evidence. Mark affected old
   passes Needs recheck after meaningful behavior changes. Explain blocked checks.
6. Link failures and remaining checks from the active thread. Report what was planned, what
   actually ran, what passed or failed, and what remains unverified.
