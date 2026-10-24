---
name: tife-create-thread
description: "Start a work record for a feature, fix, investigation, or planning task. Use when starting a thread or new substantial feature work; reuse an active thread for the same work. This creates project documents, not an application chat."
---

# Create Thread

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)

Establish one durable work record for the requested line of work.

1. Discover existing records using the shared workflow. Identify the user's goal and current
   stage: discussion, implementation, or investigation. Reuse an active thread for the same work.
2. If creating, choose a stable work ID and write the thread outline with the real request,
   constraints, completion criteria, known state, and first next step. Don't infer permission
   to implement from permission to document or plan.
3. Link the relevant feature context and technical context. Create missing context from facts
   already established, using the context outline. For an existing codebase, inspect enough source
   to identify the boundary; label observations separately from intended requirements.
4. For substantive feature work, establish or link a test document using known acceptance criteria.
   Unknown expected behavior remains a question. Planning-only threads need no invented tests.
5. Check links and report the thread path and any blocking questions. Creating a new app chat,
   branch, or worktree is not part of this skill.
