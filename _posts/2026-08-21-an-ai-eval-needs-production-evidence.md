---
layout: post
title: "AI Agent Evals: Your Test Passed. Production Found the Bug."
date: 2026-08-21 10:49:00 -0500
category: AI + Product
description: "AI agent evals are only useful if production failures flow back into the test set. A passing score should start a learning loop, not end one."
read_time: "5 min read"
---

The eval passed.

The customer still found the failure.

That's the uncomfortable part of AI evaluation: a good pre-release test can be completely legitimate and still miss the combination that shows up in production five days later.

A recent VentureBeat survey of 108 enterprise respondents found that 49% said they'd had an AI agent or LLM feature pass internal testing and later cause a customer-visible problem. It's a small, self-selected survey, so I wouldn't call 49% an industry failure rate.

The useful part is the pattern.

The test said yes. Production found something the test didn't.

I've seen the non-AI version of this in robotics. You can validate a system in simulation, on a test route, and against every scenario the team knows to create. Then the real world supplies a combination nobody thought to put in the test set: a GPS reflection in one location, an old hardware revision meeting a new software build, or weather interacting with a sensor in just the wrong way.

The response isn't to declare testing useless.

You bring the miss back into the test system.

## Production should write the next eval

A team usually begins with examples it understands: known good answers, known bad answers, policy cases, tool-use scenarios, and adversarial prompts.

That's necessary. It just shouldn't become a museum collection.

Production traffic is messier. Users omit context. Data changes mid-workflow. Agents retry, branch, call tools, and sometimes alter the state they're reasoning about.

So I'd design an explicit return path:

> pre-release eval → production trace → investigate failure → label the case → add or revise an eval → test the fix

The important part is the return arrow.

LangChain recently released a LangSmith evaluator aimed at flagging "perceived error" in production conversations using signals such as user corrections, repeated requests, rejected actions, contradictions, and unresolved outcomes. I wouldn't hand product judgment to one automated evaluator. What I like is the direction: production behavior is becoming test input instead of merely dashboard exhaust.

## Aggregate scores can hide where the risk moved

Suppose an agent improves from 91% to 94% on an eval suite.

Good news.

Now suppose the remaining failures shifted from awkward wording to occasionally selecting the wrong customer account before taking an action.

The average improved. The product got riskier.

That's why I'd segment eval results by consequence, not only by scenario count. Recommendation versus action matters. Reversible versus irreversible matters. Fresh context versus stale context matters. A common workflow and a rare but expensive edge case shouldn't automatically have equal weight.

This connects directly to [AI agent permissions](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/). The more authority the system has, the more important it becomes to understand *which* failures remain.

"Accuracy is 94%" doesn't tell me what to fix next.

"Most high-severity misses happen after the CRM lookup returns multiple customer accounts" does.

## Watch outcomes, not just the plumbing

Traditional observability still matters. I want latency, retries, API errors, token use, and cost.

Those signals tell me whether the machinery is running.

They don't necessarily tell me whether the agent produced a fluent, fast, wrong answer.

That's a different instrumentation problem.

Corrections, retries, abandoned workflows, rejected actions, escalations, and human review can all help. High-consequence workflows may need explicit sampling and manual adjudication. The mix should depend on what the agent is allowed to do and what a mistake costs.

OpenAI's August Enterprise Signals report points in the same direction on adoption: enterprise use is moving toward more delegated work, with agents receiving more context and tools. As that expands, we'll get more useful production evidence and more ways for a technically successful run to produce a bad outcome.

I'd treat meaningful production misses as potential eval cases. Some will be one-offs. Some will reveal a missing scenario. A few will expose that the test is measuring the wrong thing entirely.

That's not evidence that the eval failed.

It's evidence that the eval still has work to do.

If production found the bug, the test isn't finished until that bug makes the trip back into the eval.

## Sources

- [VentureBeat: 85% of companies burned by an AI mistake are racing to cut the humans who might catch the next one](https://venturebeat.com/data/85-of-companies-burned-by-an-ai-mistake-are-racing-to-cut-the-humans-who-might-catch-the-next-one)
- [LangChain: Introducing LangSmith Tuned Evaluators, starting with Perceived Error](https://www.langchain.com/blog/introducing-langsmith-tuned-evaluators-starting-with-perceived-error)
- [OpenAI: Enterprise Signals, what frontier firms are doing differently](https://openai.com/signals/enterprise-data/)
