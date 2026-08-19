---
layout: post
title: "Build Dashboards Around Exceptions, Not Averages"
date: 2026-06-26 09:20:00 -0500
category: Product + Analytics
description: "Averages summarize the system. Exceptions tell operators where attention is needed now."
read_time: "4 min read"
---

Most dashboards are built to summarize what happened.

Operators usually need something different.

They need to know **where the system is behaving badly enough that somebody should act.**

That distinction sounds small, but it changes the entire design of a dashboard.

## Averages are useful, but they hide the work

Suppose a delivery operation reports:

> Average delivery time: 31 minutes

That number may be useful for leadership. It tells you something about overall performance.

But imagine there were 1,000 deliveries yesterday:

- 850 arrived in less than 30 minutes
- 100 took 30 to 45 minutes
- 40 took 45 to 60 minutes
- 10 took more than an hour

The average can still look healthy while a small group of customers has a very bad experience.

An operator generally does not need to stare at the 850 normal deliveries.

The interesting question is:

**What happened in those 50 unusually slow deliveries?**

## Turn the dashboard into a queue

A useful operational dashboard often behaves more like a prioritized work queue than a report.

Instead of showing:

> Average delivery time: 31 minutes

show something like:

> 50 deliveries exceeded 45 minutes

Then break those exceptions down:

- 19 capacity constraints
- 13 routing failures
- 8 equipment problems
- 6 customer-access problems
- 4 unknown

Now the dashboard is pointing directly at work.

The 19 capacity-related failures might trigger a staffing or fleet decision.

The 13 routing failures might trigger a route-quality review.

The four unknown cases might be especially valuable because they expose a gap in your telemetry or categorization.

## Define normal before looking for abnormal

Exception-driven dashboards require an explicit definition of normal.

That could be:

- a threshold
- a service-level target
- a statistical range
- a comparison with a historical baseline
- a difference from a peer group

For example, if a machine normally operates between 68°C and 74°C, a dashboard that continuously plots temperatures inside that range may not be especially useful.

Instead, surface:

> 7 machines exceeded 74°C for more than 10 minutes today

Then rank them by severity and duration.

The underlying data is the same. The presentation is different because the dashboard is optimized for decisions rather than observation.

## Exceptions need context

An exception by itself is not enough.

For each exception, try to give the user enough context to answer three questions:

1. **How bad is it?**
2. **Why might it be happening?**
3. **What should I do next?**

A good exception card might therefore include:

- current value
- expected range
- duration
- trend
- likely contributing factors
- owner
- recommended next action

You do not need all of those fields for every problem. But the closer the dashboard gets to answering those questions, the more operational value it creates.

## The dashboard should get quieter when things are working

There is a useful design test here:

> If everything is operating normally, should this dashboard become boring?

For many operational systems, the answer should be yes.

A quiet dashboard means the system is inside expected bounds.

Attention should become more concentrated as abnormal behavior appears.

That is very different from a dashboard whose goal is to fill every square inch with charts.

The best operational dashboard is often not the one that shows the most information.

**It is the one that makes the next abnormal thing difficult to miss.**
