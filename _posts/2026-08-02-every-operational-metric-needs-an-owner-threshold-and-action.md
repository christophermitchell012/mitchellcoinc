---
layout: post
title: "For an Operational Metric, Define the Owner, Threshold, and First Move"
date: 2026-08-02 11:35:00 -0500
category: Product + Analytics
description: "When a metric is intended to drive an operational response, define who responds, what abnormal means, and what happens first."
read_time: "4 min read"
---

I've worked on autonomous robots, energy systems, analytical instruments and software platforms. They all have one thing in common: once the instrumentation gets good, it's very easy to create more metrics than anyone can realistically pay attention to.

The dashboard isn't the scarce resource. Attention is.

So for the small set of metrics that are actually supposed to drive an operational response, I want three things to be pretty clear: who owns the response, what abnormal means, and what the first move should be.

That sounds obvious. In practice, teams often discover those answers in the middle of the incident, which is exactly when you don't want to be figuring them out.

## "Engineering owns it" usually isn't enough

Suppose a fleet starts showing a higher rate of localization failures.

Who actually takes the first look?

Autonomy? Fleet operations? The engineer responsible for sensor fusion? Whoever pushed the latest build?

The right answer depends on the organization, and it can change as the product matures. What matters is that the people dealing with the problem don't have to reconstruct the org chart while the system is misbehaving.

Ownership isn't blame. It's just the role responsible for making sure the signal turns into a response.

## Thresholds need context, not just a number

I'm suspicious of thresholds that are simply "above X is bad."

A CPU spike for three seconds is different from the same value for twenty minutes. One failed delivery is different from twenty failures clustered in the same neighborhood. A sensor dropout on a parked system may be irrelevant and critical while the system is moving.

So I tend to think about the condition as some combination of:

> value + duration + operating context + impact

That's much closer to how people reason about real systems.

It also cuts down on noisy alerts. Once operators stop trusting alerts, you're in a bad place because the monitoring system starts becoming background decoration.

## Make the first investigation cheap

A runbook doesn't need to be enormous. Often I only care that the first useful step is obvious.

That might be:

- compare affected units with the latest deployment
- check whether the problem is geographic
- inspect the largest contributing error category
- verify whether an upstream dependency changed
- pull the raw telemetry for one of the first affected events

The point is to remove the dead time before useful investigation begins.

I don't operationalize every metric this way. Weekly trends don't need paging rules. Product adoption metrics don't need an on-call engineer. Plenty of numbers are there simply to help a team understand what changed over time.

But if a metric is supposed to cause a near-term response, I want the operating contract to be obvious.

Who notices it? Under what condition? What happens first?

If those answers are still fuzzy, I treat the metric as reporting until the team proves otherwise.
