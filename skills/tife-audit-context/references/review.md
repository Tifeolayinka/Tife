# Context review

## Sync: compare documents with implementation

Determine the requested subsystem and whether the request is review-only or a sync that permits
documentation updates. Identify the source boundaries and version under inspection.

Read the scoped feature context, technical context, referenced tests, relevant source, and
available execution evidence. For broad projects, prioritize affected subsystems and report the
scope actually inspected. Do not claim whole-project verification after sampling a few files.

| Finding | Meaning | Response |
|---|---|---|
| Undocumented behavior | Code contains behavior the docs omit | Describe it as observed; do not assume it is intended |
| Missing implementation | An agreed requirement is absent from code | Flag the gap; preserve the requirement |
| Contradiction | Sources disagree | Show both sides and ask only if resolving it is necessary |
| Insufficient evidence | Cannot establish the claim | Mark uncertainty and identify what would settle it |
| Test mismatch | Scenario or recorded confidence no longer fits | Propose scenario correction or Needs recheck |

Review-only requests write nothing, including timestamps. A request to sync or update docs permits
clear, evidence-backed documentation corrections; it does not permit new product decisions, code
changes, or silent removal of requirements. When no document exists, report the gap in review mode;
in write mode create a clearly labelled baseline with observed behavior separated from intended
requirements. Use the context writing rules.

For every finding include location, documented claim, observed evidence, classification, and next
action. If writing, list applied changes separately from unresolved findings. Record verification
scope, time, and code revision independently of last edit time. Reading code never proves a test passed.

## Audit: inspect document coherence

Use the requested scope; when omitted, start with the active feature and linked documents.

Check document ownership, duplicate active threads for the same work, contradictions, terminology,
stable IDs, duplicate requirements, broken links, unlabelled planned behavior, missing test
scenarios, and stale thread status. Separate firm findings from questions. A technical pointer is useful when it helps navigation; flag code mirrors
and distracting detail rather than banning file paths.

When a user asks for an audit, return findings by default. When they ask to fix or clean up, apply
unambiguous corrections within scope and preserve unresolved decisions. No unrelated code edits,
bulk restructuring, lifecycle changes, or changes to the shared skill collection.

For each audit finding, give the affected location, consequence, and proposed correction. Missing
test coverage is not proof of a failing implementation. Report the scope, any applied corrections,
and remaining questions; verify links after cleanup.
