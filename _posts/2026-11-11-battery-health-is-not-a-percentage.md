---
layout: post
title: "Battery Health Is Not a Percentage"
date: 2026-11-11 10:16:15 -0600
category: Energy + Product
description: "Battery products should separate usable energy, power capability, uncertainty, and operating limits instead of hiding health behind one percentage."
read_time: "5 min read"
---

The delivery robot reports 82 percent battery health. It completes a slow morning route, then shuts down on the same hill it climbed last month.

The number was not fabricated. It came from a capacity estimate. The robot still stored most of its original energy, but rising internal resistance had reduced the power available under load.

One percentage made two different conditions look like one answer.

Battery products need a health contract: a clear definition of what health measures, under which conditions, with what uncertainty, and for which decision.

## Separate energy health from power health

State of charge describes how full a battery is now. State of health describes how its present capability compares with a reference condition. Neither concept is automatically one-dimensional.

A battery can lose energy capacity, limiting runtime or range. It can also lose power capability, causing voltage sag, slower charging, heat, or failure during a demanding load. Those changes may progress at different rates.

The U.S. Department of Energy notes that batteries experience both power and capacity fade. The mechanisms depend on chemistry, operating profile, ambient conditions, cycling, time, temperature, and state of charge.

A useful product surface should therefore expose at least:

- Estimated usable energy under stated conditions.
- Available charge and discharge power.
- Temperature and state-of-charge limits.
- Confidence or uncertainty for each estimate.
- The reference state used for comparison.

I call the mistake of collapsing those dimensions into one reassuring score **health compression**. The interface gets simpler while the decision becomes harder to defend.

## Attach conditions to every estimate

Battery capability changes with temperature, load, recent use, and operating limits. A cold pack may temporarily deliver less power without having suffered equivalent permanent degradation.

Preserve the conditions behind the estimate. Record pack temperature, current, voltage response, state of charge, recent duty cycle, test duration, firmware version, and estimation method.

NREL describes battery state-of-health estimation as a difficult problem because health is not directly measurable during ordinary operation. Models infer it from observable behavior, and their accuracy depends on the data and conditions available.

That uncertainty belongs in the interface. “Usable energy: 41 to 44 kWh at 25°C” is more honest than “health: 86%.”

Trend history matters too. A stable estimate with a narrow range supports a different action than a value that moved six points after one software update.

When the method changes, keep both the old and new series or mark the discontinuity. Silent recalculation turns an algorithm revision into fictional battery degradation or recovery.

## Define health around the next decision

There is no universal threshold at which a battery stops being useful.

An electric vehicle owner may care about winter range and fast charging. A warehouse robot may need enough peak power for ramps. A stationary system may tolerate lower energy density while still serving a predictable backup load.

NREL research on second-life batteries emphasizes that end-of-life can mean the battery no longer meets driver needs, not that it has no remaining value. Another application may have different capacity, power, duration, safety, and economic requirements.

Products should translate estimates into decision-specific states:

- Suitable for the current duty cycle.
- Suitable with reduced load or runtime.
- Inspection or controlled capacity test required.
- Eligible for another defined application.
- Unsafe or uneconomic to continue.

Each state needs an owner, evidence threshold, and next action. The interface should also show which requirement failed. “Service soon” is weak if nobody knows whether the problem is range, peak power, thermal behavior, or confidence.

This is where a [failure horizon matters more than an anomaly score](/blog/2026/11/07/predictive-maintenance-needs-a-failure-horizon/). A battery warning becomes useful when it leaves enough time to change the route, schedule service, or source a replacement.

## Design recalibration and disputes before launch

Health estimation will occasionally disagree with observed operation. The product needs a recovery path before that happens.

Define when the system requests a controlled test, longer observation window, sensor check, or model reset. Preserve the estimate before recalibration, the evidence that triggered it, and the result afterward.

Warranty decisions need stronger traceability. A claim should identify the metric, reference capacity or power, test conditions, allowed operating window, software version, and applicable threshold. A bare percentage invites disputes because both sides can attach different meanings to it.

Fleet views should separate individual outliers from population drift. If every pack changes after a firmware release, the likely cause differs from one pack losing power during high-current events.

Finally, measure whether health estimates improve operations. Track unexpected shutdowns, early replacements, late replacements, disputed claims, forecast error, and time between warning and intervention.

Battery health is not a decorative gauge. It is a collection of estimates used to make expensive decisions about operation, service, warranty, and reuse.

Show the dimensions. Keep the conditions. Name the uncertainty. Then the product can turn electrochemical change into an operating decision people can trust.

## Sources

- [National Renewable Energy Laboratory: Battery State of Health Estimator](https://www.nrel.gov/docs/fy25osti/91880.pdf)
- [U.S. Department of Energy: Batteries, Chapter 4 Technology](https://www.energy.gov/sites/default/files/2022-10/Chapter_4-Technology.pdf)
- [National Renewable Energy Laboratory: Procedure for Assessing the Suitability of Battery Second Life Applications](https://www.nrel.gov/docs/fy22osti/84527.pdf)
