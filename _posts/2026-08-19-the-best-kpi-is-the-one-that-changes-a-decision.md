---
layout: post
title: "The Best KPI Is the One That Changes a Decision"
date: 2026-08-19 12:58:00 -0500
category: Product + Analytics
description: "If a metric moves and nobody knows what to do next, it is probably reporting rather than an operational KPI."
read_time: "4 min read"
---

I've spent a lot of time around dashboards, both as a product manager and as the person trying to figure out why an operational system is misbehaving.

The charts usually aren't the hard part. It's deciding which numbers actually deserve attention.

A fleet can have completion rate, latency, localization health, battery telemetry, route performance, support volume and another dozen signals. That's useful when you're trying to understand the system as a whole. It's less useful at 2:15 in the afternoon when performance suddenly drops and somebody needs to decide what to investigate first.

That's the distinction I care about: **does the metric change a decision?**

## Start with the person who has to act

In robotics and fleet operations, two very different failures can push the same top-line KPI in the wrong direction. A localization problem may reduce completed missions. So can a routing problem. So can a hardware issue.

If the dashboard only tells me completion fell from yesterday, I still have to do the diagnostic work manually.

What I really want is something closer to:

- Which failures increased?
- How many units are affected?
- Is the problem concentrated in one location, software version or operating condition?
- Has this happened before?
- Who owns the next investigation?

At Refraction AI, some of the most useful observability work wasn't about adding more charts. It was about making abnormal behavior easier to separate from normal fleet noise.

That's as much a product problem as an analytics problem.

## I like metrics with an implied verb

One quick test I use is to put a verb after the metric.

If route failures rise, **inspect** the affected routes.

If localization confidence degrades, **compare** sensor and positioning data.

If customer-facing status errors increase, **trace** the event path that generates those updates.

The action will be different for every system, but the metric should at least narrow the next move. A number that only produces the sentence "that looks bad" isn't finished yet.

I also don't think every number needs an alert, an owner and a runbook. Some metrics are there for trends. Some belong in a weekly product review. Some are useful only after another signal fires.

The mistake is treating all of them as equally important because they happen to fit on the same screen.

I'd rather have five metrics that consistently trigger good decisions than fifty metrics that create the appearance of visibility.

So when I'm defining a KPI, I usually ask one extra question:

**If this changes materially tomorrow, who will care, and what will they do differently?**

If there's a clear answer, keep it prominent. If there isn't, it may still be useful data. I just wouldn't confuse it with an operational KPI.
