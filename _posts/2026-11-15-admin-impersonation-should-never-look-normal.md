---
layout: post
title: "Admin Impersonation Should Never Look Normal"
date: 2026-11-15 10:13:28 -0600
category: Security + Product
description: "Admin impersonation should use bounded sessions, unmistakable visual state, dual attribution, and a clean exit instead of borrowing a customer identity."
read_time: "5 min read"
---

A support engineer opens a ticket from a billing administrator who cannot complete a month-end export. The account looks healthy from the support console. The failure appears only inside the customer workspace.

The engineer selects `Impersonate`, reproduces the error, and fixes a saved filter. Twenty minutes later, an audit reviewer sees that the customer changed the filter.

The support problem was solved. The identity problem was hidden.

Admin impersonation is useful because it places support inside the exact permissions, data, and interface that produced a failure. It is dangerous for the same reason. A safe product must bound the session, make its state unmistakable, and attribute every action to both people involved.

## Start with a bounded support purpose

Impersonation should not begin with a customer search and one powerful button. Start with a support case, a reason, and an expected task.

The operator should select the target account, ticket identifier, allowed workspace, requested capability, and session duration. The product can then issue temporary authority that fits the stated purpose.

NIST defines least privilege as granting only the access needed to complete an assigned task. That principle matters inside an impersonation session. A support engineer investigating an export should not inherit billing changes, user deletion, API key creation, or every permission held by the customer.

Use read-only access as the default. Add narrow write capabilities only when the case requires them. High-impact actions should remain unavailable or require a separate approval and fresh authentication.

OWASP recommends denying access by default and validating permissions on every request. Impersonation does not suspend those rules. Each request still needs authorization against the temporary support grant, the represented user, the tenant, and the requested object.

That model also prevents a stale browser tab from outliving the ticket. Closing the case, revoking the grant, changing the operator's role, or reaching the time limit should end the session immediately.

## Make the borrowed state impossible to miss

An impersonated session should never resemble an ordinary customer session.

Place a persistent banner around the entire experience. Show the support operator, represented user, tenant, case number, remaining time, and a clear exit control. Change the color and browser title. Keep the state visible across navigation, modal dialogs, and new tabs.

I call an interface that hides who currently holds authority **identity blur**. It invites an operator to forget the boundary and makes screenshots, recordings, and support notes ambiguous later.

Customers should also know what the session can do. A pre-session notice may be appropriate for planned support. A post-session notice may fit urgent investigations. Policy will vary, but silence should be a deliberate choice rather than an accidental default.

The operator needs friction at the right moments:

- Require a reason and case identifier before entry.
- Display a countdown before expiration.
- Confirm any newly requested write capability.
- Block credential, payment, and security-setting changes by default.
- End all impersonated tabs from one exit action.

Do not rely on a small avatar badge. The risk follows the session, so the visual state must follow the session too.

## Preserve both identities in every record

An action performed during impersonation has two actors. The represented user supplies the product context and permissions. The support operator supplies the intent and physical action.

Store both identities on every audit event. Include tenant, session identifier, support case, reason, original operator role, represented-user role, requested object, action, outcome, timestamp, source, and authorization-policy version.

GitLab documents that administrators can impersonate users and take actions on their behalf. It also captures impersonation activity with audit events. That is a baseline, but the product record should make dual attribution easy to query rather than bury it in a generic metadata field.

Customer-facing history should not say only that the customer changed a setting. A clearer entry says that a named support operator changed it while representing the customer under a specific case.

Internal analytics need the same distinction. Impersonated clicks should not inflate customer adoption, conversion, or feature-use measures. Separate support activity before events reach the product analytics model.

This echoes [treating authority as a product decision](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/). Capability is not enough. The product must preserve the actor, borrowed authority, supporting evidence, and review path.

## End authority, then verify the outcome

Stopping impersonation should revoke the temporary grant, invalidate related session tokens, close active streams, and return the operator to a neutral support surface. A banner disappearing from one tab is not a complete exit.

Show a session receipt after termination. Summarize entry and exit times, represented account, capabilities used, records viewed, changes made, blocked actions, approvals, and any exports or downloads.

The receipt should link back to the support case and provide a customer-safe version when policy allows. It should also identify work that needs reversal or customer confirmation.

Measure the workflow with care. Track sessions without case identifiers, permission expansions, expired sessions, blocked actions, changes reversed, customer disputes, and events missing dual attribution. Review outliers by operator, tenant, capability, and support queue.

Test the exit path as aggressively as entry. Cover browser crashes, network loss, role changes, account suspension, ticket closure, tab duplication, and service restarts. Temporary authority must remain temporary when the happy path breaks.

Impersonation is not a shortcut around the product's permission model. It is a privileged support workflow inside that model.

Make the purpose narrow. Make the state loud. Keep both identities. Then support can reproduce a customer's problem without rewriting who performed the work.

## Sources

- [GitLab Docs: Admin Area and User Impersonation](https://docs.gitlab.com/administration/admin_area/#user-impersonation)
- [OWASP Cheat Sheet Series: Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [NIST SP 800-53 Rev. 5: Security and Privacy Controls](https://doi.org/10.6028/NIST.SP.800-53r5)
