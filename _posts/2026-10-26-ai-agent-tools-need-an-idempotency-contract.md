---
layout: post
title: "AI Agent Tools Need an Idempotency Contract"
date: 2026-10-26 10:55:05 -0500
category: Product Strategy
description: "Agent retries can duplicate charges, tickets, and orders. An idempotency contract makes uncertain outcomes safe to inspect and repeat."
read_time: 5 min
---

The most dangerous agent failure can look like success. A tool call times out, the agent retries, and two purchase orders appear. The interface reports one clean result. Operations finds the twin later.

Teams often treat this as a model problem. They tune the prompt, lower the temperature, or add another instruction about caution. None of those changes can tell whether the first request reached the system of record. The uncertainty lives below the model.

An agent that can change state needs an idempotency contract. That contract gives one intended action a stable identity across retries. It also defines what the product shows when the outcome is still unknown.

## A timeout is not a verdict

A timeout says the caller stopped waiting. It does not say the action failed.

The receiving service may have created the refund, booked the shipment, or opened the ticket before its response disappeared. A fresh retry can repeat the side effect. The agent then pays a duplicate-action tax: extra work, customer confusion, financial exposure, and a trail that is hard to reconstruct.

This problem grows as agents gain broader authority. A conversational answer can be regenerated with little consequence. A payment, access change, or customer notification cannot. That is why [agent permissions need explicit product boundaries](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/), and why retry behavior belongs inside the same boundary.

The product should classify every tool operation before launch:

- Read-only calls can usually be repeated.
- Naturally idempotent writes can converge on the same state.
- Non-idempotent writes need a stable operation key and durable result.
- Irreversible writes may also need confirmation or human review.

This classification is more useful than a generic “retry on error” rule. It connects technical behavior to the cost of being wrong.

## Give the intention a durable name

The key should represent the user-approved intention, not an individual network attempt. If an agent tries three times to create the same invoice, all three requests should carry the same key. A genuinely new invoice should receive a new one.

That sounds small. It changes the product contract.

Stripe stores the first result for an idempotency key after execution begins and returns the saved result on a matching retry. It also rejects reuse when the parameters differ. Amazon EC2 uses client tokens for many mutating calls and can return an `IdempotentParameterMismatch` when a token reappears with changed inputs. Both behaviors protect users from an agent quietly changing its mind under an old identity.

The agent layer should preserve four fields together: operation key, normalized intent, current status, and returned result. The status cannot be only success or failure. It needs an unknown state for cases where the caller has no trustworthy answer yet.

Call that record a retry receipt. It gives the interface something concrete to inspect before another attempt. It also gives support and audit teams a shared reference when the execution trail gets messy.

## Design the unknown state on purpose

Many agent interfaces collapse uncertainty into a red error banner. That invites the user to click again. The product is effectively asking a person to gamble on whether the first action happened.

A better interface separates three conditions:

1. **Rejected:** the system did not accept the request, so a corrected attempt may be safe.
2. **Pending or unknown:** execution may have started, so the product should reconcile status before resubmission.
3. **Completed:** the result is durable, and later retries should return that result without repeating the action.

Microsoft’s retry guidance makes the underlying risk plain: a service can process a request successfully and still fail to return the response. It also recommends bounded retry policies that distinguish transient faults from lasting failures. An agent product needs to expose that distinction instead of burying it inside middleware.

This is where orchestration earns its keep. Before repeating a consequential action, the agent can query by operation key, inspect the current resource, or ask the user to resolve a genuine conflict. Automatic retries remain useful, but only inside a known envelope.

## Measure duplicate prevention, not retry volume

Retry counts are operational signals. They are not proof that the product is safe.

The useful measures sit closer to user outcomes: duplicate actions prevented, unknown outcomes reconciled, parameter mismatches blocked, and manual recoveries required. Track how long an operation remains unknown. Track which tools still lack stable keys. Review the cases where a human had to compare two systems.

Start with the actions that move money, change access, create external commitments, or contact customers. Require a retry receipt for each one. Test response loss after the downstream system commits. Confirm that the next attempt returns the prior result instead of creating another side effect.

There is no perfect network and no perfect agent. There can be a clear promise: one approved intention produces at most one consequential action. Once that promise becomes visible in the product, retries stop being hopeful repetition and become controlled recovery.

## Sources

- [Stripe API: Idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- [Amazon EC2: Ensuring idempotency in API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html)
- [Microsoft Azure Architecture Center: Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)
