---
layout: post
title: "Build vs. Buy: Price the Product Freedom You Lose"
date: 2026-08-31 10:28:00 -0500
category: Product Strategy

description: "Build-vs-buy decisions should price more than engineering cost. A supplier becomes strategic when its constraints start shaping what your product can become."
read_time: "4 min read"
---

## TL;DR

Build-versus-buy decisions get more interesting when a supplier starts constraining a product property customers actually pay for, such as cost, latency, availability, or differentiation. Price the freedom you lose to the dependency alongside engineering cost; ownership deserves another look when supposedly replaceable infrastructure begins acquiring roadmap authority.

A reported $7 billion acquisition can reveal a product decision even when the acquisition doesn't happen.

Reuters reported on August 27 that Anthropic explored buying AI-chip startup MatX for roughly $7 billion before discussions shifted toward a partnership, according to people familiar with the matter. Whether that particular deal closes matters less here. Anthropic considered an enormous commitment to gain more control over compute, a resource sitting underneath nearly every interaction its customers have with the product.

Build-versus-buy discussions often start too low in the stack, with teams comparing engineering cost against vendor price and adding maintenance. The spreadsheet produces a winner. It can miss the variable I care about first: how much product freedom does this dependency consume as the company grows and customer requirements get less forgiving?

## Price the constraint, not just the component

A vendor can be cheaper and still become expensive when its roadmap determines your latency ceiling, unit economics, release timing, geographic availability, or ability to differentiate for paying customers.

AI accelerators make the mechanism unusually visible because hardware choices reach upward into model performance, capacity planning, software tooling, power, cooling, and ultimately the economics of serving a request. Google describes Ironwood as a co-designed system spanning compute, high-bandwidth memory, networking, cooling, and software rather than a chip operating alone. AWS makes an explicitly economic pitch for Trainium2, claiming its instances provide 30–40% better price-performance than comparable GPU-based P5e and P5en instances.

Those percentages are vendor claims. I wouldn't treat them as neutral benchmarks, but the more durable product point is what specialized infrastructure can change once the workload becomes large enough. A dependency that materially alters the cost or performance envelope of the service above it has stopped behaving like an interchangeable input.

This happens with less drama in payments, mapping, identity, search, messaging, and data infrastructure after a product grows around one supplier's assumptions. Plumbing becomes product architecture. Customers eventually request something the plumbing can't do, and a vendor contract quietly acquires roadmap authority over a feature nobody thought the vendor owned.

## Buy while the dependency is ordinary

Owning a capability creates its own gravity: specialist hiring, tooling, testing, security work, capital, operational coverage, and years of upgrades that somebody has to fund. Google says it began work on its first TPU in 2013. Custom infrastructure is hardly a weekend insourcing project, particularly when hardware, compilers, networking, datacenter operations, and application behavior have to improve together for the economics to work. Vendors can also spread development costs across customer bases an individual buyer can't reproduce, while absorbing failure modes the buyer never sees.

So I'd keep buying while the dependency remains ordinary. Market capability is good enough, switching is credible, and the product's differentiation lives somewhere else rather than inside the supplied component. Reconsider ownership when the dependency repeatedly blocks a product property customers pay for, or when its economics worsen directly as your own usage succeeds.

This connects to my earlier argument that [IoT smart modules turn component choice into product strategy](/blog/2026/08/25/iot-smart-modules-product-strategy/): integration convenience is valuable, but bundled dependencies deserve a lifecycle view.

A useful build-versus-buy memo needs more than a five-year cost table; I'd include switching cost, supplier concentration, roadmap mismatches already encountered, constrained product properties, and what ownership would actually change. Sometimes the right answer remains a contract.

When a supposedly interchangeable component starts deciding what your product can become, though, the build-versus-buy question has already moved upstairs.

## Sources

- [Reuters: Anthropic explored buying AI chip startup MatX](https://www.reuters.com/business/finance/anthropic-planned-then-abandoned-7-billion-purchase-matx-sources-say-2026-08-27/)
- [Google Cloud: Tensor Processing Units](https://cloud.google.com/tpu)
- [Google Cloud: Inside the Ironwood TPU co-designed AI stack](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)
- [AWS: Trainium AI accelerators](https://aws.amazon.com/ai/machine-learning/trainium/)
