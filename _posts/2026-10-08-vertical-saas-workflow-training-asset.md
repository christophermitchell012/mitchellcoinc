---
layout: post
title: "Vertical SaaS: The Workflow Is the Training Asset"
date: 2026-10-08 10:06:10 -0500
category: "AI + Product Strategy"
description: "Vertical SaaS products contain more than data. Their workflows, exceptions, rubrics, and test environments can become valuable AI training assets."
read_time: "4 min read"
---

Vertical SaaS companies have spent years capturing how an industry works.

The forms are the least interesting part.

The real product lives in the approval rules, exceptions, handoffs, permissions, and slightly peculiar definitions of done that accumulate around an important workflow.

OpenAI's new research collaboration with Ironclad makes that asset visible. Ironclad helped turn contracting work into 11 research tasks across legal, commercial, and procurement workflows. Each task had between 8 and 50 grading criteria, and the company supplied hosted product environments where models could practice.

That is more than product integration. The workflow itself has become training and evaluation infrastructure.

## Domain knowledge has to become testable

Most workflow expertise starts as a mixture of configuration, documentation, customer requests, and things an experienced operator knows not to do.

That isn't yet a useful training asset.

OpenAI and Ironclad had to translate the work into concrete tasks: configure an NDA process, build procurement approvals, or make a reusable clause respond correctly to jurisdiction. An experienced user would need an estimated 30 to 40 minutes for an average task.

The detailed rubric matters because success is not one final screenshot. A procurement workflow might need Finance approval above a threshold, Security review for a particular request, Legal review for nonstandard terms, and correct behavior on both sides of every branch.

An agent can complete most of the clicks and still build the wrong process.

That makes the rubric a product artifact. It captures the business rules that the interface alone cannot explain.

## The environment is part of the moat

Data gets most of the attention in AI strategy. Vertical software companies may have another defensible asset: a realistic place where models can perform the work, encounter state changes, and receive granular feedback.

Ironclad provided hosted environments. OpenAI developed synthetic training tasks around representative workflows and used reinforcement learning so the models could improve through practice. On the 11 research tasks, GPT-6 Astra averaged 55.0% against the rubric versus 41.6% for GPT-5.6 Sol. Estimated time per attempt fell from 37.0 to 19.2 minutes.

Those are research results on a small, company-designed evaluation, not proof of customer ROI. Still, the mechanism is worth noticing.

A static corpus can teach terminology and examples. An interactive environment can test whether the system preserved requirements across a long sequence, handled an exception, changed the right state, and left the workflow usable.

The screen is the cheap part. The executable business context is harder to copy.

## Product teams should inventory workflow assets

I would not begin by asking how much customer data a vertical SaaS product can feed into a model. That framing creates obvious privacy problems and misses much of the useful material.

Start with the assets that describe how work should behave:

- configurable rules and decision points
- representative workflow templates
- safe sandbox environments
- expert-reviewed success criteria
- common exceptions and costly failure modes
- production outcomes that can improve the eval

These assets also need governance. Training rights, customer isolation, synthetic-data quality, environment fidelity, and expert-review capacity become product constraints. A workflow copied from one sophisticated customer may be a terrible default for everyone else.

I previously argued that [vertical SaaS should map handoffs before features](/blog/2026/09/15/vertical-saas-map-handoffs-before-features/). The same map can now serve another purpose. Each handoff, rule, and exception is a candidate training task or evaluation criterion.

The strongest vertical AI products may not win because they have the largest pile of documents.

They may win because they can turn how the industry actually works into something a model can practice, measure, and improve.

## Sources

- [OpenAI: Advancing Computer Use with Ironclad](https://openai.com/index/advancing-computer-use-with-ironclad/)
- [OpenAI: How Evals Drive the Next Chapter in AI for Businesses](https://openai.com/index/evals-drive-next-chapter-of-ai/)
- [OpenAI: Measuring Model Performance on Real-World Tasks](https://openai.com/index/gdpval/)
