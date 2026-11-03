---
layout: post
title: "Every Webhook Needs a Delivery Receipt"
date: 2026-11-03 10:50:51 -0600
category: Product Strategy
description: "Webhook products need visible delivery receipts, replay controls, and reconciliation tools so customers can recover from missed events."
read_time: 5 min
---

A customer says an order never reached the warehouse system. The commerce platform shows the order. The integration service shows no error. The warehouse team sees nothing.

Three engineers open three dashboards. One asks for a request ID that nobody saved. Another checks logs that expired yesterday. The third suggests creating a test order and watching what happens.

The missing event has become an archaeological dig.

Webhooks often enter a roadmap as plumbing. Once customers depend on them, delivery state becomes part of the product.

## An HTTP status is not the whole receipt

A provider can prove that it sent a request. A consumer can prove that its endpoint returned a response. Neither fact proves that the business action completed.

The endpoint may acknowledge before processing, which is usually the correct design. A queue can accept the payload while a downstream worker later fails. A timeout can leave the provider uncertain even though the consumer committed the change. Duplicate delivery can then produce a second action.

That uncertainty creates what I call **delivery fog**. Every component has a local answer, but the customer cannot see one trustworthy story.

GitHub makes this boundary explicit. A slow endpoint can cause a failed delivery, GitHub records the failure, and failed deliveries are not automatically redelivered. Administrators can inspect recent deliveries and manually replay eligible events. The recovery path exists because transport outcomes need an operator-facing state.

## Give every event a durable work card

A webhook delivery receipt should be a first-class product object. It needs a stable event identifier, the subscription and destination, event type, creation time, delivery attempts, response codes, latency, and current disposition.

The disposition should use plain states:

- Pending delivery
- Accepted by the endpoint
- Processing confirmed
- Failed and retrying
- Exhausted and awaiting action
- Replayed, reconciled, or intentionally ignored

The distinction between accepted and processed is important. Some providers cannot observe the consumer's downstream work. Their receipt should say so. Honest uncertainty is better than a green check that only means an HTTP server answered.

Slack requires a quick successful response and recommends moving event processing into a queue. It retries failed requests on a defined schedule and sends headers that identify the retry number and reason. Those details are valuable evidence. They should be visible without asking a developer to search raw headers.

The receipt also needs a useful search surface. Let an operator filter by customer, endpoint, event type, time range, delivery ID, and outcome. Show a safe payload preview with sensitive fields redacted. The goal is fast diagnosis without turning the webhook console into a second data-leak path.

A durable event ID also gives the consumer a deduplication key. This is the same product boundary behind an [idempotency contract for agent tools](/blog/2026/10/26/ai-agent-tools-need-an-idempotency-contract/). The request may repeat, while the intended business effect should happen once.

## Replay needs a window and a warning

Replay is useful, but it is not a generic undo button. A replayed invoice event may send another email. A replayed fulfillment event may create another shipment if the consumer lacks deduplication. The interface should show the original delivery ID, event age, prior attempts, and expected destination before the operator confirms.

Every product also needs a replay window. GitHub exposes recent deliveries for three days. Shopify keeps delivery logs for seven days and retries failed webhook calls up to eight times over four hours. The exact periods vary, but the product obligation is the same. Customers need to know how long recovery remains possible.

Do not hide expiration in documentation. Put the remaining replay time beside the failed event. Notify the right owner before recovery evidence disappears. If the replay window closes, offer a reconciliation path instead of a dead end.

Reconciliation asks the source system for current truth. Shopify recommends periodic reconciliation because webhook delivery is not guaranteed. A customer should be able to select an outage period, compare source records with processed events, and import what is missing.

## Measure recovery, not delivery theater

Webhook dashboards often lead with total deliveries and success rate. Those numbers help, but they can conceal a small set of expensive failures.

Track time to detect a failed delivery, time to recover, events nearing replay expiration, duplicate effects prevented, and subscriptions disabled after repeated failures. Show failures by customer, endpoint, event type, and deployment version. A 99.9 percent delivery rate can still hide the order that mattered.

The product should also test its own recovery promises. Simulate a slow endpoint, a malformed response, an expired certificate, a queue failure after acknowledgment, and an out-of-order event. Verify that receipts remain understandable and that replay does not create a second business action.

The useful customer promise is not that every webhook arrives once. Distributed systems rarely offer that neat guarantee.

The better promise is that every event leaves a receipt, every uncertain outcome has a visible state, and every recoverable failure has a bounded path back to truth.

## Sources

- [GitHub Docs: Redelivering webhooks](https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/redelivering-webhooks)
- [Slack Developer Docs: The Events API](https://docs.slack.dev/apis/events-api/)
- [Shopify Dev: Troubleshoot webhooks](https://shopify.dev/docs/apps/build/webhooks/troubleshoot)
