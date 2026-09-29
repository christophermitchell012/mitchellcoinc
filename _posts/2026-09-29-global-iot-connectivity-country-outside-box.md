---
layout: post
title: "Global IoT Connectivity: Keep the Country Outside the Box"
date: 2026-09-29 10:54:04 -0500
category: "IoT + Product Strategy"
description: "Global IoT products get expensive when country-specific connectivity is baked into hardware. Keep carrier and provisioning choices replaceable after shipment."
read_time: "3 min read"
---

A connected product can cross a border in a shipping container and discover that its connectivity architecture didn't travel with it.

NTT DOCOMO BUSINESS gave that problem a useful, concrete shape today. The company and stc group are launching an IoT connectivity arrangement for Komatsu construction equipment in Saudi Arabia, where long-term roaming and permanent service by foreign operators without a local communications license can be restricted or prohibited. Komatsu's Komtrax system depends on machines sending operating data back for remote monitoring and analysis.

The interesting product work sits below the dashboard, inside decisions customers rarely see.

## Treat connectivity as a replaceable dependency

Connected-device teams are tempted to treat the modem, SIM, carrier contract, and cloud endpoint as plumbing. That works until expansion adds a country whose rules, carrier relationships, or coverage assumptions don't match the original design.

I've worked on IoT and teleoperation products where the device was only one piece of the operating system around it. Once hardware is deployed across customer sites, changing a physical dependency gets expensive fast: somebody may need to find the asset, open it, replace something, reprovision it, restore its identity, and prove that it came back correctly.

NTT's Saudi arrangement separates more of that country-specific work from Komatsu's product. stc supplies the local network and connectivity-management platform, while NTT describes a service and operating model built around local communications requirements. The machinery can keep feeding Komtrax without Komatsu independently rebuilding the carrier relationship for this market.

For product managers planning international IoT, the architecture review should separate what must remain globally identical from what should stay swappable after shipment.

An eSIM pushes that boundary further. NTT's SIGN Pro offering, announced September 24 for availability in March 2027, plans support for the GSMA SGP.32 IoT eSIM standard. NTT says communications profiles can then be changed remotely after devices have shipped, including switching service providers without replacing a physical SIM or manufacturing a different device configuration for every country.

A remotely replaceable carrier profile turns a decision made at manufacturing time into an operating decision. That's a much bigger product change than the tiny rectangle of silicon suggests.

## The SKU you avoid may matter more

Global hardware programs accumulate country variants almost by gravity. Different radio modules, SIMs, labels, certifications, provisioning procedures, and inventory pools can turn one connected product into a family of nearly-the-same products.

Some country-level variation is simply unavoidable in hardware. Radio approvals and local rules don't disappear because the architecture is elegant.

Still, product teams should count avoided variants as a product metric. A connectivity layer that lets one hardware configuration serve another market can reduce inventory fragmentation, field retrofits, provisioning branches, country-specific manufacturing decisions, and the ugly support question of exactly which device version the customer owns.

This connects to my earlier argument about [smart modules preserving product options](/blog/2026/08/25/iot-smart-modules-product-strategy/). The same logic applies one layer above the board: preserve choices that are expensive to recover after hardware leaves the factory.

For global IoT products, I'd put one question into the architecture review before debating another dashboard feature: what decision are we accidentally soldering into the device?

The best answer is sometimes nothing soldered into it at all. Leave the country-specific choice outside the box.

## Sources

- [NTT DOCOMO BUSINESS: IoT connectivity for Komatsu construction equipment in Saudi Arabia](https://www.ntt.com/about-us/press-releases/news/article/2026/0929_2.html)
- [NTT DOCOMO BUSINESS: SIGN Pro for large-scale global connected products](https://www.ntt.com/en/about-us/press-releases/news/article/2026/0924_2.html)
