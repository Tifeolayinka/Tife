---
name: tife-prepare-next-session
description: "Save current conversation knowledge and working state before a fresh chat or context reset. Automatically create missing context and thread documents, update existing ones, preserve tests, and return a short handoff referencing the saved thread."
---

# Prepare Next Session

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)
- [Handoff](references/handoff.md)

Complete the save-before-handoff workflow in the handoff reference.

1. Review available conversation context and discover the active records for this work.
2. Update the relevant context document; if absent, create it automatically. Preserve established
   knowledge even when this is planning rather than coding. Label unknowns instead of inventing facts.
3. Update or create the same work's thread, preserving the user's request, present state, decisions,
   failed attempts, constraints, next action, and stop point. Link supporting documents.
4. Save relevant test scenarios and actual verification results using the testing contract.
5. Verify the saved documents and links. Keep the work open. Do not require a commit for a valid
   checkpoint; record uncommitted state so the next session can inspect it.
6. Return a short ready-to-paste prompt using the actual thread path and a continuation instruction
   grounded in the current work. Detailed context belongs in the documents, not the prompt.

If the collection's other skills are installed, use their relevant workflows for these writes;
otherwise the bundled references provide the complete document contracts. Do not omit saving
because a sibling skill is unavailable. Do not create another app chat or clear context yourself.

When invoked to resume a supplied handoff, follow the On pickup section of the handoff reference.
