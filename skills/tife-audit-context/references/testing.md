# Test document contract

Keep requirements in feature context and test execution in the test document. Use stable test IDs
and link each acceptance scenario to stable requirement IDs. Exploratory checks may be marked as
exploratory; operational checks may cite a technical contract. Do not fabricate a product requirement
just to give a useful existing test an ID.

```markdown
# Feature name — test plan and results
Feature context: <relative link>
Updated: <actual timestamp with offset>

## Scope and prerequisites
Environment, test data, dependencies, and relevant limitations. No inline secrets.

## Scenarios
| ID | Requirement / contract | Setup | Action | Expected result | Method |
|---|---|---|---|---|---|
| FEATURE-T1 | FEATURE-R1 | ... | ... | ... | Automated / manual |

## Execution instructions
Verified commands or reproducible manual steps. Identify instructions that still need validation.

## Results
| Test ID | Result | When | Tested version / environment | Evidence |
|---|---|---|---|---|
| FEATURE-T1 | Not run | — | — | — |

## Gaps and follow-up
Missing coverage, blocked checks, failures, and affected work records.
```

Results: Not run, Passed, Failed, Blocked, Needs recheck. Distinguish a planned check from a run.
Record a pass only from an observed execution or supplied attributable evidence, never by reading
code or writing an automated test. Preserve meaningful previous execution records when adding a
new result. A changed requirement, relevant implementation, or environment invalidates confidence
in affected old results: retain the old evidence and mark their current applicability Needs recheck.
Unrelated changes need not invalidate all checks.

Include ordinary flows, roles and permissions, boundaries, and realistic failure/recovery cases.
Add concurrency, replay, or partial failure scenarios when the feature actually warrants them.
Use exact expected outcomes established by requirements. Unknown outcomes remain open questions;
do not invent product behavior while writing tests. Avoid exhaustive speculative combinations.

When running checks, use the project's existing test tools and authorized environment. Record the
command, outcome, revision (or dirty working-tree description), and useful evidence. Do not perform
destructive or production checks solely to populate a document. A blocked test is a valid result.
