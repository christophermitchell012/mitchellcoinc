---
layout: post
title: "Session Timeouts Need a Grace State"
date: 2026-11-26 10:37:58 -0600
category: Security + Workflow
description: "Session timeout design should expire authority without discarding user work, using clear warnings, reauthentication, safe drafts, and honest recovery."
read_time: 6 min
---

A procurement manager spends forty minutes entering supplier details. She pauses to check a tax form, returns to the browser, and clicks Save. The application sends her to login. After authentication, it opens an empty form.

The session expired correctly. The product failed anyway.

Security requires an end to stale authority. It does not require an end to the user's work. A good timeout flow separates those two things and makes the boundary visible before the final click.

## Separate authority from work

An authenticated session proves that a user may act. A draft records what the user intends to submit. Those objects have different lifetimes and should not share one hidden timer.

When authority expires, stop privileged reads and writes immediately. Keep the unsent draft in a protected state that cannot execute, publish, approve, or reveal fresh server data. After successful reauthentication, restore the draft and ask the user to review any fields that may now be stale.

I call this **work-safe reauthentication**. The phrase describes a narrow promise: authority ends on schedule, while recoverable input survives long enough for the same authorized person to continue.

The storage choice depends on sensitivity. A harmless search filter may stay in browser memory. A benefits application may need an encrypted server draft with a short retention limit. A payment instruction may preserve field labels and non-sensitive context while requiring account and amount entry again.

Do not keep a privileged session alive because a form is dirty. That converts usability pressure into a longer attack window. Preserve the work object instead.

## Use more than one clock

NIST distinguishes an overall timeout from an inactivity timeout. The overall clock limits a session after authentication or reauthentication. The inactivity clock ends a session after the user stops acting. NIST also allows a warning before termination, but requires the session to end when either limit expires.

Those are security clocks. The interface also needs a warning clock and a draft-retention clock.

The warning should state what will happen, when it will happen, and what the user can preserve. “Your session expires in two minutes” is incomplete. “Sign in again within two minutes to keep editing this saved draft” gives the user a decision.

Activity must mean evidence from the user, not background noise. Polling, autosave, analytics, open sockets, and a rotating dashboard should not reset inactivity. Otherwise, a forgotten tab can remain authorized because the product kept talking to itself.

The server remains authoritative for expiry. OWASP recommends server-side idle and absolute timeouts because client-managed limits can be manipulated. A browser countdown is useful feedback, not the security control.

## Reauthenticate into a known destination

A timeout often occurs on the request that matters most. The user clicks Submit after the session has already expired. Redirecting that request through login can create duplicate actions, lost context, or an unsafe replay.

Store intent as data before reauthentication, not as a blind request replay. Record the destination, draft identifier, expected object version, and action type. Exclude secrets, one-time values, and raw authorization headers.

After reauthentication, return to a review state. Recheck permissions and reload current server data. If another person changed the record, show a conflict before submission. If the user's role changed, explain which part of the intended action is no longer allowed.

OpenID Connect provides a useful mechanism for freshness. Its `max_age` parameter states the maximum acceptable time since active authentication, and the returned token includes `auth_time` when that parameter is used. The relying product still decides how fresh authentication must be for the action at hand.

Do not treat every return from an identity provider as fresh proof. The identity provider may still have its own active session. For a sensitive action, require an authentication event recent enough for that action and verify the evidence the protocol returns.

## Design the grace state as a state machine

A countdown modal is only the visible edge. The underlying product needs explicit transitions:

1. **Active:** reads and writes are authorized under the current session.
2. **Warning:** authority still exists, but expiry is close and the draft is saved.
3. **Grace:** authority has ended, protected work remains, and no privileged action can execute.
4. **Restored:** reauthentication succeeded, authorization was checked again, and the draft is ready for review.
5. **Abandoned:** the grace period ended or the user chose to discard the draft.

Grace is not an extension of the old session. It is a holding state without application authority. That distinction should survive across tabs, devices, network loss, and service restarts.

If logout, password reset, account suspension, or administrator revocation occurs, decide whether drafts survive. The safe answer may differ by event. A voluntary logout can retain a personal draft. An account-compromise response may need to destroy it.

This is also where the design should connect with [bounded admin impersonation](/blog/2026/11/15/admin-impersonation-should-never-look-normal/). A support session needs a loud expiry boundary, but any unfinished customer-facing change should remain inert after authority ends.

## Test the unpleasant transitions

Test expiry between keystrokes, during file attachment, after a review screen, and while a submit request is in flight. Open the same draft in two tabs. Change the user's permissions during grace. Revoke the session from another device. Let the draft-retention limit expire while login is open.

Measure expired sessions, warning extensions, successful restorations, abandoned drafts, lost-work reports, duplicate submissions, authorization changes found after reauthentication, and drafts retained past policy. Segment by workflow because a dashboard and a tax filing carry different costs.

The goal is not to make timeouts painless. A real authority boundary should sometimes interrupt the user. The product earns trust by interrupting honestly, preserving only what is safe, and returning the person to a known state.

Expire the session. Keep the work inert. Then let fresh authority pick it up.

## Sources

- [Session Management](https://pages.nist.gov/800-63-4/sp800-63b/session/), NIST Digital Identity Guidelines.
- [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), OWASP Cheat Sheet Series.
- [OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html), OpenID Foundation.
