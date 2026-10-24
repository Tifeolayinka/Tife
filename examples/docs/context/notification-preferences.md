---
id: notification-preferences
status: draft
updated: 2026-01-01T10:00:00+00:00
---
# Notification preferences

Fictional planning fixture. No implementation or verification claimed.

## Purpose and scope

Allow signed-in users to choose whether they receive optional product announcements.
Security notifications are outside this preference and remain enabled.

## Requirements

| ID | Behavior / acceptance criterion | State | Basis |
|---|---|---|---|
| NOTIFY-R1 | A signed-in user can save their own product-announcement preference; reopening settings shows the saved choice | Agreed, not verified | Fictional user decision |
| NOTIFY-R2 | Changing the product-announcement preference does not disable security notifications | Agreed, not verified | Fictional user decision |
| NOTIFY-R3 | A user cannot change another user's notification preference | Agreed, not verified | Fictional user decision |

## Behavior and edge cases

- Persistence must survive reopening settings.
- If saving fails, the expected user-facing recovery behavior is not yet settled.
- The initial preference for a newly created account is an open question.

## Decisions

| Decision | Reason | Source |
|---|---|---|
| Separate optional announcements from security notifications | Users should retain control over optional messages without losing security notices | Fictional user decision |

## Open questions

- Are new accounts opted in or opted out of product announcements?
- What should the user see when saving fails?

## Related documents

- [Active planning thread](../threads/notification-preferences-work.md)
- [Test plan](../tests/notification-preferences.md)

## Change history

- Fixture initialization: recorded agreed requirements and explicitly unsettled behavior.
