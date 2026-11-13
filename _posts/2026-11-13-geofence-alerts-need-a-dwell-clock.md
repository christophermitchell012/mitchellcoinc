---
layout: post
title: "Geofence Alerts Need a Dwell Clock"
date: 2026-11-13 10:48:33 -0600
category: Location + Product
description: "Reliable geofence products combine boundary geometry, location uncertainty, dwell time, and evidence instead of treating every coordinate crossing as truth."
read_time: "5 min read"
---

A delivery van turns through the corner of a depot entrance. The driver's phone reports an arrival, an exit, and another arrival before the van reaches the parking row.

The depot did not move. The van did not leave. Its estimated position wandered across a mathematical circle while the product treated every crossing as fact.

Geofence alerts need a dwell clock. A useful transition combines boundary geometry, location uncertainty, direction, and time before it triggers a customer action.

## Treat the boundary as a decision zone

A geofence is usually represented as a center point and radius. The line looks exact on a map. The location estimate used to cross it is not.

GPS.gov notes that smartphone accuracy can be about 4.9 meters under open sky and becomes worse near buildings, bridges, and trees. Signal blockage and reflections can move an estimated position even when the device remains still.

The product should compare the reported accuracy radius with the distance to the boundary. A five-meter uncertainty band near a five-meter loading zone cannot support a confident arrival event.

Use at least three spatial states:

- Clearly outside the zone.
- Near the boundary with an uncertain state.
- Clearly inside the zone.

I call repeated transitions inside the uncertain state **boundary chatter**. The cure is not a prettier map pin. The decision rule needs room to absorb ordinary measurement error.

Apple applies a system-defined cushion before it reports region crossings. The purpose is practical: prevent rapid enter and exit events when a user travels near the edge.

Products with their own location pipeline should use the same principle. Set separate enter and exit thresholds, or require the device to move beyond an uncertainty-adjusted boundary before changing state.

## Add time before consequence

An entrance event and a meaningful arrival are not always the same thing. A courier can pass a store on the frontage road. A service truck can circle a block. A customer can walk through a mall corridor beside a pickup counter.

Android supports a dwell transition that waits for a device to remain inside a geofence for a defined period. Its guidance recommends dwell events when brief entries would otherwise create alert spam.

That waiting period should match the product decision. A curbside pickup check-in may need thirty seconds. A time-on-site record may need several minutes. A safety alert for a restricted area may require faster action and stronger location evidence.

Make the timing rule visible in product requirements:

- Minimum time inside before arrival.
- Maximum tolerated gap between samples.
- Exit delay before departure.
- Reset behavior after an uncertain observation.
- Different rules for walking, driving, and stationary devices.

Do not silently restart the clock whenever one weak point lands outside. Preserve accumulated evidence unless the device clearly exits or the observation gap becomes too large.

The alert also needs an event-time policy. A delayed background update should not pretend it was observed at delivery time. This is why [connected products need a clock contract](/blog/2026/11/08/connected-products-need-a-clock-contract/) before they turn location history into operational truth.

## Keep the evidence behind the transition

Store more than “entered zone.” Retain the geofence version, transition rule, observation time, receipt time, coordinates, accuracy estimate, speed, provider, device state, and the samples that satisfied the dwell condition.

That record turns a disputed arrival into a testable sequence. It also distinguishes three failures that look identical to a user:

- The device never produced an adequate location.
- The location was adequate, but the transition rule rejected it.
- The rule accepted the transition, but notification delivery failed.

Expose a compact explanation to operators. “Arrival confirmed after 90 seconds inside, with 18-meter accuracy” is better than a green dot. When confidence is weak, say so and show the next action.

Measure precision and recall around the business event, not merely API delivery. Compare geofence arrivals with scans, vehicle ignition, door activity, payment, or another independent signal when one exists.

False arrivals and missed arrivals carry different costs. A retail notification may tolerate a late prompt better than an unwanted one. A fleet detention clock may prefer a review queue over an automatic charge based on weak evidence.

## Design for platform limits and recovery

Mobile operating systems conserve battery by reducing how often they calculate and deliver background location. A requested five-second response does not guarantee a five-second alert.

Android advises larger radii for many geofencing uses and notes that location accuracy can degrade to hundreds of meters or more when Wi-Fi location is unavailable. Apple limits how many regions one app can monitor at once.

Those platform limits belong in the product design, not in an engineering footnote.

Define what happens after reboot, permission loss, disabled location services, stale geofence configuration, and missing network connectivity. Show operators whether a zone is active, degraded, or unmonitored.

Privacy needs the same clarity. Explain why background location is required, how long transition evidence is retained, who can inspect it, and whether precise samples can be discarded after a dispute window closes.

Finally, test the product at the ugly edges. Walk the boundary. Drive past without stopping. Park under a structure. Disable Wi-Fi. Delay network delivery. Reboot the phone inside the zone. Change the radius while a device is nearby.

A geofence is not a line that turns physical movement into certainty. It is a decision system built from noisy observations.

Add a dwell clock. Preserve the uncertainty. Keep the evidence. Then an arrival alert can mean something more useful than “one coordinate crossed a circle.”

## Sources

- [Android Developers: Create and Monitor Geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing)
- [Apple Developer: Region Monitoring and iBeacon](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html)
- [GPS.gov: GPS Accuracy](https://archive.gps.gov/systems/gps/performance/accuracy/)
