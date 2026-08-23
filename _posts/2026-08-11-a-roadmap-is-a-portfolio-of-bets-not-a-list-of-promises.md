---
layout: post
title: "Product Roadmaps: Plan, Promise, or Portfolio of Bets?"
date: 2026-08-11 16:05:00 -0500
category: Product
description: "Product roadmaps work better when they distinguish commitments from uncertain bets and show what evidence could change the plan."
read_time: "4 min read"
---

Every rectangle on a roadmap looks equally confident.

They rarely are.

A known infrastructure migration may have clear scope, dependencies, and a date another team genuinely depends on. A new AI workflow may still be asking whether users trust the output enough to act on it.

Put both on the same quarterly slide and uncertainty has a funny way of turning into a promise.

That's why I think a useful product roadmap should show what kind of commitment each item actually represents.

Some items are plans. Some are promises. Some are bets.

Pretending they're the same makes the roadmap look cleaner and the decisions worse.

## Commitment and confidence aren't the same thing

A team can be highly committed to solving a problem and still have low confidence in the current solution.

That's normal in 0-to-1 work.

If customers struggle with onboarding, I may be confident the problem is real but uncertain whether guided setup, better diagnostics, services, or a different integration strategy will fix it.

I don't want the roadmap to force the team to pretend that uncertainty is gone.

I'd rather frame the item around the problem and the next evidence we need.

For example:

> Reduce failed first-time integrations. Test whether automatic connection diagnostics remove the two most common setup failures in support cases.

Engineering and design have something concrete to work on, but the first idea hasn't quietly become a permanent promise.

## Some roadmap milestones should be evidence, not features

A fixed customer commitment may need a real delivery date. No argument there.

Exploratory work often needs a different kind of milestone:

> By the end of the month, determine whether pilot users can complete the workflow with acceptable accuracy without increasing operator time.

That's still a commitment.

It's a commitment to produce evidence.

I've found that distinction useful whenever technical feasibility and product value are tangled together. A model can work and still fail the workflow. An integration can look promising until the customer can't reliably provide the required data. A feature can test well in interviews and still add too much operational cost.

Those aren't planning failures. They're exactly the uncertainties the plan should expose.

## Protect the outcome more than the noun

Stakeholders remember nouns remarkably well: dashboard, API, PDF report, AI assistant.

The underlying need is usually closer to a verb: understand, reduce, detect, automate, decide.

If discovery shows that a Monday morning exception email solves the problem better than the "reporting dashboard" on the roadmap, I'd rather make that change than defend the rectangle.

There are exceptions. Compliance deliverables, contractual commitments, and platform dependencies can make the implementation itself part of the promise.

But when the goal is an outcome, the roadmap should leave room for the solution to improve as the team learns.

I usually want to answer three questions when I look at a roadmap item:

- What are we trying to change?
- How confident are we in this approach?
- What evidence would make us change direction?

That gives stakeholders more useful information than a quarter printed beside a feature name.

It also makes roadmap conversations less theatrical. Nobody has to pretend a discovery bet has the same certainty as a committed migration.

A good roadmap can contain all three kinds of work. It just shouldn't disguise one as another.

The roadmap is most useful when everyone can see which items are plans, which are promises, and which are still bets.

## Sources

- [Silicon Valley Product Group: Changing How You Decide Which Problems To Solve](https://www.svpg.com/changing-how-you-decide-which-problems-to-solve/)
- [Silicon Valley Product Group: Product Roadmaps](https://www.svpg.com/product-roadmaps/)
