---
layout: post
title: "Operational Metrics: Your Number Moved. Who Acts Next?"
date: 2026-08-02 11:35:00 -0500
category: Product + Analytics
description: "Operational metrics need an owner, a meaningful threshold, and an obvious first action. Otherwise a moving number is only reporting."
read_time: "4 min read"
---

A metric crosses a threshold at 2:15 in the afternoon.

Now what?

I've worked on autonomous robots, energy systems, analytical instruments, and software platforms. Once the instrumentation gets good, all of them can produce more metrics than anyone can realistically watch.

The dashboard isn't the scarce resource.

Attention is.

For the small set of numbers that are supposed to trigger an operational response, I want three things to be obvious before the number moves: who owns the response, what abnormal actually means, and what happens first.

Otherwise the team gets to discover those answers during the incident, which is a strangely popular time to redesign the operating model.

## Ownership should identify the first responder, not assign blame

Suppose a robot fleet suddenly shows a higher rate of localization failures.

Who takes the first look?

Autonomy? Fleet operations? The engineer responsible for sensor fusion? Whoever pushed the latest build?

The right answer depends on the organization, and it may change as the product matures. What matters is that nobody has to reconstruct the org chart while the fleet is misbehaving.

Ownership isn't blame. It's the role accountable for turning the signal into investigation.

That first owner can always pull in somebody else.

## A useful threshold has context

I'm suspicious of thresholds that amount to "above X is bad."

A CPU spike for three seconds is different from the same value for twenty minutes. One failed delivery is different from twenty failures clustered in the same neighborhood. A sensor dropout on a parked system may be irrelevant and critical while the system is moving.

I usually think about an operational condition as some combination of:

> value + duration + context + impact

That's much closer to how operators actually reason.

It also helps with alert fatigue. Once people learn that an alert usually means nothing, you've built an expensive notification generator.

The threshold should narrow attention, not merely create noise.

## Make the first move cheap

A runbook doesn't need to be a small novel.

Often, the most useful thing is simply making the first investigation step obvious.

For a fleet problem, that might mean comparing affected units with the latest deployment, checking whether failures cluster geographically, inspecting the largest error category, or pulling raw telemetry from one of the first incidents.

For a SaaS integration, the first move may be checking dependency health or looking for a configuration change shared by the affected tenants.

The exact action changes. The principle doesn't.

The metric should make the next useful question cheaper to answer.

This connects to the way I think about [exception-first dashboards](/blog/2026/06/26/build-dashboards-around-exceptions-not-averages/). Summary trends tell me whether the system is moving. Exceptions tell me where to look.

And [a KPI should change a decision](/blog/2026/08/19/the-best-kpi-is-the-one-that-changes-a-decision/). An operational metric needs an even tighter contract because somebody may need to act now rather than at next week's review.

I don't operationalize every number this way. Adoption metrics, weekly trends, and diagnostic data can be useful without an owner or paging rule.

But if the metric is supposed to trigger a near-term response, I want the operating contract to be obvious.

**The product question:** If this number crosses its threshold tomorrow, who sees it first and what do they do?

If the number moved and nobody knows who acts next, you don't have an operational metric yet. You have reporting.

## Sources

- [Google SRE: Incident Management Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/)
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
