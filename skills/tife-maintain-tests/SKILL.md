---
name: tife-maintain-tests
description: "Create or update requirement-linked test scenarios and execution records. Use for test planning, results, coverage gaps, or changed behavior; documentation alone does not trigger implementation or test execution."
---

# Maintain Tests

Read [workflow](references/workflow.md) and [testing](references/testing.md), which owns the
scenario format, result states, evidence requirements, and recheck rules.

1. Read feature requirements and technical contracts. If context is missing, establish it from
   known facts using [documents](references/documents.md); leave unknown expectations open.
2. Create or update the test document. Link stable scenario IDs to requirements or contracts;
   record setup, actions, expected outcomes, and methods. Map existing automated tests where useful.
3. Execute checks when requested or necessary for authorized implementation. Otherwise record only
   available attributable evidence and leave unexecuted checks Not run. Apply the testing contract
   when recording results or invalidating confidence after changes.
4. Link failures and outstanding checks from the active thread, if one exists.

**Done when:** scenarios trace to their intended behavior, results distinguish plans from actual
runs, and evidence identifies the tested state. Report what was planned, executed, and left
unverified, including blocked checks.
