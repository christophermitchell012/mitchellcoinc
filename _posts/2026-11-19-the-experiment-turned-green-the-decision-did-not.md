---
layout: post
title: "The Experiment Turned Green. The Decision Did Not."
date: 2026-11-19 10:48:56 -0600
category: Product Analytics
description: "A practical guide to product experiment stop rules, decision thresholds, guardrails, and the evidence product teams need before shipping a result."
read_time: 6 min
---

The conversion chart turned green on Tuesday afternoon. Someone pasted it into Slack with three rocket emojis. By Wednesday morning, the estimate had drifted back toward zero.

Nothing about the customers had changed overnight. The team had simply stopped looking at one convenient moment and resumed at another. That is a weak basis for deciding what to ship.

An experiment is not a slot machine that pays out a decision when the line changes color. It is a controlled way to reduce uncertainty around a choice. That choice, along with the evidence required to make it, belongs in the plan before the first customer enters the test.

## Choose the decision before the result

A clean experiment brief starts with a proposed action. It might say that the team will roll a new checkout flow to all eligible customers if the test produces a meaningful lift without exceeding its payment-error guardrail. That is more useful than a vague promise to “learn what works.”

The brief should name five things:

- The eligible population and assignment unit.
- The primary decision metric and its exact definition.
- The smallest effect that would matter to the business or customer.
- The guardrails that can block a rollout.
- The actions attached to positive, negative, and inconclusive results.

This is where a metric becomes operational. As we argued in [Product KPIs and the decisions they change](/blog/2026/08/19/the-best-kpi-is-the-one-that-changes-a-decision/), a number earns its place by changing an action. An experiment metric should meet the same test.

Without a meaningful-effect threshold, a large sample can turn a trivial movement into a statistical victory. Without a guardrail, the team can improve conversion while creating more refunds, support contacts, or failed payments. Without defined actions, every result becomes an invitation to negotiate.

## The stop rule is a product requirement

Teams often treat duration as an analytics detail. It is part of the product requirement because it shapes which version customers receive.

A fixed-horizon test sets its sample or duration in advance and evaluates the result at that point. A sequential design uses a method built for repeated looks and defines its decision boundaries ahead of time. Both can be sound. Repeatedly checking an ordinary fixed-horizon test and stopping on the first favorable result is not sound.

That habit creates **green-flash bias**. The team remembers the brief interval when the dashboard supported its preferred answer and forgets the many intervals when it did not.

The stop rule also needs product context. A checkout test should usually cover the weekday and weekend behavior that matters to that business. A notification change may need time for novelty to fade. A low-frequency purchase can require a sample target that no tidy seven-day calendar can provide.

Pick the rule, write it down, and resist the urge to improvise after seeing the line.

## A statistical win can still be a product loss

The primary metric gets priority because the team chose it before the result. It does not get sovereign power.

Suppose a new trial flow raises starts by 2.1 percent. That sounds promising. If paid conversion is flat, cancellations rise, and support volume jumps, the product has probably made curiosity easier rather than value clearer. The headline metric moved, but the customer outcome did not improve enough to justify the cost.

Good review separates statistical evidence from product judgment. The team should inspect the estimated effect and its uncertainty, then compare both with the predeclared meaningful threshold. It should review guardrails, implementation health, and important customer segments. Segment findings deserve caution because slicing creates more chances to mistake noise for a story.

The decision can then take one of four forms:

- Ship because the effect is meaningful and guardrails remain healthy.
- Extend because the planned method allows it and uncertainty remains material.
- Narrow because a credible, preplanned population responds differently.
- Stop because the effect is too small, harmful, or too costly to pursue.

“Inconclusive” is a valid result. It is better than pretending a small uncertain lift has earned a permanent place in the product.

## Make the result durable

Six months later, the dashboard screenshot will be nearly useless. The durable artifact is an experiment receipt that another person can audit without reconstructing the project from chat messages.

Keep the hypothesis, owner, product version, assignment logic, dates, sample size, exclusions, metric definitions, stop rule, estimates, uncertainty intervals, guardrail results, planned segment views, final decision, rollout plan, and rollback condition together. Record negative and null results too. They prevent the next team from paying for the same lesson.

Infrastructure matters here, but software alone will not create discipline. Teams also need shared definitions, review habits, and enough statistical education to understand what the interface is showing. A fast experiment platform can produce weak decisions at impressive speed if the surrounding process is careless.

The real finish line is not a green dashboard. It is a decision that remains defensible after the excitement has worn off and the next person asks why the product changed.

## Sources

- [Continuous Monitoring of A/B Tests without Pain: Optional Stopping in Bayesian Testing](https://www.microsoft.com/en-us/research/publication/continuous-monitoring-of-a-b-tests-without-pain-optional-stopping-in-bayesian-testing/), Microsoft Research.
- [Overlapping Experiment Infrastructure: More, Better, Faster Experimentation](https://research.google/pubs/overlapping-experiment-infrastructure-more-better-faster-experimentation/), Google Research.
- [Building confidence in a decision](https://netflixtechblog.com/building-confidence-in-a-decision-8705834e6fd8), Netflix TechBlog.
