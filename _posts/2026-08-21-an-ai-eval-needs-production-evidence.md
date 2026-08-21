---
layout: post
title: "An AI Eval Needs Production Evidence"
date: 2026-08-21 10:49:00 -0500
category: AI + Product
description: "Pre-release evals are useful gates for AI products, but production behavior has to feed the next eval set if the gate is going to stay useful."
read_time: "5 min read"
---

There's a number from this week's AI news that I keep coming back to. In a VentureBeat survey of 108 enterprise respondents, 49% said they'd had an AI agent or LLM feature pass internal testing and later cause a customer-visible problem. The survey is self-selected and relatively small, so I wouldn't treat 49% as an industry failure rate. VentureBeat doesn't either.

The useful part is the failure pattern: the test said yes, and production later found something the test didn't.

I've seen the non-AI version of this in robotics. You can spend a lot of time validating a system in simulation, on a test route, or against a known set of cases. Then the real world supplies a combination you didn't think to test. A GPS reflection shows up in a particular location. A sensor behaves differently in weather you barely sampled. A failure only appears after a deployment meets an older hardware revision.

You don't respond by declaring testing useless. You bring the failure back into the test system.

AI products need the same habit.

## The eval set should have a return path from production

A team usually starts with examples it already understands: known good answers, known bad answers, policy cases, tool-use scenarios, maybe adversarial prompts. That's reasonable. The trouble starts when the eval set becomes a museum piece.

Production traffic is messier. Users omit context, change their minds halfway through a request, ask two things at once, or interact with data that changed five minutes ago. Agents add another layer because the model may choose tools, retry, branch, or take an action that changes the state of the system.

This week, LangChain released a LangSmith evaluator designed to flag "perceived error" in production conversations. It looks for signals such as user corrections, repeated requests, rejected actions, contradictions, and unresolved outcomes. I wouldn't assume one automated judge can tell you whether a product is good. What interests me is the direction: evaluation is moving closer to live traces instead of ending at the release gate.

For a product team, I'd make that a loop:

> pre-release eval → production trace → investigate failure → label the case → add or revise an eval → test the fix

The important step is the return arrow.

## A passing score can hide where the risk moved

Aggregate eval scores make me nervous when they flatten very different failures into one percentage.

Imagine an agent improves from 91% to 94% on a test suite. That's nice. But suppose the remaining misses shifted from awkward wording to occasionally selecting the wrong customer account before taking an action. The average improved while the product risk got worse.

This connects to the authority question I wrote about yesterday. The more an agent is allowed to do, the more I care about *which* cases fail, not only how many.

I'd segment results by things that change the consequence of an error: action versus recommendation, reversible versus irreversible, known context versus stale context, common workflow versus edge case. For an operational agent, I'd also want to know whether failures cluster around a tool, integration, customer configuration, or model version.

That gives the PM something useful to prioritize. "Accuracy is 94%" doesn't tell me much about the next product decision. "Most of our remaining high-severity misses happen after the CRM lookup returns multiple accounts" does.

## Production monitoring isn't just latency and cost

Traditional observability still matters. I want errors, latency, retries, token use, API failures, and cost. They tell me whether the machinery is working.

They don't necessarily tell me whether the agent gave a fluent, fast, wrong answer.

VentureBeat's July survey makes that distinction visible. Among valid responses to its monitoring question, 26% reported using inline quality assertions, while another 26% focused on transaction traces and 24% mainly tracked gateway metrics such as latency, errors, and cost. Again, it's a directional survey, not a census. But it matches a product problem I've seen in other technical systems: it's easier to instrument what the system *did* than whether what it did was actually useful.

That second question usually needs several signals. Automated evaluators can help triage. Explicit user feedback helps when you can get it. Corrections and retries are often useful implicit signals. High-consequence cases may still deserve human review.

The mix should depend on the workflow.

OpenAI's latest enterprise data points in the same general direction on adoption. Its August 12 Enterprise Signals report says enterprise use is moving from assistance toward delegated work, with agents getting more context and tools. As that happens, product teams are going to have more production behavior to learn from, and more ways for a technically successful run to produce a bad outcome.

I'd treat every meaningful production miss as potential test data. Some will be one-offs. Some will expose a missing scenario. A few will reveal that the eval is measuring the wrong thing entirely.

That's useful information, provided it makes the trip back into the product-development loop.

## Sources

- [VentureBeat: 85% of companies burned by an AI mistake are racing to cut the humans who might catch the next one](https://venturebeat.com/data/85-of-companies-burned-by-an-ai-mistake-are-racing-to-cut-the-humans-who-might-catch-the-next-one)
- [LangChain: Introducing LangSmith Tuned Evaluators, starting with Perceived Error](https://www.langchain.com/blog/introducing-langsmith-tuned-evaluators-starting-with-perceived-error)
- [OpenAI: Enterprise Signals, what frontier firms are doing differently](https://openai.com/signals/enterprise-data/)
