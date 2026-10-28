---
layout: post
title: "An AI Agent Stop Button Must Stop the Work"
date: 2026-10-28 10:52:56 -0500
category: Product Strategy
description: "Stopping an AI agent should cancel owned work, preserve completed effects, run cleanup, and leave a durable receipt users can trust."
read_time: 5 min
---

A user starts an agent, notices the wrong customer list, and presses Stop. The spinner disappears. Ten minutes later, the agent finishes the export and sends it anyway.

The button worked on the screen. It failed everywhere that mattered.

Stopping an AI agent is not a display state. It is a product promise about what will no longer happen, what already happened, and what the user must do next. That promise needs a cancellation contract.

## Draw the stop boundary first

Long-running agents rarely perform one neat operation. They call models, launch workflows, create files, update records, reserve compute, and ask other services to continue the job. Hiding the progress panel does not cancel any of those things.

The product team should define a stop boundary for every agent task. The boundary lists the work owned by that task and the cancellation behavior for each dependency. Immediate stops are possible for some work. Other work can only receive a request. The rest may already have crossed an irreversible line.

OpenAI's background mode makes the first distinction visible. A background response has a cancellation endpoint, and repeated cancellation calls return the final response object. A synchronous response uses connection termination instead. The interface cannot treat those execution modes as if they carry the same stop guarantee.

Map every operation into one of four groups:

- **Interruptible:** computation or waiting that can end without cleanup.
- **Cooperative:** work that must receive a signal and reach a safe checkpoint.
- **Compensatable:** completed work that needs an explicit reversal.
- **Irreversible:** messages, external commitments, or disclosures that cannot be recalled.

That map should exist before the Stop button appears. Otherwise the control advertises certainty that the system does not have.

## Cancellation has to travel

An agent may stop its reasoning loop while a downstream job continues. The gap is easy to miss because the parent task looks quiet.

Temporal's cancellation model shows why propagation is an implementation choice. Cancellation can flow from a workflow to activities and child workflows, but activity behavior depends on configuration. A running activity receives cancellation only when it heartbeats or otherwise supports the signal. Temporal also supports non-cancellable scopes for cleanup after the main workflow has been cancelled.

Those mechanics point to a product requirement. Every owned child operation needs a known cancellation path, a deadline for acknowledging it, and a fallback when it stays alive. The parent cannot report “stopped” while a child remains in an unknown state.

Cloud orchestration adds another complication. AWS Step Functions describes cancellation of integrated jobs as a best-effort attempt. Permissions or a service outage can prevent the downstream task from stopping, and charges may continue. That is not an edge case for the infrastructure team to hide. It changes what the product can honestly tell the user.

Use separate states for **stop requested**, **stopping**, **stopped**, and **stop incomplete**. They sound fussy until the first expensive job or customer message survives a cheerful green checkmark.

## Preserve the effects that already escaped

Cancellation does not rewind time. If an agent created a ticket, sent a file, or changed access before the request arrived, the product must preserve that fact.

This is where the [idempotency contract for agent tools](/blog/2026/10/26/ai-agent-tools-need-an-idempotency-contract/) becomes useful. Stable operation identities let the system distinguish a completed side effect from a pending call. Cancellation can then stop future work without erasing the evidence needed for repair.

Give the user a cancellation receipt. It should record the task, request time, acknowledged time, final state, completed effects, work still running, cleanup attempts, and actions that need review. The receipt turns a vague button press into an auditable transition.

A good receipt can be plain:

> Stopped before 42 of 50 records were updated. Eight records changed. No email was sent. A rollback is available until 3:00 PM.

That message respects the user's actual problem. “Task cancelled” does not.

## Test for late effects

Most cancellation tests are too polite. They stop a task between steps, when nothing is in flight. Production users press Stop during the awkward moments.

Test while a tool call is committing, a child workflow is starting, a retry is waiting, and cleanup is failing. Disconnect the worker after it receives the signal. Remove the permission needed to cancel a downstream job. Press Stop twice. Press it after completion but before the interface learns the result.

Measure acknowledgement time, time to quiescence, child operations left alive, effects completed after the request, cleanup failures, and receipts that later changed state. Review every case where the interface claimed more certainty than the execution record supported.

The visual control is the easy part. The real product is the stop boundary behind it. When an agent can act across systems, Stop must mean that owned work is ending, escaped effects are visible, and uncertainty has somewhere honest to go.

## Sources

- [OpenAI: Background mode](https://developers.openai.com/api/docs/guides/background)
- [Temporal TypeScript SDK: Activity cancellation](https://typescript.temporal.io/api/namespaces/activity)
- [AWS Step Functions: Service integration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html)
