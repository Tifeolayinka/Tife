# Validation record

Validated locally on 2026-10-24. Release candidate: 0.1.0.

| Check | Result |
|---|---|
| Skill Creator `quick_validate.py` | All nine skills passed |
| Collection metadata, local skill links, and plugin manifest | Passed |
| Bundled references match shared source | Passed |
| Repository Markdown links | Passed |
| Developer-machine absolute path scan | No such paths in distributed text sources |
| Fresh installation into a disposable directory | Passed; references copied and unrelated files retained |
| Existing skill collision | Passed; refused before writing |
| Dangling symlink collision | Passed; refused without replacing link |
| Dry-run installation | Passed; target directory not created |
| Simulated copy failure | Passed; new skill folders rolled back, unrelated content retained |
| Corrupt bundled reference | Passed; installation refused before writing |

Seven automated unittest cases passed. Tests used disposable directories, not live Codex or
Claude installations. The external Skill Creator validator used an existing local PyYAML package;
the distributed scripts require only Python's standard library.

These are packaging and installer checks. The worked example illustrates the intended workflow,
but is not evidence of a live model executing the skills. Automatic selection, runtime behavior,
and the Claude plugin loading path have not been exercised in a live host. The documented
folder-copy installation was tested locally.

Manual behavioral cases are in [evals/scenarios.md](evals/scenarios.md). Follow those before calling
this a behaviorally verified stable release. Validation did not install into a live agent host. The collection is published separately.

## Instruction refinement — 2026-10-24

All nine entrypoints now specify reference-loading conditions and observable completion criteria.
Duplicated preparation, review, and closing procedures delegate to their bundled source references.
Names, document formats, installation behavior, and invocation policy are unchanged.

A source-level comparison checked preservation of: automatic creation of missing context and
threads; one active record per workstream; planning-only continuation; short prompts with actual
thread paths; decisions and failed attempts; requirement-linked tests and evidence; Needs recheck
for stale results; read-only reviews; document-only teammate handoffs; and saving/routing before
archive. This is an instruction review, not a live-model behavioral test.

Revalidation passed all nine Skill Creator checks, bundled-reference parity, collection packaging,
seven installer tests, and Git whitespace checks. The live-host limitations above still apply.
