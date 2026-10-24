# Document ownership and formats

Use these outlines as starting points, adapting to existing project conventions. Omit irrelevant
sections rather than padding them. Placeholder text is a drafting aid and must not survive in
documents produced for real work.

## Feature context

```markdown
---
id: feature-slug
status: draft
updated: <actual timestamp with offset>
---
# Feature name

## Purpose and scope
Who this serves, the problem, included behavior, and explicit exclusions.

## Requirements
| ID | Behavior / acceptance criterion | State | Basis |
|---|---|---|---|
| FEATURE-R1 | Given ..., when ..., then ... | Agreed, not verified | User decision, date |

## Behavior and edge cases
States, permissions, boundaries, failures, recovery, and expected outcomes.
Unsettled expected outcomes are open questions, not assumed requirements.

## Decisions
| Decision | Reason | Date / source |
|---|---|---|

## Open questions and known gaps

## Related documents
Relative links to technical context, tests, and relevant work records.

## Change history
Dated substantive changes and why they happened.
```

Requirement IDs stay stable. Mark superseded criteria as retired and point to their replacement;
do not renumber existing criteria or reuse IDs. Distinguish agreement from implementation and
verification. A useful state vocabulary is Proposed, Agreed, Observed in code, Verified, Retired.
An observed behavior is not automatically approved intended behavior.

## Technical context

```markdown
# Feature name — technical context
Updated: <actual timestamp with offset>
Feature context: <relative link>

## System role and boundaries
## Architecture and dependencies
## Data relationships and constraints
## Interfaces and contracts
## Design decisions and rationale
## Failure modes and recovery
## Implementation pointers
Only a few useful, verified entry points and operating commands.
## Planned changes and unresolved questions
## Change history
```

Explain what shapes implementation choices. Label present and target designs explicitly; remove
obsolete target framing only when implementation is established. A small feature can include this
information in its feature context instead of creating a second file.

## Thread

```markdown
---
id: work-slug
status: open
started: <actual timestamp with offset>
updated: <actual timestamp with offset>
---
# Work title

## Goal and scope
The user's request, constraints, and what finished means.

## Context documents
Relative links with a short explanation of why each matters.

## Current state
What is complete, what is incomplete, and the precise stopping point.

## Decisions and corrections
Decision, reason, source; include rejected alternatives where useful.

## Attempts and lessons
Attempt, observed outcome, evidence, and conditions under which retrying makes sense.

## Remaining
Requested work, necessary supporting tasks, and optional suggestions clearly distinguished.
State the next action, stop point, and any explicit user limits or approvals.

## In-flight
Running processes, uncommitted files, partially completed operations; verify again on pickup.

## Verification
Link to tests and summarize actual results and outstanding checks.

## Work history
Dated meaningful milestones, without repeating the entire conversation.
```

An archived thread is a closed historical record. To continue completed work, create a new active
thread that links back; do not silently reopen history. If it was archived by mistake, ask before
changing its lifecycle state. Preserve links when moving or renaming files.

## Open issue

Use the project's tracker, or a concise entry in `docs/threads/OPEN-ISSUES.md`:
ID; summary; status; origin thread link; why it matters; next action or owner when known.
Do not invent an assignee or create external issues without authorization.

## Teammate handoff

```markdown
# Handoff for <recipient>

## Open
- [ ] <stable ID>: Task or question
  - Expected outcome:
  - Context: <relative links>
  - Blockers / dependencies:
  - Updated: <timestamp>

## Completed
Closed items with outcome, completion date, and evidence if available.
```

## Context index

When useful, `docs/context/INDEX.md` lists each feature, purpose, feature context, technical
context, and test document. It is a navigation map, not another copy of requirements or status.
