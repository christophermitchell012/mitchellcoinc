---
layout: post
title: "When Satellite Manufacturing Becomes Product Strategy"
date: 2026-09-22 10:38:29 -0500
category: "Product Strategy + Geospatial"
description: "Satellite manufacturing changes product strategy when added capacity improves replenishment, resilience, or regional control customers can actually use."
read_time: "3 min read"
---

A satellite factory looks like an operations story until you ask what customers are actually buying: capacity, service latency, resilience, and control over where operational capability physically lives.

Planet said Monday that it is adding Pelican satellite manufacturing to Berlin this fall. The move extends an operation that already includes engineering, mission control, data, and business teams, while adding about 70 roles through 2027 to a Berlin team of more than 150.

For a product manager, additional capacity creates optionality across the product roadmap, which is the more interesting unit than factory square footage.

## Capacity changes the roadmap

Planet has described its existing California small-satellite factory as capable of producing up to 24 satellites like Pelican per year. The Berlin facility is intended to double Pelican manufacturing capacity.

That capacity changes more than spacecraft supply. A constellation product depends on replenishment cadence, launch availability, ground infrastructure, commissioning, downlink, processing, and customer tasking demand; extra factory throughput only matters when the rest of that chain can absorb it.

I've worked on hardware-software products where one constrained physical component quietly became the roadmap, regardless of what the feature backlog said. Manufacturing capacity deserves the same product treatment as cloud capacity: model demand, identify the bottleneck after expansion, and decide which customer promise the new headroom actually supports.

For Earth observation customers, those capacity promises become concrete fairly quickly. Pelican provides 50-centimeter orthorectified imagery and supports point, line, and area collection modes; Planet's broader product depends on turning collections into useful data quickly enough for customers to act.

This is where [revisit rate becomes a product feature](/blog/2026/09/06/earth-observation-revisit-rate-product-feature/), rather than an orbital statistic.

## Geography can be a capability

Berlin adds another dimension that a spreadsheet-shaped capacity plan can miss. Planet says more than 30% of its global team is in Europe, over 40% of satellite components come from Europe, and European ground stations bring down almost half its data.

Local manufacturing therefore sits beside existing mission operations and data infrastructure instead of appearing as an isolated factory pin on a map.

That matters when customers care about sovereignty, supply-chain resilience, or the location of operational capability. Planet's July agreement with Isar Aerospace goes further: a Pelican built in Germany is planned to launch on a German-built Spectrum rocket, with the companies targeting launch within 12 months of contract signing.

There is an obvious trap in treating geographic redundancy as automatically valuable. Regionalizing production can duplicate equipment, suppliers, qualification work, and specialized expertise; capacity that exists on paper isn't useful if another test station, launch slot, or component becomes the new choke point.

So I'd put four measures beside the factory announcement: qualified satellites per quarter, cycle time from build start to commissioning, constrained-component lead time, and usable on-orbit capacity delivered per dollar.

The product question isn't whether Berlin can build satellites. It's whether a second manufacturing node makes Planet's high-resolution service faster to replenish, harder to interrupt, or materially easier for European customers to buy.

Movement in those measures is what turns industrial capacity into part of the product.

## Sources

- [Planet: Expanding European Operations With Satellite Manufacturing](https://www.planet.com/pulse/planet-s-next-chapter-in-germany-expanding-our-european-operations-with-satellite-manufacturing/)
- [Planet: Modular Smallsat Platform and Manufacturing Capacity](https://www.planet.com/pulse/modular-extensible-smallsat-platform/)
- [Planet Documentation: Pelican Imagery](https://docs.planet.com/data/imagery/pelican/)
- [Planet: European Operations and Infrastructure](https://www.planet.com/pulse/driving-strategic-growth-in-europe-announcing-planet-s-european-advisory-board/)
- [Planet: German Pelican Launch Partnership With Isar Aerospace](https://www.planet.com/pulse/souveraene-weltraumfaehigkeiten-planet-labs-germany-und-isar-aerospace-schliessen-partnerschaft/)
