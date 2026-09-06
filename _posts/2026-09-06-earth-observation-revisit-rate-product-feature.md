---
layout: post
title: "Earth Observation: Revisit Rate Can Be the Product"
date: 2026-09-06 10:37:00 -0500
category: "Geospatial + Product"
description: "Earth observation products compete on resolution, but revisit and delivery latency can matter more when customers need to know what changed quickly."
read_time: "4 min read"
---

Earth observation products have spent years teaching customers to ask a familiar question: how sharp is the image? India’s newly launched EOS-05 is a useful reminder that another variable can matter more: how long you wait for the next useful observation.

ISRO launched the 2,367-kilogram EOS-05 on September 4 and placed it into a sub-geosynchronous transfer orbit. On September 5, the agency completed a 5,406.4-second engine burn that moved the spacecraft to an estimated 20,000-by-31,129-kilometer orbit, with more maneuvers planned. Its destination is the 85.5° East geosynchronous slot. That orbit changes the product conversation because persistence becomes part of the value proposition, rather than merely a specification buried beside resolution and sensor type.

## Revisit rate can become the feature

Most Earth-imaging products make some version of a trade: better spatial resolution usually comes from satellites much closer to Earth, but those satellites move quickly over the ground. Customers get a detailed look. Then they wait for another pass, another spacecraft in the constellation, or a new tasking opportunity.

A geosynchronous imager approaches the problem differently, staying over roughly the same region and trading the close-up geometry of low Earth orbit for persistence. For floods, storms, fires, maritime movement, or rapidly changing infrastructure, a less detailed image arriving sooner can answer the more valuable operational question. That sounds obvious until a product team puts “resolution” at the top of every comparison table and quietly trains buyers to optimize for it.

The better product requirement starts with the decision being made because two customers buying “satellite imagery” may actually be purchasing very different clocks; a claims team documenting roof damage may need centimeters of spatial detail; an emergency manager watching floodwater cross roads cares about change over minutes or hours. Same category, different information product.

I’d model those requirements with at least four variables: spatial resolution, revisit latency, coverage area, and delivery latency from collection to a usable customer artifact. Delivery latency gets forgotten surprisingly often. The spacecraft specification can look impressive enough to carry the marketing page by itself. Frequent collection doesn’t help much if processing, downlink, permissions, or a brittle API adds forty minutes before the customer can act on anything.

## Sell the change, not just the image

Persistent observation also changes what the software should deliver, because a gallery works differently when acquisitions stop feeling scarce and individually interesting. Higher cadence creates a slightly awkward product problem: customers probably don’t want to inspect every frame, even if engineering is understandably proud of producing them.

They want the delta, preferably before somebody remembers to refresh a dashboard.

That pushes the product toward change detection, threshold alerts, time-series views, confidence scores, and APIs. Those outputs can trigger another system without requiring a human image-review loop. The satellite may be the expensive part, but the customer experience starts looking less like a photo catalog and more like an event stream with imagery attached.

There’s a counterweight worth keeping visible: persistence over one region narrows geographic flexibility, while higher altitude constrains the detail available from a given sensor and aperture. Cadence won’t dominate every use case, and pretending otherwise simply replaces resolution tunnel vision with revisit-rate tunnel vision.

This complements an earlier argument about [hiding geospatial machinery without hiding the evidence](/blog/2026/08/26/satellite-imagery-product-abstraction/): the abstraction still has to preserve the dimensions that change a customer decision.

EOS-05 is a useful prompt for geospatial product teams because image quality was never really one number, despite how neatly comparison tables make it look. The useful unit may be how quickly the product can tell a customer that the ground changed. Then the customer needs enough evidence to decide what happens next.

## Sources

- [ISRO: Orbit manoeuvring of EOS-05 spacecraft](https://www.isro.gov.in/Orbit_manoeuvring_of_EOS05_spacecraft.html)
- [ISRO: GSLV-F17 / EOS-05 mission status](https://www.isro.gov.in/)
- [Space.com: India launches EOS-05 toward geosynchronous orbit](https://www.space.com/space-exploration/launches-spacecraft/gslv-mark-ii-eos-05-launch-first-indian-geo-earth-observing-satellite)
