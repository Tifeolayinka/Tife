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
