---
layout: post
title: "Product Tiers Work Better When Constraints Draw the Line"
date: 2026-09-02 10:38:00 -0500
category: Product Strategy
description: "Product tiers work better when real constraints define the boundary. Before adding another SKU or plan, identify what actually requires a different product."
read_time: "4 min read"
---

A product portfolio gets messy when tiers are organized around customer labels instead of the constraints that actually change the underlying design. Qualcomm's new Dragonwing Q-2390 and IQ-2390 are a useful example: much of the compute foundation is shared, while the industrial version spends its differentiation budget on temperature range, memory protection, deterministic networking, and longevity.

Qualcomm announced both processors on September 1. The Q-2390 is aimed at commercial and consumer devices such as kiosks, access control, appliances, and enterprise terminals. The IQ-2390 targets industrial HMI, machine vision, PLCs, gateways, building controls, and energy systems. The labels matter less.

## Let the expensive constraint draw the boundary

Both chips use a quad-core CPU, Adreno 704 GPU, Hexagon processing, a real-time RISC-V MCU, and 1.1 TOPS of AI performance. They also support Android, Linux variants, and Zephyr, so Qualcomm isn't rebuilding the whole platform for industrial buyers.

The industrial differences aren't cosmetic. Qualcomm specifies operation from -30°C to 115°C, hardware ECC memory protection, dual Gigabit Ethernet with Time-Sensitive Networking, industrial packaging, and support in its longevity program through 2036. Those are constraint features, which is a more useful distinction than simply calling one processor industrial.

A product manager can say one SKU is for retail and another is for factories, but those labels don't explain why two products should exist in the first place. Temperature, deterministic timing, service life, certification, power, physical abuse, connectivity, and failure cost can force different architecture even when customers want similar application behavior and use much of the same software stack.

Persona-shaped tiers tend to collect features because customer identity becomes the justification for putting another checkbox into a package. Sales hears that an enterprise customer wants something, the enterprise SKU absorbs it, and eventually nobody can explain whether the boundary reflects engineering reality, commercial packaging, or organizational history.

Constraint-shaped tiers have a cleaner test: what requirement becomes materially harder or more expensive if both customer groups share the same product? Sometimes nothing does. Then a second SKU may mostly create inventory, documentation, testing, forecasting, support, and migration work without buying enough useful product separation.

Hardware makes that carrying cost obvious because every variant can touch sourcing, certification, firmware, manufacturing tests, spare parts, and lifecycle planning. Software hides much of the same tax behind configuration flags, entitlements, documentation branches, and increasingly baroque pricing pages.

## Customers don't need to see the architecture diagram

Customers buy packages rather than architecture diagrams. That's the strongest argument against taking this framing too literally, because an internally clean segmentation model can still produce customer-facing names based on jobs, markets, or familiar purchasing categories. The internal model can stay internal. Product teams don't need to expose thermal limits and support matrices as the marketing taxonomy; they need to explain why a boundary exists before sales names it.

This framing also changes roadmap discussions because capabilities on the shared platform may reasonably move across tiers over time. Some differences should remain differences. When a feature exists because one tier has a genuinely different operating constraint, forcing parity can erase the reason for the split while adding cost to both products.

I made a related argument about [IoT smart modules](/blog/2026/08/25/iot-smart-modules-product-strategy/): component choices can become product strategy once lifecycle and supplier dependencies accumulate. Portfolio design sits one level above that decision, asking which constraints deserve a different product before deciding which components belong inside it.

Good product tiers make those constraints legible internally, even when customers never see the architecture underneath. When nobody can name the constraint separating two tiers, the portfolio may be segmenting the org chart instead of the product.

## Sources

- [Qualcomm: Dragonwing Q-2390 and IQ-2390 announcement](https://www.qualcomm.com/news/releases/2026/09/-qualcomm-introduces-dragonwing-q-2390-and-iq-2390-processors--e)
- [Qualcomm: Dragonwing Q-2390 product page](https://www.qualcomm.com/internet-of-things/products/q2-series/q-2390)
- [Qualcomm: Dragonwing IQ-2390 product page](https://www.qualcomm.com/internet-of-things/products/iq2-series/iq-2390)
- [Qualcomm: IoT Product Longevity Program](https://www.qualcomm.com/internet-of-things/products/product-longevity-program)
