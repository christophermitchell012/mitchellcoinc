---
layout: post
title: "Observability Needs a Sampling Budget"
date: 2026-10-25 10:47:02 -0500
category: "Product Strategy"
description: "Telemetry volume is not observability. Build a sampling budget that protects rare failures, controls cardinality, and ties retention to decisions."
read_time: "5 min"
---

Telemetry feels free right up to the invoice, the slow query, or the incident nobody can reconstruct.

Teams often respond by collecting everything first and promising to optimize later, which turns a product decision into an infrastructure accident. Every trace, metric label, and log field earns storage without proving that it helps someone detect, explain, or fix a problem.

Observability needs a sampling budget.

A sampling budget defines which signals deserve full fidelity, which can be summarized, and which can be dropped while it reserves capacity for events that are rare but expensive to miss. The point is not simply to reduce telemetry cost but to buy enough evidence for the decisions the product must support.

## Collection is already a product policy

Sampling changes what a team can know after an event. OpenTelemetry makes the tradeoff visible in tracing because head sampling decides early and efficiently but cannot inspect the completed trace. Tail sampling waits for more context, which allows policies that retain errors, slow requests, or traces with selected attributes.

Neither approach is automatically correct. A high-volume health-check path may deserve a tiny rate, while payment failures get complete retention and newly deployed services receive temporary over-sampling until their behavior is understood.

The product question is not what percentage to keep. It is which future decisions become impossible when evidence disappears. That distinction gives engineering, support, security, and finance a shared basis for choosing.

## Budget by decision, not by signal type

Start with the decisions that telemetry must support. A practical budget can separate four classes:

- immediate detection for signals that trigger an alert or automated response.
- investigation evidence for incidents that require reconstruction.
- trend evidence that supports capacity, reliability, and product plans.
- exploratory data with no committed operational use yet.

Each class can have a different resolution, retention period, label policy, and rules for sampling. Immediate detection may need fast metrics but little historical detail, while reconstruction may need complete traces around a failure window. Trend analysis can often use aggregates, and exploratory data should receive an explicit expiration date.

This is similar to building [dashboards around exceptions](/blog/2026/06/26/build-dashboards-around-exceptions-not-averages/). The scarce resource is not the number of charts but attention. A sampling budget extends that idea backward into the data pipeline, before unused detail becomes a permanent bill.

Amazon CloudWatch shows how resolution affects both usefulness and cost. Standard metrics use one-minute granularity, while high-resolution custom metrics can store data at one-second granularity. AWS also notes that more frequent custom-metric calls can increase charges. A one-second metric should therefore have a one-second decision attached to it.

## Protect rare paths from averages

Uniform sampling is easy to explain and easy to misuse because it treats routine success and unusual failure as if they carry equal information. At a five-percent rate, a common request remains visible while a rare failure mode may vanish for days.

Reserve part of the budget for exceptions by keeping all traces with errors or extreme latency and preserving low-volume services at a higher rate. Increase collection during a release, incident, or customer escalation, then return to the baseline automatically.

Call the missing evidence created by an aggressive policy visibility debt. Like other debt, it may not hurt during normal operation. The cost arrives later, when a team cannot distinguish a one-off complaint from a systemic defect because the relevant detail was discarded.

The budget should track that risk directly. Measure retained error coverage, investigation success rate, time to diagnosis, query latency, active series, ingested bytes, and cost per resolved incident. Raw volume alone says little about whether the retained telemetry is useful.

## Make reductions reversible

Metrics create a different version of the same problem through cardinality. A useful label can multiply into thousands of time series when values vary by customer, container, endpoint, or identifier. More data arrives, but broad queries become slower and more expensive.

Grafana's Adaptive Metrics documentation describes a usage-based approach that analyzes dashboards, alerts, rules, and queries before recommending aggregation for unused or underused series. Teams can review rules, create exemptions, and restore full cardinality for future data if needs change.

That last property matters because sampling and aggregation policies should be reversible without a redesign. Record the owner, reason, effective date, expected savings, protected use cases, and rollback condition for every rule. Recheck the decision after launches, architecture changes, and serious incidents.

Do not reward a team merely for cutting telemetry volume. Instead, reward it for reducing cost while preserving the evidence needed to operate the product. A good sampling budget makes both sides visible: what the system stopped storing and what the business can still decide.

## Sources

- [OpenTelemetry: Sampling](https://opentelemetry.io/docs/concepts/sampling/)
- [Amazon CloudWatch: Metrics concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
- [Grafana Cloud: Adaptive Metrics](https://grafana.com/docs/grafana-cloud/observe-and-act/adaptive-telemetry/adaptive-metrics/)
