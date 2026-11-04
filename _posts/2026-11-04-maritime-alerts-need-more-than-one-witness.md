---
layout: post
title: "Maritime Alerts Need More Than One Witness"
date: 2026-11-04 10:14:54 -0600
category: Product Strategy
description: "Maritime awareness products should preserve sensor provenance, corroborate contacts, and show disagreement before they escalate an alert."
read_time: 5 min
---

At 2:13 in the morning, a camera on a harbor pier sees a warm shape moving between two anchored vessels. Radar reports a weak return nearby. The Automatic Identification System shows nothing.

A clean dashboard could turn those three facts into one bright red target. That would look decisive. It might also wake a watchstander for a drifting plastic barrel.

Maritime awareness products need to do more than merge detections. They need to explain when independent sensors actually corroborate one another, when they disagree, and what evidence deserves a human decision.

## A fused dot can hide three different stories

AIS is useful, but it is not a complete roster of traffic. International Maritime Organization guidance notes that some small craft, fishing vessels, warships, and government vessels may not carry it. Equipped ships may also switch it off.

The same guidance warns that transmitted sensor data can be wrong. AIS should support radar and other navigational information rather than replace them.

Radar has a different set of blind spots. Sea clutter, shoreline reflections, weather, target shape, and geometry can weaken or distort a return. A visible or infrared camera adds classification detail, yet glare, fog, darkness, spray, and occlusion change what it can see.

These are not interchangeable votes. Three reports are not automatically three witnesses.

A product creates **corroboration debt** when it collapses uncertain observations into a single confident marker without retaining how that conclusion was built. The operator gets an answer now, then pays for the missing reasoning during an incident review.

## Make the contact an evidence bundle

The primary product object should be a contact with an evidence bundle, not a dot with a color. Each observation should retain its sensor, location, timestamp, calibration state, detection method, confidence, and raw-data reference.

The bundle should also show the association logic. Two detections may refer to the same vessel because their positions, motion, size, and timing agree. They may also be two vessels crossing near each other. The interface should expose the match distance, time gap, and motion consistency used to join them.

NOAA-hosted research on above-water sensing combined marine radar, lidar, visible cameras, infrared imaging, GPS, and inertial data. The work required time synchronization, frame correction, common data formats, metadata, and significant parameter tuning. That plumbing is the product boundary. A fused contact is only as defensible as the transformations beneath it.

The evidence bundle should preserve dissent. If radar tracks a contact while two cameras see open water, the product should not average the disagreement into medium confidence. It should say that radar supports the contact, cameras do not, and visibility conditions may explain why.

This resembles the need to [make every robot incident reproducible](/blog/2026/10/16-make-every-robot-incident-reproducible/). The system must retain enough state to replay the decision, not merely display its final label.

## Corroboration needs rules, not arithmetic

A simple majority rule fails quickly. Two cameras on the same mast can share the same occlusion. Three software detectors can consume the same frame. Their agreement is correlated, not independent.

The product should group evidence by failure domain. Sensors that share power, network, mounting point, weather exposure, clock source, or upstream model should not count as separate witnesses without qualification.

NIST has highlighted a related problem in automated-vehicle perception. Combining uncertain sensors does not guarantee that the system's collective uncertainty remains bounded. Product teams should resist translating more inputs into a larger confidence number unless the claim has been tested under relevant conditions.

Corroboration policy should depend on the action. Logging an unknown contact can accept a low threshold. Sending an operator notification should require stronger support. Initiating an autonomous maneuver, dispatching a patrol, or declaring a security event should demand more evidence and a narrower uncertainty range.

The rules need explicit exceptions. A high-quality radar track entering a restricted zone may warrant escalation without AIS or camera confirmation. A distress beacon should not wait for a second sensor. The system should record which exception fired and why.

## Measure alerts by what they cost

Detection rate alone is not a product score. An alert that arrives without enough evidence sends the operator back through video, radar history, and radio calls. The software moved the investigation rather than completing it.

Track alert precision by location, weather, sensor mix, vessel class, and action level. Measure time from first observation to corroboration, operator review time, unresolved disagreements, missed contacts found later, and alerts downgraded after inspection.

Test disagreement on purpose. Disable the live AIS feed. Delay one camera clock. Rotate a sensor frame. Add radar clutter near a seawall. Cut one network link. Confirm that the product shows degraded evidence instead of manufacturing certainty.

Collaborative edge nodes can add new viewing angles, especially around islands, piers, and large ships. They also add clock drift, duplicate reports, intermittent links, and shared blind spots. The product must identify which node saw what and whether the observations were independent enough to matter.

The useful promise is not perfect awareness. It is an alert whose evidence, uncertainty, and dissent survive the trip from sensor to watchstander.

One witness can start a contact. More witnesses can strengthen it. Trust grows when the interface shows the difference.

## Sources

- [IMO Resolution A.1106(29): Revised Guidelines for the Onboard Operational Use of Shipborne AIS](https://www.navcen.uscg.gov/sites/default/files/pdf/ais/references/IMO_A1106_29_Revised_guidelines.pdf)
- [NOAA Repository: All-Around Above-Water Sensing for Recreational Boaters](https://repository.library.noaa.gov/view/noaa/38553/noaa_38553_DS1.pdf)
- [NIST IR 8527: Standards and Performance Metrics for On-Road Automated Vehicles](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8527.pdf)
