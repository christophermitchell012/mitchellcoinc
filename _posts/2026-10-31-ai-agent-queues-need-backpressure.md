---
layout: post
title: "AI Agent Queues Need Backpressure"
date: 2026-10-31 10:46:31 -0500
category: Product Strategy
description: "AI agent queues need admission limits, honest wait states, and fair scheduling so accepted work does not become a promise the system cannot keep."
read_time: 5 min
---

An agent accepts a research job that usually takes ten minutes. Then a customer imports 200 of them.

Every request gets the same cheerful status: started.

Nothing is broken in the narrow technical sense. The work is safely stored, workers are busy, and the queue will eventually drain. But the fiftieth customer is not waiting ten minutes. They may be waiting until tomorrow, while the product keeps pretending capacity has no consequences.

AI agent queues need backpressure.

Backpressure is the mechanism that keeps a fast producer from overwhelming a slower consumer. For an agent product, it is also the discipline of refusing, delaying, or reshaping new work before an invisible backlog turns into a false promise.

## Admission is a product decision

Reactive Streams was designed around a blunt systems fact: asynchronous consumers should not be forced to buffer arbitrary amounts of data. The receiver signals how much work it can handle, which allows the queue between components to stay bounded.

An agent interface needs its own version of that signal. Before accepting a task, estimate the expected compute, tool calls, concurrency, deadline, and customer priority. Compare that demand with available capacity and the work already committed.

The result shouldn't always be yes.

A useful admission policy can start now, reserve a later slot, ask the user to reduce the scope, route the job to a cheaper mode, or decline it with a clear reason. Those choices are product behavior, not queue configuration.

This is where teams accumulate what I call **promise pressure**: the gap between work the product has accepted and work it can finish within the expectation it created. Queue depth measures items. Promise pressure measures broken expectations.

## Give waiting work a receipt

“Queued” is too thin for work that may spend an hour there. A user needs to know whether the task has a place, what could delay it, and when the estimate changed.

Give every accepted job a queue receipt with:

- its admission time and current state
- an estimated start window, not a fake precise countdown
- priority and the reason for that priority
- the capacity or spending limit assigned to it
- a way to cancel, narrow, or reschedule before execution

The receipt should distinguish accepted, reserved, waiting, running, blocked, and expired. A task that cannot begin before its deadline should expire in the queue instead of consuming resources after its answer has lost value.

Amazon SQS makes one important boundary explicit through visibility timeouts. A received message becomes temporarily invisible while a consumer works on it. If processing does not finish before the timeout, the message can become available again, which can create duplicate work. The timeout is therefore part of the processing contract, not housekeeping.

Agent jobs need the same honesty about ownership. The product should show when a worker has claimed a job, how long that claim remains valid, and whether the job returned to the queue after a failure. That history belongs in the [work card for persistent AI](/blog/2026/10/11/persistent-ai-needs-a-shift-handoff/), especially when a run survives a shift or session.

## Fairness needs an explicit rule

A single customer can fill a shared queue with large jobs and make every small request wait behind them. First in, first out sounds neutral. In practice, it can let one batch monopolize the product.

Temporal supports task-queue priorities, fairness keys, weights, and dispatch rate limits. Those controls expose the real choices. Should an interactive task pass a nightly batch? Can one tenant use half the workers? Does a safety review outrank a report that already missed its deadline?

Write the policy down before the backlog appears. Reserve some capacity for short interactive work. Limit in-flight jobs per account. Age waiting tasks so low-priority work does not starve forever. Keep premium priority bounded rather than allowing the richest customer to purchase every lane.

Then explain enough of the rule to users. They do not need the scheduler implementation, but they should know why a task moved, whether changing scope would help, and what service promise applies.

## Test the product at saturation

Most agent demos test an empty queue. That is the easiest possible environment and the least revealing one.

Run the product with workers already full. Submit one large batch, then a small urgent task. Let an account hit its concurrency limit. Lose a worker after it claims a job. Change a job's priority while it waits. Cancel work at the front and the back of the queue.

Measure admission accuracy, estimated-versus-actual start time, queue age by customer, starvation, expired work, duplicate execution, cancellations before compute begins, and completed value per constrained resource. Average latency alone can hide the customer who waited six hours behind somebody else's import.

Also test the refusal copy. “Try again later” exports capacity planning to the customer. A better response says the current plan has reached its three-job limit and the next slot is expected between 2:00 and 2:20 PM. It also explains that reducing the dataset would qualify the job for the faster lane.

Backpressure will not make capacity infinite. It does something more useful: it keeps the product from promising infinite capacity. A trustworthy agent accepts work with a visible place, a bounded claim on resources, and an honest path when the answer is not now.

## Sources

- [Reactive Streams](https://www.reactive-streams.org/)
- [Amazon SQS: Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
- [Temporal: Task Queue Priority and Fairness](https://docs.temporal.io/develop/task-queue-priority-fairness)
