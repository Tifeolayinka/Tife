---
name: tife-update-context
description: "Create or update feature or subject documentation from established conversation facts and decisions. Use to record requirements, rationale, or corrections. Code-driven drift checks belong to sync-context."
---

# Update Context

Read [workflow](references/workflow.md), then the feature or technical outline in
[documents](references/documents.md) for the kind of context being written.

1. Locate the relevant document and update it, or create it automatically if missing. Gather
   established requirements, decisions and reasons, corrections, observations, and open questions.
   For a new codebase baseline, inspect scoped source and label what was actually observed.
2. Integrate information into the matching sections. Use a natural outline for non-feature subjects;
   separate technical context when warranted. Apply the document reference's stable-ID rules and
   reconcile affected statements across the document. Record substantive edits in its change history
   and flag unresolved disagreements.
3. If behavior changes, read [testing](references/testing.md), update affected scenarios, and
   mark affected prior results Needs recheck while preserving their evidence.

**Done when:** the saved document reflects established knowledge, changed requirements and tests
agree, and unresolved questions remain explicit. Report paths and gaps. Saving a conversation
decision does not require a full code-sync.
