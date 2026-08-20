---
layout: post
title: "AI Agent Permissions Are a Product Decision"
date: 2026-08-20 10:46:00 -0500
category: AI + Product
description: "As AI agents move from recommending work to taking actions, permission design becomes part of the product contract, not just a security setting."
read_time: "5 min read"
---

I've been watching the conversation around AI agents move in a useful direction this week. Less attention is going to whether an agent can complete an impressive demo, and more is going to what happens when we give it credentials and let it touch real systems.

On August 17, Fortinet announced that it acquired Virtue AI, whose technology includes runtime protection, automated validation and monitoring of autonomous agents. Two days later, Info-Tech Research Group published guidance arguing that agentic systems are moving into enterprise workflows while many organizations are still carrying architecture designed for pilots. CIO Dive also reported this week that only 35% of executives in an HFS Research/TCS survey said AI consistently delivers intended outcomes while remaining controllable and trusted.

I don't read those as three separate security stories. I read them as a product signal.

The interesting question is becoming: **what is this agent allowed to do when nobody is watching it?**

## Read access and action access are different products

A support copilot that reads account history and drafts a response can be wrong and still give the user a chance to catch the mistake.

Give the same system permission to issue a refund, change an account entitlement or send the response automatically and you've changed the product substantially, even if the model and user interface are identical.

The same thing happens in technical workflows. An agent that can inspect telemetry is different from one that can restart a service. Reading a Jira ticket is different from closing it. Recommending a configuration change is different from pushing it.

I think product requirements need to represent those differences explicitly.

When I've worked with remote operations and automated systems, I've generally wanted the authority of the system to increase more slowly than its capability. A robot may technically be able to perform an operation before I'm comfortable removing the fallback path. Software agents deserve the same skepticism.

## I would design an authority ladder

For a consequential workflow, I'd rather start with a few deliberate levels than a single "agent enabled" switch.

A useful progression might be:

1. **Observe:** retrieve context and explain what it sees.
2. **Recommend:** propose an action but cannot execute it.
3. **Act with approval:** prepare the action and wait for a human confirmation.
4. **Act inside limits:** execute a defined class of reversible, bounded actions.
5. **Act autonomously:** operate without approval inside an explicitly defined scope.

That ladder isn't universal. A low-risk internal workflow may skip steps. A safety, financial or customer-facing workflow may never need level five.

The product decision is where to put the boundary and what evidence is required to move it.

This is where evaluation gets more interesting than a benchmark score. I want to know how often the agent chooses the wrong tool, whether it requests an action outside its scope, how it behaves with stale context, what happens after an API failure, and whether the operator can tell what it actually did.

Those are product acceptance criteria.

## Reversibility buys a lot of freedom

I also care about whether an action can be undone.

If an agent labels an internal record incorrectly, recovery may be cheap. If it deletes customer data, sends money or changes a production configuration, the same error rate has a completely different meaning.

So I'd put reversibility beside confidence when deciding how much autonomy to allow.

That can lead to slightly awkward product behavior, and I'm fine with that. Maybe an agent can automatically tag and route a support case but needs approval to close it. Maybe it can generate a deployment plan but can't execute against production. Maybe it can restart one unhealthy edge device but has to escalate when the same symptom appears across twenty devices.

Those boundaries are not evidence that the AI product is unfinished. They're part of the product.

## This extends the workflow argument

I wrote recently that AI prototypes often fail at the workflow boundary because the model is only one box in a larger system. Permissions are one of those boundaries, but they deserve special attention once the agent can take action.

Context tells the agent what it knows. Permissions determine what a mistake can become.

That's why I wouldn't treat agent permissions as a security review that happens after product design. Product, engineering, security and operations should decide the authority model together, then instrument it well enough to learn whether the boundary is in the right place.

As agents get better, the temptation will be to keep moving that boundary outward. Sometimes that's exactly the right move.

I just want the decision to be based on observed behavior, blast radius and recovery cost, not on how good the last demo looked.

### Sources

- Fortinet, "Fortinet Advances Continuous AI Protection with the Acquisition of Virtue AI," August 17, 2026.
- Info-Tech Research Group, "Pilot-Era Agentic AI Stacks Expose Enterprises to Integration and Governance Risks," August 19, 2026.
- CIO Dive, "Executives put the spotlight on AI's reliability issue," August 17, 2026.
