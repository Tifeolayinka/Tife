---
name: tife-update-thread
description: "Save ongoing work state, decisions, failed attempts, blockers, and remaining tasks. Use for checkpoint, save progress, update thread, or meaningful milestones in active feature work. For a context reset also use prepare next session."
---

# Update Thread

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)

Checkpoint the current work without closing it.

1. Find its active thread. Create one from the shared outline if missing; do not duplicate the
   same work because this is a different chat. For distinct concurrent workstreams, use separate records.
2. Reconcile Current state, Remaining, and In-flight from the latest conversation and available
   evidence. Verify important volatile details when possible; mark unverified state explicitly.
3. Preserve decisions and their reasons, user corrections, failed approaches, observed results,
   and useful retry conditions. Separate optional ideas from requested or necessary work.
4. Save settled feature knowledge to existing context or create missing context using the shared
   outlines. Follow the tife-update-context workflow if that skill is installed; these bundled
   references also contain the necessary rules. Do not leave durable decisions only in chat.
5. Record actual test outcomes in the test document and link it. Route out-of-scope unfinished
   work that must persist to the local tracker; leave current tasks in Remaining.
6. Keep the thread open, refresh its timestamp, and check a fresh reader can identify the goal,
   stopping point, next action, and constraints. Report the saved record. Do not archive or commit.
