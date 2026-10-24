---
name: tife-sync-context
description: "Compare documentation and tests with implementation to find drift. Review requests are read-only; sync requests permit evidence-backed documentation updates while preserving unresolved requirements and contradictions."
---

# Sync Context

Read [workflow](references/workflow.md), then follow **Sync: compare documents with implementation**
in [review](references/review.md). That section owns scope, modes, finding classifications, permitted
corrections, and verification metadata.

When writing a baseline or changing requirement structure, read the relevant outline in
[documents](references/documents.md). When evaluating scenarios or result confidence, read
[testing](references/testing.md).

**Done when:** each finding identifies the location, documented claim, implementation evidence,
classification, and next action. State the inspected scope and version; separate applied updates
from unresolved findings. In review mode, every file and timestamp remains unchanged. Requirements
that the code has not fulfilled remain visible; reading code does not establish a passed test.
