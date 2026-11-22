---
layout: post
title: "An Invitation Is a Temporary Credential"
date: 2026-11-22 10:05:12 -0600
category: Identity + Access
description: "Treat product invitations as temporary credentials with explicit authority, verified identity, expiration, revocation, and an auditable acceptance receipt."
read_time: 6 min
---

The invitation sat in an inbox for six days. During that time, the project changed, the contractor's assignment narrowed, and the administrator who sent it went on vacation.

On day seven, the contractor accepted the original link and received the original access.

Nothing in the acceptance screen showed that the business decision behind the invitation had aged. The link still worked, so the product treated the authority as fresh.

An invitation is not friendly email wrapped around a Join button. It is a temporary credential that carries a proposed identity, destination, role, scope, and deadline from one person to another.

## Bind the invitation to the intended authority

An invitation should say exactly what will happen if it is accepted. “Join the workspace” is thin consent when the result may include production data, billing access, shared channels, repositories, or administrative tools.

The invitation record should bind:

- The inviting organization and destination workspace.
- The intended recipient or allowed identity condition.
- The proposed role, teams, groups, and resource scope.
- The inviter and approval chain.
- The creation and expiration times.
- The policy version evaluated before activation.

Do not calculate the role again from whatever default exists at acceptance time. Do not silently add a newly configured default group. The recipient should accept the authority that was displayed, and a material change should produce a new invitation.

This is the human version of [treating authority as a product decision](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/). Capability is not the same as permission, and permission should remain bounded by consequence.

## Link possession is not enough identity

Invitation emails get forwarded. Shared mailboxes have several readers. Addresses are recycled after employees leave. A link can therefore reach somebody other than the person the inviter pictured.

GitHub binds an email-based organization invitation to a verified email address on the accepting account. Its documentation also states that invitations expire after seven days and that required two-factor authentication must be enabled before acceptance. Those are separate checks for recipient, time, and account posture.

Microsoft Entra B2B makes the destination boundary visible too. Its direct redemption links carry tenant context, and invited guests authenticate before completing consent. The acceptance changes the guest from a pending state to an accepted state.

The product should show both identities during redemption: the account currently signed in and the address or identity condition named by the invitation. If they do not match, stop cleanly. Do not offer a tiny “continue anyway” link that turns an identity failure into a usability shortcut.

Some products intentionally use broad invite links. That can be appropriate for a low-risk community or training space. The interface should then state that anyone with the link may claim a seat, cap the number of uses, allow immediate deactivation, and avoid attaching privileged roles to the link.

## Expiration is necessary but incomplete

Time limits reduce exposure, but an unexpired invitation can still be stale. The inviter may leave. The project may close. The recipient may change employers. A role may gain new permissions after the invitation was sent.

Treat acceptance as a fresh authorization event. Recheck the inviter's authority, available license, recipient eligibility, organization policy, role definition, and resource existence immediately before membership becomes active.

OWASP recommends that account-recovery URL tokens be random, sufficiently long, stored securely, single use, and expired after an appropriate period. An invitation token deserves the same baseline because possession can result in account or workspace access.

Single use also needs precise behavior under races. Two browser tabs should not create two memberships or apply the invitation twice. Acceptance should make one atomic transition from pending to accepted, with later attempts receiving the completed state rather than replaying side effects.

Build explicit states for pending, accepted, expired, revoked, superseded, and failed. Resending should not create a pile of independently valid links. Prefer a new token that supersedes the old one while preserving the invitation history.

## Leave an acceptance receipt

After activation, the administrator and recipient should be able to see what happened. Record the invitation identifier, inviter, recipient account, verified identity, destination, granted role and groups, policy checks, acceptance time, and resulting membership identifier.

Call this record an **authority landing receipt**. It closes the gap between permission offered and permission actually established.

The receipt should also explain deviations. Perhaps a requested group no longer existed, a license was unavailable, or policy removed one privilege. For high-impact access, partial acceptance is usually worse than a clean failure because neither side knows which promise survived.

Measure pending invitations by age, expired and revoked invitations, repeated sends, identity mismatches, activation failures, accepted invitations with later role corrections, and time until unused access is removed. Review privileged invitations separately from ordinary membership.

The email is only delivery. The product is the controlled transfer of authority, including the moment the transfer should no longer be allowed.

## Sources

- [Inviting users to join your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization), GitHub Docs.
- [B2B collaboration invitation redemption](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience), Microsoft Learn.
- [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html), OWASP Cheat Sheet Series.
