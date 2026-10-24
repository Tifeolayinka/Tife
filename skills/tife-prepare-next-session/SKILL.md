---
name: tife-prepare-next-session
description: "Save work before a fresh chat or context reset: create or update context and thread documents, preserve relevant tests, and return a short prompt referencing the thread. Also handles resuming that handoff."
---

# Prepare Next Session

Read [workflow](references/workflow.md), then use the applicable branch in
[handoff](references/handoff.md):

- **Preparing:** follow **Save before handing off**, then **Return the short prompt**, in that
  order. This creates missing context and thread documents automatically and updates existing ones.
- **Resuming:** follow **On pickup** to read the saved records, recheck volatile state, and continue
  under the current user's instructions.

When creating or restructuring a document, read its outline in [documents](references/documents.md).
When preserving test scenarios or results, read [testing](references/testing.md). These bundled
references support the full operation even when no sibling skills are installed.

**Preparation is done when:** the open thread and supporting documents are saved, links resolve,
and the record states the goal, current state, decisions, failed attempts, next action, and user
limits. Return a few-sentence prompt with the actual thread path and next instruction; detailed
context stays in the documents. On a failed save, report the failure instead of claiming durability.

Leave context clearing and opening a new chat to the user. No Git commit is required to hand off.
