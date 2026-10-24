---
name: tife-update-context
description: "Create or update feature or subject context from established conversation facts and decisions. Use for update context, document this feature, record a decision, or missing context during session preparation. Use sync context for code-driven comparison."
---

# Update Context

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)

Persist the knowledge established in the current work.

1. Locate the relevant document; update it if present, create it automatically if absent. Match
   scope and meaning, not just the exact filename. Ask only when the destination is materially ambiguous.
2. Gather established requirements, decisions and reasons, corrections, observed behavior, and
   unresolved questions. Use source pointers where helpful. On initial codebase documentation,
   inspect scoped source and label the baseline as observed, not approved product intent.
3. Write into the appropriate sections using the feature outline, or a natural outline for
   non-feature knowledge. Separate technical context when design detail warrants it.
4. Preserve requirement IDs. Retire superseded requirements with a reason and replacement link.
   Review affected sections for contradictions. Do not silently settle disagreements.
5. When behavior changes, update affected scenarios and mark prior results Needs recheck while
   retaining evidence. Do not invent executions. Link the test document.
6. Refresh update metadata and substantive change history; update existing indexes and links.
   Report saved paths and open questions. Do not run a full code-sync merely to save a decision.
