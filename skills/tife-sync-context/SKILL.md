---
name: tife-sync-context
description: "Compare scoped context and test documents with implementation to identify drift, missing implementation, contradictions, and uncertainty. Use for sync context or check whether docs match code. Review requests are read-only; sync requests allow evidenced documentation updates."
---

# Sync Context

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)
- [Review](references/review.md)

Follow the Sync section of the review reference.

1. Determine the requested subsystem and whether this is review-only or write mode. Identify the
   relevant documentation, source boundaries, tests, and version under inspection.
2. Read both the intended requirements and implementation without treating either as automatically
   authoritative. Follow relevant paths far enough to substantiate claims; state inspection limits.
3. Classify findings using the shared table, with locations and evidence. Trace affected test IDs.
4. In write mode, apply clear factual documentation corrections, keeping observed behavior distinct
   from agreed intent. Preserve missing requirements and flag contradictory or uncertain decisions.
   In review mode, change nothing, including timestamps.
5. Record scoped verification metadata only after actually checking that scope. Reading source
   does not mark test scenarios Passed. Report applied changes and unresolved findings separately.

Do not fix application code, erase unimplemented requirements, or promote assumptions to product
decisions as a side effect of synchronization.
