---
layout: post
title: "Physical AI Needs an Escalation Contract"
date: 2026-09-05 10:38:00 -0500
category: "IoT + Product"
description: "Physical AI products need explicit escalation rules. A sensor event becomes a product decision when software decides how long to wait before acting."
read_time: "4 min read"
---

A home robot that detects a fall has a surprisingly product-manager-shaped problem: when should it stop waiting and call someone?

Tuya’s new Doova companion robot, unveiled September 4 at IFA 2026, gives that question a concrete answer. If a user appears to have fallen, the robot can move toward them, assess the situation, and wait for a response. After 60 seconds without one, Tuya says Doova starts an emergency workflow and sends family members a two-way live-video alert.

That one-minute decision interests me more than the robot’s multimodal model or its friendly face on a screen.

## Physical AI needs an escalation contract

A 60-second timer looks trivial, but writing down what sits on either side turns a small implementation detail into a product decision with human consequences attached. Escalate too quickly and routine floor-level activity, dropped objects, or misunderstood speech can train families to ignore future alerts. Wait too long and the product fails at the moment its safety promise matters most to the person on the floor.

The timer is product; around it sits a sensing chain, a fallback path, and assumptions about connectivity and human response that deserve requirements too.

Doova combines LiDAR, microphone-based sound localization, vision-based skeletal recognition, mobility, video calling, and autonomous charging in one moving device. Tuya also positions it as a smart-home hub rather than a single-purpose emergency device for one narrow task. More sensors can provide better context, but every additional dependency gives the decision chain another place to fail when conditions get messy.

A PM should trace this escalation end to end. Which signal started it, which signals corroborated it, what did the device try locally, how long did it wait, and who receives the alert when silence continues? The flow also needs an answer when Wi-Fi, video, or the intended recipient is unavailable at exactly the wrong moment.

That’s still a product flow, even though most of it happens without anybody tapping through a screen.

## Measure the quiet failures

Count successful alerts, sure; the more revealing counters include user-canceled alerts, family dismissals, failed calls, events where the robot couldn’t reach the person, and incidents users reported later that the system never detected.

False positives spend trust with every unnecessary interruption. False negatives expose the uncomfortable gap between the product promise and what its sensing system can actually know.

This pattern reaches far beyond eldercare. A leak detector closing a valve and an industrial controller stopping equipment both cross from observation into action, where uncertainty suddenly has physical consequences. Security systems do it too. The interesting requirement isn’t merely “detect X”; it’s the escalation contract around X, including what happens when the detector is unsure.

Model capability doesn’t settle that contract. A benchmark can tell you whether perception improved, but it can’t choose the acceptable delay before an ambiguous observation becomes somebody else’s problem. It certainly can’t decide whether 60 seconds is the right amount of silence before your product calls someone’s daughter.

This is a useful companion to the hardware-lifecycle questions in [IoT Smart Modules Turn Component Choice Into Product Strategy](/blog/2026/08/25/iot-smart-modules-product-strategy/). Once software can trigger a physical consequence, the decision path deserves the same design attention as the hardware underneath it.

For a product that acts in the physical world, the timeout may be one of the most consequential lines in the PRD.

## Sources

- [Tuya Smart unveils Doova at IFA 2026](https://www.tuya.com/news-details/Kfx9813ozlbff)
- [Tuya Smart company and AIoT platform overview](https://www.tuya.com/about)
