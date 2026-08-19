---
layout: post
title: "AI Prototypes Usually Fail at the Workflow Boundary"
date: 2026-07-05 14:10:00 -0500
category: AI + Product
description: "The model is only one component. Most of the product work lives in context, permissions, handoffs, review and recovery."
read_time: "4 min read"
---

The most impressive part of an AI demo is often the least representative part of the eventual product.

Give a model the right prompt, the right context and a clean example and it can do something genuinely useful in a few seconds. That's the fun part.

Production is where all the inconvenient questions show up.

Which context should the model see? How fresh is it? What is the user actually allowed to access? What happens when the model is uncertain? Where does the result go? Can a human correct it? Do we capture that correction? What happens on the third retry when an upstream service is down?

I've seen versions of this problem across AI/ML, robotics and geospatial workflows. The model matters, obviously, but the handoffs around it usually decide whether the feature survives contact with real work.

## A good answer in the wrong place is still a bad product

Take a support assistant.

Generating a decent draft reply isn't the hard part anymore.

The useful system has to retrieve the right account history, respect permissions, know which product or configuration the customer has, surface uncertainty, put the draft where the agent is already working, and log what was actually sent.

If the agent has to copy an identifier into another tool, wait, interpret a block of prose, copy the answer back and then clean it up, the AI can be technically impressive and operationally worse.

One exercise I use is to draw the workflow with the model as only one box:

> event arrives → retrieve context → run model → validate output → human review if needed → take action → capture outcome

Then I spend more time on the arrows than the box.

That's where stale data, permission mistakes, formatting mismatches, retries and missing feedback tend to hide.

## Model metrics aren't enough

Accuracy, precision, recall, latency and cost all matter. I still want them.

But I also want to know what happened to the job:

- Did the user finish faster?
- How often was the recommendation accepted?
- When users changed it, what did they change?
- Did the feature create a new support burden?
- How often did the system escalate instead of guessing?
- Did it hold up on the ugly edge cases, not just the demo set?

Sometimes the model gets better while the workflow gets worse. That's a pretty useful warning that the team is optimizing one component instead of the product.

## Prototype the boring parts earlier

Once the core model capability looks plausible, I like to prototype the unglamorous pieces sooner than feels natural.

Can we get the right data automatically? Can we show provenance? Can the user recover from a wrong answer? Can the output fit into the existing system without opening another tab? Can we capture feedback without asking the user to fill out a survey every time?

Those questions rarely make the demo video.

They're often the difference between a feature people try once and something they quietly start depending on.

That's usually what I'm after. I don't need the user to admire the model. I need the work to get easier.
