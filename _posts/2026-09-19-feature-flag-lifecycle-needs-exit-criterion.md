---
layout: post
title: "Feature Flag Lifecycle Needs an Exit Criterion"
date: 2026-09-19 10:08:00 -0500
category: "Experimentation + Product Strategy"
description: "Feature flags need an exit criterion. Tie each flag to a product decision, live rollout state, an owner, and a defined retirement event."
read_time: "4 min read"
---

A feature flag is temporary infrastructure with a surprisingly good chance of becoming permanent furniture.

DoorDash recently described the scale of that problem: more than 60,000 feature flags across roughly 623 repositories, with about 2,300 new flags created each month and more than 1,000 already stale before anyone schedules the work to remove them again. DoorDash defines stale with four conditions, including 90 days without modification.

Those numbers turn cleanup from developer tidiness into a product-lifecycle problem, one that accumulates quietly while everybody is busy shipping the next thing.

> “Every flag has a lifecycle.” — DoorDash Engineering

Flags are cheap when they enter. A product manager wants a controlled rollout, an experiment needs variants, or engineering wants a kill switch, so somebody creates one. The carrying cost arrives later, after the decision the flag supported has already been made.

A stale flag leaves conditional logic behind. DoorDash notes that even a simple Boolean flag can touch five to 20 files once wrappers, call sites, constants, and tests are counted. Now imagine debugging an incident while old branches preserve behaviors nobody intends to use again.

This is where I think experimentation platforms need an explicit exit criterion alongside the launch criterion, because [MVPs should remove uncertainty rather than maximize features](/blog/2026/07/18/an-mvp-should-remove-uncertainty-not-maximize-features/).

When a flag is created, its metadata should say what decision it supports, who owns that decision, and what event makes the flag removable. For an A/B test, that might be choosing a winner or abandoning both variants. For a rollout flag, 100% deployment isn't quite enough; the product also needs a defined soak period and confidence that rollback no longer requires the old branch.

Otherwise, “temporary” becomes a storage class, which is a wonderfully product-manager-y way to accumulate code nobody quite owns.

I like DoorDash's approach because the automation doesn't infer the winning behavior from source code alone. Its cleanup system queries the live experimentation platform for rollout percentage and target value, then asks an engineer to confirm ambiguous cases before code changes begin. A flag sitting at 60% rollout, for example, isn't silently converted into either branch.

That distinction is product judgment embedded in infrastructure: code tells you what paths exist, while rollout state tells you which path customers are actually on.

The economics are also unusually concrete. Across 50 recent stale flags, DoorDash reported 45 usable pull requests, averaging 13.8 minutes and $4.79 per cleanup, versus an estimated one to two hours manually. Thirty-one landed on the first attempt, while five required engineer intervention.

The obvious failure mode is treating automated cleanup as permission to create flags forever. Faster garbage collection doesn't make garbage free, especially when each flag adds another state that testing, support, and incident response may encounter.

I'd put flag retirement directly into experiment design reviews and release checklists, because creation should open a clock and a completed product decision should start closing it.

Feature flags are useful because they let teams postpone commitment while evidence arrives. Once the evidence has arrived and the decision is made, the flag has finished its product job; leaving it in the code is just indecision with an API.

## Sources

- [DoorDash Engineering: Automating Feature-Flag Cleanup at Scale with a Multi-Agent LLM System](https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/)
- [InfoQ: DoorDash Uses Multi Agent LLMs to Clean up 60,000 Feature Flags](https://www.infoq.com/news/2026/09/doordash-feature-flag-cleanup/)
