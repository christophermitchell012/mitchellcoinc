---
layout: post
title: "AI Agent Approvals Need an Expiration Date"
date: 2026-10-30 10:09:06 -0500
category: Product Strategy
description: "AI agent approvals should expire when their action, context, or risk changes. Bind every decision to exact inputs and require revalidation."
read_time: 5 min
---

A purchasing agent asks for permission to place a $4,800 order. The manager approves it after lunch. By the time the agent resumes that evening, the quantity has changed, the expedited shipping fee has doubled, and a different warehouse is selected.

The system still has an approval. It no longer has the same decision.

Human review is often treated as a permanent green light attached to a workflow. That model is too loose for agents that can pause, retain state, and act later. Approval should be a short-lived product object bound to the exact action a person saw.

## Bind approval to the proposed action

OpenAI's Agents SDK pauses execution when a sensitive tool call needs approval. The pending item includes the tool name, arguments, and call identity, while `RunState` preserves the paused run for later resumption. That makes durable review possible. It also forces the product to define what remains valid when later arrives much later.

The approval record should contain more than a yes. Store the tool identity, normalized arguments, actor, requested time, decision time, policy version, and a hash of the material context shown to the reviewer. The execution service should compare that record with the action it is about to perform.

If the total, destination, recipient, access scope, or target object changed, the old approval should not transfer. The product can explain the difference and request a new decision. Quietly stretching consent across changed inputs creates a stale-consent gap.

This is the approval version of the [authority boundary for AI agents](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/). Permission defines what the agent may request. Approval defines one action the agent may execute under known conditions.

## Give every approval a clock

Some decisions decay faster than others. A draft newsletter may remain safe for a day. A market order, password reset, inventory allocation, or production rollback may be stale within minutes.

Assign a time to live based on the action's volatility and consequence. Do not hide that clock. Show the reviewer when approval expires, and show the agent how much validity remains before it starts expensive preparation.

There is useful precedent outside agent products. OAuth's device authorization flow issues codes that are valid for a limited time and requires an `expires_in` value. When the code expires, the authorization session ends. The system does not reinterpret an old decision as current consent.

Workflow infrastructure also needs explicit limits. AWS Step Functions can pause for a task token while waiting for a human or external process, potentially until the execution reaches its one-year quota. AWS recommends timeout and heartbeat controls so a missing callback does not leave work suspended indefinitely. A durable pause is an implementation capability, not a sensible product default.

Call this the approval half-life: the period during which the original decision remains trustworthy without fresh evidence. It should be short enough to contain drift and long enough to support the real review workflow.

## Revalidate before execution

Expiration alone is not enough. Context can change three seconds after approval.

Add a final validation gate immediately before the side effect. Recalculate prices, permissions, resource versions, policy results, and external availability. Compare them with the approved snapshot. Then choose one of four outcomes:

- execute because the approved action still matches.
- refresh harmless details and record why they do not change the decision.
- request approval again because a material field changed.
- reject execution because the action is no longer allowed.

The distinction between harmless and material change must be explicit. A reformatted address may be harmless. A new recipient is not. A lower price might look harmless, yet it could signal a different product or quantity. Product and risk owners should define those rules together instead of leaving them inside a prompt.

Revalidation should fail closed when the system cannot retrieve current state. An agent that cannot confirm the destination account should not rely on yesterday's screenshot and optimistic momentum.

## Make stale approvals visible

Approval queues need states that people can understand: pending, approved, rejected, expired, superseded, and executed. Approved is not the same as executed. Expired is not an error. Superseded means a newer request replaced the old proposal.

Keep the receipt after any transition. It should show what was proposed, what was approved, what changed, whether execution occurred, and which rule required another review. This helps operators distinguish a cautious product from a broken one.

Test the awkward timing. Approve while inventory changes. Resume after a policy deployment. Modify one argument after review. Let the approval expire during a downstream outage. Submit two versions of the same request and approve the older one last. Measure stale approvals caught, unnecessary reapprovals, execution delay, and side effects attempted with mismatched context.

Human review adds value only when the decision survives intact until execution. A button labeled Approve is not a transferable blessing. It is a bounded agreement about one action, under one visible set of conditions, for a limited time.

## Sources

- [OpenAI Agents SDK: Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [AWS Step Functions: Service integration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html)
- [IETF RFC 8628: OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
