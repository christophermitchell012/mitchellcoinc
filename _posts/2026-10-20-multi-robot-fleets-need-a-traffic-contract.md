---
layout: post
title: "Multi-Robot Fleets Need a Traffic Contract"
date: 2026-10-20 10:17:35 -0500
category: Product Strategy
description: "A multi-robot fleet needs a traffic contract for intent, right of way, stale data, deadlocks, shared infrastructure, and safe recovery."
read_time: 5 min
---

Two robots meet in a narrow aisle. Both stop. Nothing is broken, yet the warehouse has acquired a very polite traffic jam.

This is easy to dismiss as a routing bug. It is usually a product-boundary problem. Each robot may understand its own map, mission, and safety rules. The facility still needs a shared agreement for who can enter constrained space, how long that claim remains valid, and what happens when reality diverges from the plan.

Call that agreement a **traffic contract**.

## Interoperability does not assign right of way

Robot interoperability covers several distinct layers. Mixing them creates false confidence.

The MassRobotics AMR Interoperability Standard lets different vehicles share location, speed, direction, health, and availability. An operator can see unlike fleets without demanding every vendor expose its internal map.

VDA 5050 defines a vendor-neutral interface between mobile robots and central fleet control. It specifies orders, state, connection status, and released route segments. It also draws a useful line: prioritization, congestion handling, deadlock resolution, and operational responsibility remain outside the interface.

That gap is where a product decision lives. Compatible messages do not automatically produce compatible behavior.

## Intent needs an expiration date

Open-RMF models traffic with a schedule of intended trajectories. Fleet managers report where their robots expect to be. The schedule changes when routes, delays, or cancellations change, and negotiation begins when intentions conflict.

The product implication is sharper than "share the route." Every intention needs four properties:

1. **Scope:** the aisle, intersection, lift, door, or charging bay being claimed.
2. **Time:** when the robot expects to enter and clear that resource.
3. **Confidence:** whether the estimate reflects current motion or an aging plan.
4. **Expiry:** when other participants must stop trusting the claim.

Without expiry, a disconnected robot can leave a ghost reservation. Missing confidence makes a delayed robot look punctual. An unclear scope lets systems disagree about whether a doorway includes its approach zone.

This is the traffic contract in practical form: a time-bounded promise about shared space, plus a defined response when the promise becomes stale.

## Design the failure states before the happy path

A fleet coordinator can look impressive in a clean simulation. The hard product work begins when a robot pauses for a pallet, loses connectivity, or cannot execute the route it accepted.

The traffic contract should answer uncomfortable questions. May a robot finish its released segment after losing the coordinator? Does a lift reservation expire while the robot waits outside? Which fleet yields during an emergency? How does an operator clear a deadlock without creating another?

VDA 5050 provides a useful pattern through its base and horizon. Released nodes and edges form the route a robot may traverse. Unreleased route elements remain a plan, and the robot stops at the decision point if the base is not extended.

The broader product lesson is to separate permission from prediction. A predicted path is not yet a right of way.

The user interface should preserve that distinction. Operators need the current permission, next contested resource, state age, and reason a robot is waiting. A red dot labeled "blocked" is weak evidence. "Waiting 38 seconds for Lift 2; reservation held by Fleet B; state updated 1.2 seconds ago" is actionable.

## Measure coordination debt

Multi-fleet sites accumulate special cases. One robot cannot reverse. Another needs a wider turn. A third loses localization near reflective doors. Soon, nobody can predict the effect of a map edit.

Track this as **coordination debt**: the growing cost of site-specific rules that sit outside the common traffic contract.

Useful measures include reservation timeouts by resource, deadlocks per hundred missions, manual traffic releases, stale-intent duration, and throughput lost at shared infrastructure. Segment them by fleet and location. The average hides the one intersection that ruins every afternoon shift.

This also connects to a broader [platform strategy question: how many handoffs does the platform remove?](/blog/2026/10/02/platform-strategy-count-the-handoffs-you-remove/) A traffic layer earns its place when adding a new fleet requires an adapter and a verified contract, rather than another set of operator workarounds.

## Ship the contract with the map

A facility map is incomplete if it only describes geometry. It should carry resource boundaries, direction rules, speed limits, waiting positions, reservation policies, and recovery behavior. Version those rules, test them against replayed traffic, and retain the prior version for rollback.

The goal is not perfect global optimization. It is legible coordination under imperfect information. When every fleet can state its intent, respect bounded permission, and recover from stale promises, the narrow aisle becomes infrastructure instead of a daily negotiation.

## Sources

- [Open Robotics: RMF Core Overview](https://osrf.github.io/ros2multirobotbook/rmf-core.html)
- [VDA 5050: Vendor-Neutral Mobile Robot Interface](https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md)
- [MassRobotics AMR Interoperability Standard](https://github.com/MassRobotics-AMR/AMR_Interop_Standard)
