# Worked example: preparing to clear context

This is a fictional, discussion-only notification preferences feature. No application code was
inspected or built, and no tests ran. Dates below are fixture data, not real execution evidence.

Suppose a user agrees on notification rules, then says:

> Prepare the next session. Keep discussing the design; don't implement yet.

With no existing documents, session preparation would create the following linked records:

- [Feature context](docs/context/notification-preferences.md): agreed behavior and open questions.
- [Thread](docs/threads/notification-preferences-work.md): the goal, current state, and next instruction.
- [Test document](docs/tests/notification-preferences.md): scenarios derived from agreed behavior,
  all marked Not run.

There is no technical companion yet because architecture has not been established. It can be added
when that knowledge exists. Preparing a future session updates these same records rather than
creating another thread for the same work.

The final pasteable handoff would be:

> Read `docs/threads/notification-preferences-work.md` and continue designing notification
> preferences. Resolve the default opt-in question with me before implementation. Don't write
> application code yet.

Those paths are relative to this example project. In real use they point to documents in the
actual project. The short prompt does not repeat the requirements, test plan, or conversation.

If the user later changes the behavior, update the existing context and affected scenarios. If
tests had passed for the earlier behavior, preserve that evidence and mark affected current results
Needs recheck. When work moves to implementation, update this thread's current state and next steps.
