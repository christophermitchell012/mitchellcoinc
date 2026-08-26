---
layout: post
title: "Satellite Imagery: Hide the Machinery, Keep the Receipt"
date: 2026-08-26 12:00:00 -0500
category: Geospatial + Product
description: "Satellite imagery is getting easier to query. The product challenge is hiding geospatial complexity without hiding the evidence customers need to trust."
read_time: "4 min read"
---

Satellite imagery has a vocabulary problem before it has a data problem.

SkyFi launched Rowan this week, an AI navigator that accepts plain-language questions, searches imagery archives, can task new satellite captures, recommends geospatial analytics, and returns results inside the same conversation. The announcement is interesting for a reason that has little to do with chat interfaces.

Commercial Earth observation products have traditionally exposed the machinery of the supply chain to the buyer. Customers encounter resolution, revisit rate, incidence angle, cloud cover, archive versus tasking, sensor type, area-of-interest geometry, and processing choices before they get near the business question.

Experts need those controls; most buyers don't wake up wanting a better incidence angle; they want to know whether construction moved, a road changed, vegetation declined, or inventory appeared somewhere.

That distinction creates a product decision: how much domain machinery should remain visible after software becomes capable of translating intent into a valid geospatial workflow?

## Abstraction is useful until the answer becomes unauditable

Natural language can compress a complicated workflow. A request to compare a construction site with last year's imagery may require selecting dates, finding usable scenes, accounting for clouds, aligning imagery, choosing an analytic method, and deciding whether a fresh capture is worth ordering.

Hiding that sequence can make satellite imagery accessible to people who'd never learn a traditional GIS workflow. It also removes clues that an expert uses to judge whether the answer deserves trust.

A 30-centimeter optical image and a three-meter image aren't interchangeable because both contain the same building, and neither are images captured at different sun angles, seasons, or viewing geometries. A conversational layer that quietly chooses among them is making product decisions on the user's behalf.

I'd treat those choices as inspectable defaults rather than invisible magic. Show the answer first when confidence is high, then preserve a short path back to the evidence: source image, capture date, sensor, resolution, processing step, and assumptions that materially changed the result.

This is less dashboardification than provenance with decent manners.

The interface doesn't need to dump remote-sensing homework onto every user. It does need to let a skeptical customer pull the thread.

## Geospatial products can sell the question instead of the sensor

Traditional imagery catalogs naturally organize around what suppliers sell: sensors, resolution tiers, archive scenes, tasking windows, analytics, and square kilometers. A question-driven interface starts closer to what customers are buying.

That changes product discovery because search logs from a conversational system can expose recurring customer intents in language customers actually use, rather than forcing every request into the company's existing catalog taxonomy.

Repeated questions about construction progress, for example, could reveal a workflow-shaped product hiding inside what looked like one-off imagery purchases. The product team can then decide whether to package that workflow, automate more of it, or leave it as a flexible query.

The risk appears when every request becomes a friendly text box: customers may lose useful ways to express constraints, compare alternatives, or understand why one answer costs more than another. Power users also notice quickly when a simplified interface makes a precise job slower.

A good abstraction should therefore have an escape hatch. Plain language gets the user to a sensible starting point; explicit controls remain available when resolution, acquisition timing, sensor choice, budget, or geometry matters.

I've made a similar argument about [API deprecation and customer migration](/blog/2026/08/24/api-deprecation-customer-migration/): product work includes moving users between mental models, not merely shipping the replacement interface. Geospatial abstraction has the same migration problem in miniature. The old model was "choose imagery." The emerging model is "state the decision, then inspect how the system assembled the evidence."

That also connects to [MVPs as uncertainty-reduction tools](/blog/2026/07/18/an-mvp-should-remove-uncertainty-not-maximize-features/). The useful experiment isn't whether people enjoy chatting with a map. It's whether less-specialized users can reach defensible answers without creating a support queue full of expert corrections.

The product opportunity in satellite imagery isn't removing the sensor from the system. It's letting the customer's question arrive before the sensor specification, while keeping the evidence close enough to challenge.

A good geospatial product can hide the machinery. It shouldn't hide the receipt.

## Sources

- [SkyFi: Rowan AI navigator announcement](https://www.prnewswire.com/news-releases/skyfi-launches-rowan-a-native-ai-navigator-that-turns-satellite-imagery-into-decision-ready-answers-302860100.html)
- [SkyFi: What Is SkyFi? Satellite Imagery Made Simple](https://skyfi.com/en/blog/what-is-skyfi)
- [SkyFi: Introducing Open Data and SkyFi Insights](https://skyfi.com/en/blog/introducing-open-data-and-skyfi-insights)
