---
layout: post
title: "Product KPIs: If the Number Moves, What Changes?"
date: 2026-08-19 12:58:00 -0500
category: Product + Analytics
description: "Product KPIs should narrow a decision or action when they move. If nobody changes what they do, the metric may be reporting rather than a KPI."
read_time: "4 min read"
---

A dashboard can hold fifty metrics.

An operator can still make one decision at a time.

I've spent a lot of time around dashboards, both as a product manager and as the person trying to figure out why an operational system is misbehaving. The charts usually aren't the hard part.

The hard part is deciding which numbers deserve attention.

A fleet can track completion rate, latency, localization health, battery telemetry, route performance, support volume, and another dozen signals. That's useful for understanding the system.

It's less useful at 2:15 in the afternoon when performance suddenly drops and somebody has to decide what to investigate first.

That's the test I care about for a KPI:

**If the number moves, what changes?**

## Start with the decision, not the chart

In robotics and fleet operations, several different failures can push the same top-line KPI in the wrong direction. Localization trouble can reduce completed missions. So can routing. So can hardware.

If the dashboard only tells me completion fell, I still have most of the diagnostic work ahead of me.

What I want is context that narrows the next move:

- Which failure types increased?
- How many units are affected?
- Is the problem concentrated by location, software version, or operating condition?
- Who owns the next investigation?

At Refraction AI, some of the most useful observability work wasn't adding more charts. It was making abnormal behavior easier to separate from normal fleet noise.

That's a product problem as much as an analytics problem.

## I like metrics with an implied verb

One quick test is to put a verb after the number.

If route failures rise, **inspect** the affected routes.

If localization confidence degrades, **compare** sensor and positioning data.

If customer-facing status errors increase, **trace** the event path that generates those updates.

The action changes by system, but the metric should at least narrow the next move.

A number that only produces "well, that looks bad" isn't finished yet.

This doesn't mean every metric needs an alert, owner, and runbook. Some numbers are there for trend analysis. Some belong in a weekly review. Some are diagnostic signals you only open after something else fires.

The mistake is treating all of them as equally important because they happen to fit on the same screen.

I'd rather have five metrics that reliably produce good decisions than fifty that produce the appearance of visibility.

That connects directly to [operational metrics with explicit owners and thresholds](/blog/2026/08/02/every-operational-metric-needs-an-owner-threshold-and-action/) and to [exception-first dashboards](/blog/2026/06/26/build-dashboards-around-exceptions-not-averages/). The common thread is attention: surface what matters, then make the next decision cheaper.

**The product question:** If this changes materially tomorrow, who will care and what will they do differently?

If there's a clear answer, keep the KPI prominent. If there isn't, the number may still be useful data.

If the number moves and nothing changes, it's probably useful reporting. It just isn't the KPI you thought it was.

## Sources

- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
