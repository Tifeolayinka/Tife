---
name: tife-end-thread
description: "Close and archive an explicitly completed, cancelled, or superseded line of work after saving durable context, test status, and unfinished items. Use for end or close thread; leaving a chat or clearing context instead uses prepare next session."
---

# End Thread

Read the shared workflow before acting. Read the other references relevant to the operation.

- [Workflow](references/workflow.md)
- [Documents](references/documents.md)
- [Testing](references/testing.md)
- [Closing](references/closing.md)

Follow the ordered closing workflow in the closing reference.

1. Establish explicit closure intent and the target work. A farewell is not a request to archive.
2. Reconcile the final outcome and actual verification status without overstating completion.
3. Create or update durable context and relevant test records before moving the thread.
4. Route unfinished items and verify their destinations. Preserve explicit cancellations.
5. Only after those saves succeed, close and archive the thread; preserve historical content,
   rebase relative links, and repair inbound references or indexes.
6. Report the archive path, outcome, test limitations, and where unfinished work now lives.

If a required save or routing step fails, leave the thread active. Do not overwrite an archive,
delete unresolved tasks, close unrelated work, or perform unrequested Git or deployment actions.
