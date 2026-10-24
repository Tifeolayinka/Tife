---
name: tife-update-teammate-handoff
description: "Create or maintain a project handoff document for a named teammate: tasks, questions, decisions, blockers, and completion notes. Use for teammate handoffs, not the short AI continuation prompt produced by prepare next session. This skill does not send messages."
---

# Update Teammate Handoff

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)

Maintain a teammate's durable task and information handoff.

1. Identify the recipient, requested content, and project. Ask if the recipient or assignment is
   materially ambiguous. Locate their existing handoff; create one when the request needs it.
2. Add or update an item with a stable ID, expected outcome, relevant context and thread links,
   blockers, and a real timestamp. Preserve existing ownership and conventions.
3. Separate a task from a question or informational decision. Do not invent a deadline, assignee,
   commitment, or permission beyond what the user established.
4. When closing an item, record the outcome and evidence where available; retain completed items
   or use the project's existing archival convention. Do not delete open items.
5. Verify links and report the updated document and items. Do not send email, chat, invitations,
   or external notifications. If the user separately requested sending, handle it as a separate
   authorized action with its own verified destination.
