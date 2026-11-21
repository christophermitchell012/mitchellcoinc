---
layout: post
title: "A Support Ticket Needs a Reproduction Packet"
date: 2026-11-21 10:56:03 -0600
category: Product Operations
description: "Design support tickets with a safe reproduction packet that captures product state, request context, versions, permissions, and evidence at failure time."
read_time: 6 min
---

The ticket says, “Export failed.” It includes a screenshot of a red banner, taken after the banner covered the useful part of the page.

Support asks which browser, which account, which report, which time zone, and whether the customer tried again. Two days later, the customer replies that it works now. Engineering closes the issue with no explanation, and the same failure returns next month wearing a different ticket number.

The missing feature is a reproduction packet: a bounded collection of product state and technical evidence captured when the failure occurs, attached to the support case with customer awareness and appropriate access controls.

## Capture the moment before it disappears

Most diagnostic questions become harder after the event. Feature flags change. A deployment finishes. Tokens expire. A background job retries. The customer navigates away, and browser state that could explain the failure vanishes.

The product should collect the fields it already knows at the moment a user reports a problem:

- Account, workspace, user role, and relevant permissions.
- Product area, object identifier, and attempted action.
- Client, application, API, and schema versions.
- Feature flags and configuration values that affected the path.
- Local timestamp, server timestamp, and time zone.
- Request or trace identifier and final error code.
- Recent state transitions for the affected object.

This is not permission to copy the entire environment into a ticket. The packet should be scoped to the failed workflow and generated from a documented allowlist. More data can make diagnosis slower while increasing privacy and security risk.

## Connect the customer symptom to the system trace

A screenshot proves that pixels appeared. It rarely identifies the request, worker, queue item, or downstream dependency that produced them.

OpenTelemetry context propagation offers the underlying mechanism. A trace identifier and span relationships can connect activity across services and processes, while logs can carry the same context. The support product does not need to expose the entire tracing system to the customer. It needs to preserve a stable correlation key that engineering can follow.

Show that identifier in an expandable error detail and copy it into the ticket automatically. The identifier should also survive asynchronous boundaries such as queues, scheduled jobs, webhooks, and retries. Otherwise the trail ends at the first background worker.

The packet should record which deployment and configuration were active for that trace. Without those versions, a successful replay against today's code may only prove that the product changed.

## Sanitize before the packet leaves the boundary

Diagnostics can be unusually concentrated collections of secrets. URLs may contain identifiers. Headers can contain authorization material. Request bodies may include personal data. Console logs occasionally reveal information nobody intended to store twice.

Chrome DevTools handles this distinction explicitly when exporting network requests. Its default HAR export is sanitized and excludes sensitive headers such as `Cookie`, `Set-Cookie`, and `Authorization`. A separate, deliberate option is required to include sensitive data.

That is a sound product pattern. Generate the least-sensitive packet by default. If deeper evidence is necessary, explain what additional fields will be collected, why they matter, who can access them, and when they will expire.

GitHub Enterprise Server uses a similar boundary for support bundles. Its documentation distinguishes diagnostic files, standard bundles, and extended bundles, while noting that specified log directories are sanitized for authentication tokens, keys, and secrets.

Sanitization needs tests, not reassuring copy. Seed synthetic secrets in every supported location, generate a packet, and verify that none survive. Test filenames, query strings, headers, nested JSON, binary attachments, copied console output, and third-party integration logs.

## Make the packet useful after collection

A ZIP file with forty vaguely named logs is merely **evidence confetti**. The packet needs a manifest that tells the next person what it contains and how the pieces relate.

Include the case identifier, capture time, workflow, object identifiers, versions, trace identifier, included artifacts, redactions performed, retention deadline, and a checksum for each attachment. Mark missing evidence explicitly. “No client log available” is more useful than silence.

Support should see a short product summary before the raw artifacts. Engineering can then open the trace, inspect the precise configuration, and follow a replay recipe if the action is safe to reproduce. Customer-visible status should distinguish captured, reproducible, diagnosed, fixed, and unable to reproduce.

This complements [safe admin impersonation for support](/blog/2026/11/15/admin-impersonation-should-never-look-normal/). Impersonation can reveal the customer's current experience. A reproduction packet preserves the experience that existed when the failure happened. Those are different kinds of evidence.

Measure packet coverage for priority failures, time from ticket creation to the first useful engineering artifact, reproduction rate, redaction defects, packets opened, and packets that expire without use. A packet nobody trusts or opens is another attachment ritual.

The customer should still be able to describe the problem in ordinary language. The product's job is to keep that person from becoming an unpaid log-collection technician while the evidence quietly evaporates.

## Sources

- [Network features reference](https://developer.chrome.com/docs/devtools/network/reference), Chrome for Developers.
- [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/), OpenTelemetry Documentation.
- [Providing data to GitHub Support](https://docs.github.com/en/enterprise-server@3.20/support/contacting-github-support/providing-data-to-github-support), GitHub Docs.
