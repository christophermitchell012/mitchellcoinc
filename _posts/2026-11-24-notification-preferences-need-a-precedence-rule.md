---
layout: post
title: "Notification Preferences Need a Precedence Rule"
date: 2026-11-24 10:04:14 -0600
category: Product Systems
description: "Notification products need explicit precedence across user choices, workspace policy, quiet hours, urgency, channels, and temporary overrides."
read_time: 6 min
---

The account owner turned off weekly summaries. Her workspace administrator required billing alerts. Her phone silenced the app overnight. At 2:13 a.m., a failed payment triggered all three rules.

The product sent a sound, an email, a badge, and two reminders.

Each individual setting looked reasonable. Together, they produced a result nobody had actually chosen.

Notification preferences are not a collection of toggles. They are a policy system that needs an explicit rule for resolving authority, urgency, channel, delivery schedule, and repetition.

## Separate authority from delivery behavior

Start by naming who can decide what. A workspace administrator may require a security event to be recorded and delivered somewhere. That does not automatically authorize a sound on every employee's personal phone.

Separate the decision to create a notification from the decisions to choose a recipient, channel, interruption level, delivery window, and retry pattern. One business requirement should not silently acquire control over all five.

Android makes part of this boundary concrete. Apps assign notifications to channels and choose initial channel behavior. After a channel exists, the user controls its visual and auditory behavior in system settings. The app can inspect those settings and direct the user to them, but it cannot simply reclaim control.

Apple requires notification authorization and advises apps to check current settings before scheduling notifications. A person can change the allowed interactions later. Product settings therefore describe intent, while the operating system remains an independent enforcement layer.

The interface should state that difference. “Critical alerts are on” is misleading when the device has denied sounds. Show the product preference, the effective device capability, and the route to fix a mismatch.

## Write the precedence rule down

A useful model resolves constraints from strongest to weakest:

- Legal or safety obligations determine whether an event must be retained or routed.
- Organization policy selects eligible recipients and approved channels.
- User preferences narrow optional topics, schedules, and interruption modes.
- Device settings determine what the application can actually present.
- Event urgency and freshness affect timing within those boundaries.
- Deduplication and acknowledgment prevent repeated noise.

This is a **notification precedence ladder**. Each rung limits the next one rather than erasing it.

The ordering will differ by product. A hospital alarm, bank fraud notice, team mention, and marketing update should not share one hard-coded rule. The important requirement is that the order be deliberate, testable, and visible to the people affected.

Defaults still matter. They are [product decisions about user time](/blog/2026/09/04/product-defaults-are-product-decisions/), not harmless starting values. Default every new topic to the quietest behavior consistent with its consequence.

## Treat urgency as data, not permission

Urgency should describe the event. It should not bypass a user's choices by itself. Define a small set of levels with objective criteria, maximum delay, eligible channels, repeat limits, and an owner responsible for misuse.

RFC 8030 gives web push messages explicit time-to-live and urgency fields. It also allows a topic to replace an outstanding message with the same topic. Those mechanics support three useful product behaviors: expire stale notices, delay low-value work, and replace redundant updates before delivery.

Use the same thinking above the transport layer. A delivery-status message can replace its earlier version. A meeting reminder should expire after the meeting starts. A resolved incident should suppress a queued escalation rather than arriving after the resolution.

Temporary overrides need boundaries too. “Mute for one hour” requires an exact start, end, time zone, affected topics, and behavior when the period ends. “Pause all” should say whether mandatory records, inbox entries, or administrator notifications continue.

Avoid override traps. A one-time choice should not rewrite the permanent preference. An administrator policy change should not quietly reset a user's device channel. A new notification type should not inherit the loudest existing category because implementation was convenient.

## Explain every effective outcome

When a notification is sent, suppressed, delayed, replaced, or downgraded, store the decision inputs. Record the event type, urgency, freshness deadline, organization rule, user preference version, device capability, quiet period, selected channel, deduplication key, and final outcome.

Support should be able to answer why a message did or did not interrupt someone. The user should see a shorter explanation such as “Delivered silently because your device channel is set to low importance” or “Email required by workspace billing policy.”

Build a preference preview for high-consequence products. Let a user or administrator choose a sample event and see the effective recipients, channels, delivery time, and interruption level before saving a policy change.

Measure opt-out rates by topic, device-level blocks, deliveries during quiet hours, administrator overrides, and repeated messages before acknowledgment. Track stale deliveries, replacement rates, and support cases about missing or excessive notifications. A high delivery rate can coexist with a broken notification product.

The event starts the process. Trust comes from resolving every layer of preference without pretending that the loudest rule always wins.

## Sources

- [Create and manage notification channels](https://developer.android.com/develop/ui/compose/notifications/channels), Android Developers.
- [Asking permission to use notifications](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications), Apple Developer Documentation.
- [Generic Event Delivery Using HTTP Push](https://www.rfc-editor.org/rfc/rfc8030.html), RFC Editor.
