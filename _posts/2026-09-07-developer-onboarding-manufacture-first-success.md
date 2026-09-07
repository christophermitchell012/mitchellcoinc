---
layout: post
title: "Developer Onboarding Should Manufacture First Success"
date: 2026-09-07 10:00:00 -0500
category: "Developer Experience + Product"
description: "Developer onboarding improves when the product supplies missing test dependencies, letting customers reach useful evidence before real data or hardware arrives."
read_time: "4 min read"
---

A new Kafka cluster has a peculiar onboarding problem: success looks like an empty pipe.

Google Cloud’s September 3 Data Cloud update includes a small feature I like more than several bigger announcements around it. Managed Service for Apache Kafka now has a generally available synthetic data generator that can start sending mock data to a cluster in three clicks and, Google says, in under two minutes.

That sounds like developer convenience, but I think it’s product instrumentation aimed at the customer’s first useful moment.

## Empty states are expensive in infrastructure products

Infrastructure onboarding often ends exactly where the interesting work begins: the resource exists, the console says healthy, and billing has started. Then the customer needs another application, credentials, a schema, test records, and enough knowledge of the system to prove anything actually flows. A provisioned Kafka cluster with no messages is technically successful and experientially unfinished.

Synthetic data changes that boundary before real traffic exists. Instead of making a new user leave the product to manufacture an upstream producer, the platform supplies disposable traffic. Now the customer can inspect a topic, test consumers, exercise monitoring, break something harmlessly, and learn the shape of the system before real production data enters it, without first wiring up a separate producer application or test environment.

That distinction matters because “cluster created” is a weak activation event. Time to first produced record, first successful consumer read, or first observable end-to-end flow says considerably more about whether onboarding worked.

## Build the shortest path to evidence

The product lesson travels beyond Kafka. An API sandbox needs sample requests that return believable responses, while a geospatial product benefits from a ready-made area of interest with enough variation to make exploration useful before the customer uploads anything. An IoT platform should simulate telemetry before hardware arrives. These aren’t tutorials stapled onto the side; they’re temporary substitutes for dependencies the customer doesn’t have yet.

There’s a failure mode here: synthetic data can become demo theater. If the generated traffic is too clean, too small, or structurally unlike production, customers learn the happy path and discover the actual constraints later. The generator should make first success cheap without pretending it proves production readiness.

For Kafka, I’d want the next layer to expose a few deliberate knobs: message rate, payload size, schema choice, malformed-record percentage, burst behavior, and partition skew so developers can push beyond the polite demo stream into something resembling their actual workload. Keep that test surface deliberately small. That turns a welcome mat into a lightweight test harness without trying to become a full load-testing product.

Google’s same weekly update offers a useful contrast for mature workloads. BigQuery continuous queries gained stateful operations such as joins, aggregations, and window functions, while Dataflow added stop-and-replace pipeline updates and drain timeouts. Those are substantial capabilities for established workloads; the Kafka generator attacks an earlier problem because there is no workload yet.

I wrote previously that [an MVP should remove uncertainty rather than maximize features](/blog/2026/07/18/an-mvp-should-remove-uncertainty-not-maximize-features/), and developer onboarding deserves the same treatment. Ask what dependency prevents a new customer from producing evidence that the product works for them, then see whether the product can temporarily supply it.

For an empty Kafka cluster, the first product feature may simply be something worth sending through it.

## Sources

- [Google Cloud: What’s new with Google Data Cloud, September 3, 2026](https://cloud.google.com/blog/products/data-analytics/whats-new-with-google-data-cloud)
- [Google Cloud: Generate synthetic data for Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-synthetic-data)
