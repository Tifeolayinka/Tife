---
name: tife-audit-context
description: "Review context, technical, thread, and test documents for coherence, duplication, stale status, broken references, and missing requirement coverage. Use for audit context or documentation cleanup; code accuracy comparisons belong to sync context."
---

# Audit Context

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)
- [Review](references/review.md)

Follow the Audit section of the review reference.

1. Establish scope from the request. If omitted, start with the active feature and its linked
   documents; avoid turning a local question into an unbounded repository-wide rewrite.
2. Inspect ownership of facts, requirement and test IDs, references, terminology, status, and
   current versus planned behavior. Look for duplicate active threads for the same work.
3. Report actionable findings with affected locations, consequence, and proposed correction.
   Distinguish contradictions from unknowns. Missing tests are coverage gaps, not proof of failure.
4. For audit-only requests, write nothing. If cleanup is requested, fix unambiguous issues within
   scope and verify links afterward. Preserve undecided behavior and meaningful historical evidence.
5. Report scope, corrections if any, and remaining questions. Do not archive threads, change code,
   or restructure unrelated documentation as a side effect.
