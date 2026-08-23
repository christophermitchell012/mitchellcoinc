---
layout: post
title: "AI Agent Permissions: How Much Authority Is Too Much?"
date: 2026-08-20 10:46:00 -0500
category: AI + Product
description: "AI agent permissions should expand with evidence, reversibility, and blast radius. Capability alone is not a reason to grant more authority."
read_time: "5 min read"
---

Giving an AI agent another tool isn't just an engineering change.

It changes what a mistake can become.

A support copilot that reads account history and drafts a response can be wrong while still giving a person a chance to catch it. Give the same system permission to issue a refund, change an entitlement, or send the response automatically, and you've changed the product even if the model and interface stay exactly the same.

That's why I think AI agent permissions belong in product requirements, not only in a security review.

Recent enterprise security news is moving in the same direction. Fortinet acquired Virtue AI, whose technology includes runtime protection and validation for autonomous agents. Info-Tech Research Group has warned that many organizations are moving agentic systems into enterprise workflows while still carrying architecture designed for pilots. CIO Dive recently reported that only 35% of executives in an HFS Research/TCS survey said AI consistently delivers intended outcomes while remaining controllable and trusted.

Those are security and governance signals, but the product question underneath them is simpler:

**What is this agent allowed to do when nobody is watching?**

## Capability and authority should move at different speeds

I've worked around remote operations and automated systems where the system could technically perform an operation before I was comfortable removing the fallback path.

Software agents deserve the same skepticism.

Reading telemetry is different from restarting a service. Reading a Jira ticket is different from closing it. Recommending a configuration change is different from pushing it to production.

A single toggle labeled "agent enabled" is doing a lot of work there.

I'd make the authority levels explicit.

For a consequential workflow, a simple progression might be:

1. **Observe:** retrieve context and explain what it sees.
2. **Recommend:** propose an action but cannot execute it.
3. **Act with approval:** prepare the action and wait for confirmation.
4. **Act inside limits:** execute a bounded class of reversible actions.
5. **Act autonomously:** operate without approval inside a defined scope.

The ladder isn't universal. A low-risk internal workflow may move faster. A safety, financial, or customer-facing workflow may never need the last step.

The useful product decision is what evidence earns the next level.

## Reversibility changes the amount of autonomy I can tolerate

An agent incorrectly tagging an internal record is inconvenient.

An agent deleting customer data, moving money, or changing production configuration is a different species of mistake.

So I put reversibility beside confidence when deciding how much autonomy to allow.

That can create slightly awkward boundaries, and I'm fine with that. Maybe the agent can automatically route a support case but needs approval to close it. Maybe it can generate a deployment plan but can't execute it. Maybe it can restart one unhealthy edge device but must escalate when the same symptom appears across twenty devices.

Those boundaries aren't proof that the product is unfinished.

They're part of the product.

## Permission design should include failure behavior

Once an agent can act, I want acceptance criteria around authority, not just task completion.

How often does it choose the wrong tool? Does it request actions outside its scope? What happens when context is stale? What happens after an API fails halfway through a multi-step task? Can an operator reconstruct what the agent actually did?

This extends the [workflow-boundary problem I wrote about earlier](/blog/2026/07/05/ai-prototypes-fail-at-the-workflow-boundary/). Context tells the agent what it knows. Permissions determine what a mistake can become.

I'd also instrument denied actions and approval overrides. If humans constantly approve one class of action, maybe the boundary is too conservative. If they frequently reject another, the agent hasn't earned more room yet.

That gives the team evidence instead of vibes.

**The product question:** What evidence would make us comfortable moving this action one level higher?

As agents improve, the temptation will be to keep expanding their authority. Sometimes that's exactly right.

But authority becomes too much when the blast radius grows faster than the evidence that the agent has earned it.

## Sources

- [Fortinet: "Fortinet Advances Continuous AI Protection with the Acquisition of Virtue AI" (GlobeNewswire via Yahoo Finance)](https://finance.yahoo.com/technology/ai/articles/fortinet-advances-continuous-ai-protection-130000226.html)
- [Info-Tech Research Group: "Pilot-Era Agentic AI Stacks Expose Enterprises to Integration and Governance Risks" (PR Newswire)](https://www.prnewswire.com/news-releases/pilot-era-agentic-ai-stacks-expose-enterprises-to-integration-and-governance-risks-finds-info-tech-research-group-302855642.html)
- [CIO Dive: "Executives put the spotlight on AI's reliability issue"](https://www.ciodive.com/news/executives-spotlight-ai-reliability-issue/828075/)
