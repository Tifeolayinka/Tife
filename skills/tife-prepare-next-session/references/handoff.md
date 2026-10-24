# Preparing a fresh conversation

Session preparation saves the knowledge first, then returns a short reference prompt. The detailed
handoff lives in the thread's Current state and Remaining sections. Do not create a separate
handoff document or duplicate that detail in the pasteable prompt.

## Save before handing off

1. Identify the active work and read its existing records. Review the available conversation for
   requirements, decisions, corrections, scope limits, discoveries, progress, and failed attempts.
2. Update the relevant feature or subject context. If none exists, create it automatically using
   established facts. This also applies to planning and research: use a natural subject outline,
   without forcing code architecture or test cases onto discussion-only work.
3. Create or reconcile the existing thread for this same work. Set a precise stopping point,
   remaining requested work, necessary supporting tasks, and optional suggestions. Link the
   saved context and test documents. Keep status open.
4. Preserve relevant test scenarios and actual results. Create a missing test document for
   substantive feature work when requirements support one; flag unknown expectations.
5. Re-read the saved thread as a new reader. Can it explain the goal, present state, next action,
   stop point, and user's constraints? Verify referenced files exist and paths resolve.

If a necessary write fails, report it and do not claim the handoff is durable. Provide a clearly
labelled fallback summary only if useful. Never clear the user's context window or start another
chat automatically.

## Return the short prompt

Use the actual saved thread path, preferably project-relative when the next session opens the
same repository. Include a project locator if the destination is otherwise ambiguous. The thread
links to supporting documents. Include extra paths only when they are essential entry points.

Pattern, not boilerplate:

> Read `<actual-thread-path>` and continue <specific work> from where we stopped. <Next instruction
> grounded in the current state>. <Relevant user constraint or stopping point>.

Keep it to a few sentences. Do not include a full status recap, unrelated standard pipeline, or
new tasks. The next instruction can be 'continue discussing the design'; it need not be coding.
State restrictions when the user expressed them, not as a blanket refusal to perform normal work.

Example for discussion-only work:

> Read `docs/threads/development-skills.md` and continue designing the collection. Resolve the
> remaining questions with me before creating any skill files.

Example for implementation:

> Read `docs/threads/notification-preferences.md` and continue the persistence work. Run the
> outstanding checks after saving preferences works, then report the results.

## On pickup

Read the referenced thread and relevant linked context and tests. Recheck volatile state such as
the branch, working tree, running jobs, and prior failures before relying on it. Continue the
requested work under the current user's instructions. Saved suggestions are not approved tasks.
