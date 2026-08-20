---
layout: post
title: "An MVP Should Remove Uncertainty, Not Maximize Features"
date: 2026-07-18 08:45:00 -0500
category: Product
description: "I use MVPs to answer the riskiest unanswered question, not to build a miniature version of the eventual product."
read_time: "4 min read"
---

One of the easiest ways to make an MVP too large is to call it "version one of the product."

That wording almost immediately turns the conversation into feature negotiation. Authentication is probably needed. Reporting would be nice. Admin controls seem responsible. Somebody wants CSV export. Before long, the minimum product has a roadmap of its own.

I use a simpler definition: **an MVP is the smallest amount of product needed to answer an important question.**

That question changes from project to project.

## The first version may look nothing like the final one

At Refraction AI, I worked on systems where the underlying technical question mattered a lot more than polish. One example was localization. We were combining GPS, IMU, and wheel-encoder information and using filtering to improve the position estimate.

At that stage, I wasn't worried about whether the final operator interface had the right settings panel. I wanted to know whether the approach improved location precision enough to matter to the robot and the operation.

Once that answer became clearer, investing in tooling around it made sense.

I've used the same logic with internal software. A labeling tool doesn't need every feature of a mature commercial labeling platform if the real question is whether it can produce useful training data faster and consistently enough to improve the ML loop.

Those are the MVPs I like. They're narrow on purpose.

## Write down what you don't know

Before I start arguing about scope, I try to write down what would change my mind.

It might be:

- We don't know whether users trust this recommendation enough to act on it.
- We don't know whether this model is accurate enough under real operating conditions.
- We don't know whether the integration actually saves time after all the manual handoffs are included.
- We don't know whether customers will pay enough to justify the operational cost.

Now the backlog has a job.

If a feature doesn't help answer the question, it has to make a stronger case for being in the MVP.

That doesn't mean the prototype should be sloppy. Reliability, safety, and security can be part of the experiment itself. It just means the polish should be proportional to what you're trying to learn.

## Sometimes I'd rather fake the automation first

I'm comfortable with spreadsheets, scripts, manual review, and behind-the-scenes work when they let a team test the risky assumption faster.

If five customers won't use a manually assisted workflow, automating the whole thing is unlikely to rescue the idea.

The opposite is useful too. If the manual process is obviously valuable but painful to operate, you've learned something important about where software can create leverage.

I've seen teams spend weeks debating what belongs in an MVP when the faster move was to run the ugly version with a handful of users and watch what happened.

That's the part of MVP work that tends to disappear inside feature checklists. The objective isn't really to launch something small.

It's to become less wrong without spending so much that you've lost the ability to change direction.

## Sources

- [Silicon Valley Product Group: Build to Learn vs Build to Earn](https://www.svpg.com/build-to-learn-vs-build-to-earn/)
