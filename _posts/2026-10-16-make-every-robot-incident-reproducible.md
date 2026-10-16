---
layout: post
title: "Make Every Robot Incident Reproducible"
date: 2026-10-16 10:41:29 -0500
category: Product Strategy
description: "Robot telemetry is useful only when a team can reconstruct the failure. Define a replay contract for triggers, context, versions, clocks, and retrieval."
read_time: 5 min
---

A delivery robot stops at 2:13 p.m. By 2:20, it has rebooted, reconnected, and finished the route. The dashboard is green again. Nobody can explain what happened.

The team has logs, camera clips, CAN messages, and ROS topics. Unfortunately, each artifact lives on a different clock, follows a different retention rule, and requires a different person to retrieve it. Data was recorded. The incident was not.

That gap is a product problem.

## A bag file is evidence, not an answer

ROS 2 includes `ros2 bag` for recording and replaying topic data. This is a powerful foundation because a team can inspect what the robot published and reproduce part of its behavior.

Recording every topic does not automatically reproduce the system. The bag may omit the software commit, launch parameters, calibration, map version, feature flags, or health of the cellular link. A timestamp can be precise while still referring to the wrong clock.

MCAP shows how much context a recording format can carry. Its records cover schemas, channels, timestamped messages, attachments, metadata, and indexes. That supports fast access and mixed data types, but the format cannot decide which context your incident process requires.

The product needs a replay contract: the minimum evidence that must accompany a fleet event before engineering calls it reproducible.

## Capture the neighborhood around failure

Continuous full-rate upload is an expensive way to discover that the useful camera frame was overwritten. A better design keeps a rolling buffer on the robot and promotes a bounded window when a trigger fires.

The trigger might be an emergency stop, planner timeout, remote-assistance request, repeated localization jump, watchdog reset, or operator annotation. AWS IoT FleetWise documents both time-based and condition-based collection, including a post-trigger duration. The useful product pattern is broader than that service: collect ordinary summaries continuously, then preserve dense evidence around a meaningful event.

Define each trigger with four values:

- the signals and topics it promotes;
- the pre-trigger and post-trigger windows;
- the upload priority and offline retention period;
- the privacy treatment for images, audio, and location.

Make the trigger catalog versioned. Otherwise, two robots reporting the same event name may produce different evidence.

## Put identity beside telemetry

Every incident bundle should identify the robot, hardware revision, sensor serials, software image, configuration digest, map, mission, and active experiment assignments. Store that manifest with the recording, not in a dashboard that may change next week.

Clock provenance belongs there too. Record wall time, monotonic time, synchronization source, and estimated clock error. When camera, CAN, and ROS events disagree by 300 milliseconds, the team should know whether that is behavior or bookkeeping.

This is where a shared [wireless validation loop](/blog/2026/09/10/wireless-network-validation-close-design-loop/) matters. A connectivity failure should arrive with radio state and transport evidence, not merely a missing heartbeat that asks engineers to guess.

## Measure retrieval, not storage

“We retain thirty days of logs” sounds reassuring and says little about whether anyone can use them.

Measure the percentage of priority incidents that produce a complete replay bundle. Track time from incident ID to a bundle opened in the analysis tool. Count manual credentials, shell commands, and team handoffs. Run a scheduled replay against a known event and alert when schemas, plugins, or dependencies no longer load.

Call the missing portion replay debt. It accumulates whenever a new sensor, autonomy node, or configuration source ships without joining the incident bundle.

Storage volume is an infrastructure metric. Reproducibility is the product outcome.

## Make failure portable

The best incident artifact should travel from operations to engineering without a guided tour. One identifier should open the same synchronized timeline, version manifest, trigger explanation, and raw evidence for everyone.

That changes the postmortem question. Instead of asking who can find the logs, the team can ask what the robot believed, what changed, and which product decision prevents the next stop.

## Sources

- [ROS 2 Documentation: Recording and Playing Back Data](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html)
- [MCAP: Format Specification](https://mcap.dev/spec)
- [AWS IoT FleetWise: Collect Data With Campaigns](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html)
