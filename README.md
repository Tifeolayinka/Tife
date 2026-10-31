# Tife

A development skill collection that keeps feature knowledge, working state, and test evidence
available across AI conversations. Save the documents, then hand the next session a short prompt
pointing to the work record.

**Status:** v0.1.0. Nine skills, shared templates, local installation tooling, and validation.
The instructions are portable Markdown. Codex UI metadata and a Claude Code plugin manifest are
included; host-specific discovery and automatic invocation depend on the installed application.
No hooks, background services, or external accounts are required.

## Skills

| Skill | Purpose |
|---|---|
| `tife-create-thread` | Start a feature, fix, or investigation record; reuse ongoing work |
| `tife-update-context` | Create missing context or update established knowledge |
| `tife-update-thread` | Checkpoint progress, decisions, failed attempts, and remaining work |
| `tife-maintain-tests` | Maintain requirement-linked scenarios and actual verification results |
| `tife-prepare-next-session` | Save context and return a short continuation prompt |
| `tife-sync-context` | Compare requirements and documentation with implementation |
| `tife-audit-context` | Check document consistency, links, duplication, and coverage |
| `tife-update-teammate-handoff` | Maintain a person's linked task and question document |
| `tife-end-thread` | Save durable knowledge, route unfinished items, and archive work |

## Install as a Claude Code plugin

In Claude Code, add this repository as a plugin marketplace, then install the plugin:

```text
/plugin marketplace add Tifeolayinka/Tife
/plugin install tife@tife
```

Start a fresh session afterwards so the skills load. To update later, run
`/plugin marketplace update tife`. Use either the plugin or the local folder install below, not
both.

## Install locally

Requires Python 3.9 or later for the helper scripts; using the skill instructions themselves
does not require Python. Clone the repository, then install from its root:

```sh
git clone https://github.com/Tifeolayinka/Tife.git
cd Tife
python3 scripts/validate.py
python3 scripts/install.py --target ~/.codex/skills
```

For Claude Code user skills, use `--target ~/.claude/skills`. For a project-scoped installation,
use its agent's supported skill directory, for example `--target /path/to/project/.claude/skills`.
If Codex uses a custom CODEX_HOME, pass its `skills` directory explicitly.

The installer copies the nine self-contained `tife-*` folders, including references and UI
metadata. It refuses existing destination folders, leaves unrelated skills alone, and does not
edit agent settings. Run with `--dry-run` to preview. To update an existing installation, back up
and remove only this collection's nine installed folders, then reinstall. Keep any custom edits
before replacing them. Reload skill discovery or start a fresh session as your host requires.

Install the complete collection for the full workflow. An individual folder is also self-contained
and can be copied manually; its references explain supporting document operations without requiring
the other skills. Do not install both the plugin and loose skill folders in the same host, as that
can create duplicate entries.

## Use

In a host supporting `$skill-name` invocation:

```text
Use $tife-create-thread to start planning notification preferences. Do not implement yet.
Use $tife-update-context to record the notification rules we agreed on.
Use $tife-maintain-tests to prepare the feature's test scenarios.
Use $tife-update-thread to save our current progress.
Use $tife-prepare-next-session before I clear this context window.
Use $tife-sync-context to check the notification docs against the implementation.
Use $tife-audit-context to review the notification documents for contradictions.
Use $tife-update-teammate-handoff to prepare the remaining UI questions for a teammate.
Use $tife-end-thread to close this completed feature work.
```

For other hosts, select the installed skill by name or ask in natural language. The exact command
syntax is host-specific. Natural-language triggers help selection but do not guarantee automatic
execution; explicitly prepare the next session before clearing context.

## What gets saved

Default project layout (existing project conventions take precedence):

```text
docs/
  context/
    notification-preferences.md
    notification-preferences-technical.md
  threads/
    notification-preferences-work.md
    OPEN-ISSUES.md
    archive/
  tests/
    notification-preferences.md
  handoffs/
    teammate.md
```

Requirements live in context. Tests reference those requirements. Threads reference both and
hold the current work state. Technical context is separate only when useful. A thread follows
one line of work across many conversations; a new conversation does not create a duplicate thread.

Session preparation automatically creates missing context and thread records or updates existing
ones. It saves relevant tests and returns something like:

> Read `docs/threads/notification-preferences-work.md` and continue the persistence work.
> Run the outstanding checks after saving preferences works, then report the results.

The prompt contains the actual saved path and next instruction. Detailed state stays in the
documents. Planning sessions work too: the instruction can be to keep discussing before building.

See the [complete worked example](examples/README.md) for linked context, thread, and test documents
plus the short continuation prompt. All example scenarios are explicitly marked Not run.

## Operating principles

- Preserve current user intent, constraints, and the agreed stopping point.
- Separate agreed behavior, observed implementation, proposals, and open questions.
- Never label a check Passed without execution evidence.
- Preserve failed attempts and decision rationale; reconcile stale current-state sections.
- Do not let syncing erase requirements just because implementation is incomplete.
- Keep session handoffs distinct from teammate handoffs.
- Do not automatically commit, publish, send messages, install hooks, or clear context.

See [the shared workflow](shared/workflow.md), [document outlines](shared/documents.md),
[test contract](shared/testing.md), and [session handoff contract](shared/handoff.md).

## Contribute and validate

Shared source lives in `shared/`. Generated copies inside each skill make installations portable.
Edit shared source, then regenerate; do not edit bundled copies directly.

```sh
python3 scripts/bundle_references.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validation checks packaging, local links, reference parity, metadata, and the plugin manifest.
Installer tests verify portability and refusal to overwrite existing skills. These checks do not
prove an AI will follow every instruction. Use [behavioral evaluation cases](evals/scenarios.md)
to assess realistic use before broad rollout. No live-host behavioral evaluation is claimed.

## Repository and license

Public repository: [Tifeolayinka/Tife](https://github.com/Tifeolayinka/Tife).

The collection is MIT licensed. It contains no account credentials or private project data.
To contribute, fork the repository, make changes, run the validation commands above, and open
a pull request. Shared references should be edited in `shared/` and regenerated before submission.

## Acknowledgment

Inspired by the context and thread workflow in Timothy Tu's `tt-skills` collection, inspected at
version 0.12.0. This collection uses newly written instructions and adds an explicit thread-creation
skill, a dedicated test-document workflow, and the short document-reference handoff described above.
It does not bundle the original plugin's code, hooks, or project-specific content.
