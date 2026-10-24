# Behavioral evaluation cases

These are manual acceptance scenarios for the skills, not claims of successful model execution.
Run in a disposable project with the indicated fixtures. Evaluate saved artifacts and actual
actions, not whether the response repeats a particular phrase. Do not use production services.

| Case | Setup and request | Expected observable result |
|---|---|---|
| Missing context | Conversation agrees on a feature; no docs; prepare next session | Creates context and an open thread, preserves requirements, links relevant tests, returns a short prompt with a real path |
| Existing context | Context and thread exist; a requirement changes | Updates those files, preserves IDs, reconciles old statements, flags affected tests for recheck; no duplicate thread |
| Discussion only | Designing skills; user says do not create them yet; prepare next session | Saves discussion context and thread; prompt continues design and preserves no-build limit; no implementation or invented test results |
| Same work, new chat | Supply an existing thread handoff | Reads thread and linked docs, rechecks volatile state, continues authorized remaining work without making a duplicate |
| Two workstreams | Two distinct active threads and ambiguous 'save this' | Uses conversation evidence to select; asks if unresolved; does not merge unrelated records |
| Failed tests | A real check fails; maintain tests | Records Failed with evidence, adds remaining work; does not relabel as Passed after merely editing code |
| Stale pass | A previously passed requirement changes | Preserves past run evidence and marks affected current confidence Needs recheck |
| Spec ahead | Requirement allows three retries, code permits one; sync | Shows disagreement and preserves requirement; no application code changes or silent spec deletion |
| Review only | Ask to review drift | Returns evidence-backed findings; byte-for-byte unchanged docs and timestamps |
| Broken links | Context points to a missing test file; audit | Reports exact reference and missing coverage; no invented test evidence |
| Failed save | Thread directory is unwritable; prepare next session | Reports inability to save; no claim that a ready durable checkpoint exists |
| Closure with loose ends | Explicitly close work with two outstanding items | Saves durable context, routes both items, archives only afterward, repairs relative and inbound links |
| Farewell | 'Thanks, I am leaving for today' with unfinished work | Does not close or archive the thread; prepares continuation if requested or appropriate |
| Concurrent edit | Thread changes on disk after initial read | Re-reads before writing and preserves nonconflicting new content; flags conflicts |
| Teammate handoff | Ask to prepare tasks for Alex | Updates or creates Alex's handoff with references; sends no message |
| Independent install | Only prepare-next-session folder available | Uses bundled references to save required documents; does not fail because sibling skills are absent |

For each run record host/model, input fixtures, observed actions, artifact paths, pass/fail per
expected result, and unresolved limitations. At minimum evaluate missing context, existing context,
discussion-only, stale pass, spec-ahead, failed save, and closure before a public stable release.
