---
layout: post
title: "Multi-Agent AI Needs a Delegation Budget"
date: 2026-10-23 10:40:49 -0500
category: "Product Strategy"
description: "Multi-agent AI can improve difficult work, but every handoff adds cost and uncertainty. Set a delegation budget tied to measurable outcome gains."
read_time: "5 min"
---

A second AI agent is easy to add. A reason to keep it is harder.

Product teams often treat multi-agent architecture as a capability upgrade. One agent plans, another researches, a third critiques, and a fourth assembles the answer. The diagram looks sophisticated. Costs grow. Latency stretches. Sometimes the result barely changes.

The useful product question is not whether agents can collaborate. It is whether one more delegation creates enough outcome value to pay for another model call, another context transfer, and another place where work can drift.

That calls for a delegation budget.

## Start with the single-agent baseline

OpenAI advises teams to let evaluations drive the move to multiple agents. Starting with several agents can add complexity and slow the route to production. That is a sound product constraint because a single-agent baseline makes marginal value visible.

Run representative tasks through the simplest workable system first. Record success rate, completion time, token cost, tool errors, and review effort. Then add one specialist or one critique pass. Repeat the same evaluation set.

The difference matters more than the new system's absolute score. A three-point quality gain may justify a large cost increase for a legal review. It may be wasteful for support-ticket classification. Architecture has to inherit the economics of the job.

This is why an [AI outcome ledger](/blog/2026/10/13/ai-spend-needs-an-outcome-ledger/) belongs beside the agent graph. It connects orchestration choices to customer or operating value instead of counting activity as progress.

## Budget delegations by uncertainty

Not every request deserves the same team of agents. A delegation budget sets the maximum effort available before the run begins, then releases that effort only when the task shows enough uncertainty.

Useful release signals include independent research branches, evidence conflicts, low confidence, tool failure, or a high-cost decision. A routine lookup should stay with one agent. Broad market studies may earn several parallel researchers. A consequential recommendation may earn a separate critic after the evidence is assembled.

Anthropic reported that its multi-agent research system used about 15 times the tokens of ordinary chat interactions. It also beat a single-agent research configuration by 90.2 percent on an internal evaluation. Both numbers matter. That improvement came from a workload with substantial parallel search. More agents alone were not the cause.

Call the gap between the agents launched and the agents that changed the answer the coordination tax. The tax includes duplicated searches, repeated context, wait time, contradictory outputs, and human time spent untangling them. It is invisible if the dashboard reports only final quality.

## Make every handoff earn its place

A handoff needs a narrow purpose, an input contract, and a return format. “Review this” is not a useful delegation. “Find unsupported quantitative claims and return claim, evidence gap, and source needed” is testable.

Google's Agent Development Kit supports both predictable workflow agents and dynamic delegation. That choice should be exposed as product policy. Stable tasks can use a fixed path. Variable tasks can allow the lead agent to route work, but within limits for agent count, tool calls, elapsed time, and spend.

Instrument each handoff with four fields:

- why the delegation occurred
- what evidence or artifact returned
- how the result changed the final output
- what the delegation cost in time and tokens

Those fields create a delegation receipt. Receipts expose specialists that rarely contribute and critics that catch expensive defects. They also expose routing rules that fire too often.

## Define the stopping rule before launch

Multi-agent systems can keep discovering more work. Product policy has to decide when enough is enough.

Set an exit rule around outcome saturation. Stop when new agents repeat known evidence. Stop when the score improvement falls below a threshold or remaining uncertainty does not affect the decision. Escalate to a person when agents disagree on a material claim or when the next action changes persistent state.

The product promise is not “a team of AI agents.” The promise is a better result at a defensible cost and speed. A delegation budget keeps the architecture subordinate to that promise.

## Sources

- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system)
- [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Google Cloud: Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk)
