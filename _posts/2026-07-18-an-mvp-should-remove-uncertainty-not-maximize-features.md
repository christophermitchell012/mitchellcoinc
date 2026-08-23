---
layout: post
title: "MVP Strategy: Are You Learning or Just Shipping Features?"
date: 2026-07-18 08:45:00 -0500
category: Product
description: "MVP strategy should reduce the riskiest uncertainty, not build a miniature final product. Scope the first version around what you need to learn."
read_time: "4 min read"
---

The fastest way to make an MVP too big is to call it "version one."

Now authentication is probably required. Reporting would be nice. Admin controls seem responsible. Somebody asks for CSV export. Before long, the minimum product has a roadmap of its own.

I use a narrower definition:

**An MVP is the smallest amount of product needed to answer an important question.**

That sounds simple, but it changes the backlog immediately.

Instead of asking what belongs in version one, ask what uncertainty is expensive enough that we shouldn't build around it blindly.

## Start with what could make you change direction

Before arguing about scope, I like to write down what we don't know.

Maybe users don't trust the recommendation enough to act on it. Maybe the model isn't reliable under real operating conditions. Maybe the integration saves five minutes in the demo and adds ten minutes of manual cleanup. Maybe customers like the idea but won't pay enough to support the operating cost.

Now the MVP has a job.

If a feature doesn't help answer the risky question, it has to make a stronger case for being included.

That doesn't mean the prototype should be sloppy. Safety, security, and reliability can be part of the uncertainty you're testing. It means polish should be proportional to what you're trying to learn.

## The first version may look nothing like the eventual product

At Refraction AI, I worked on localization systems combining GPS, IMU, and wheel-encoder information with filtering to improve the position estimate.

At that stage, the important question wasn't whether the final operator interface had the right settings panel. It was whether the approach improved localization precision enough to matter to the robot and the operation.

Once that answer became clearer, investing in tooling around it made sense.

I've used the same logic with internal software. A labeling tool doesn't need every feature in a mature commercial platform if the real question is whether it can produce useful training data faster and consistently enough to improve the ML loop.

The first version is allowed to be narrow on purpose.

## Sometimes manual work is the better MVP

I'm comfortable with spreadsheets, scripts, manual review, and behind-the-scenes work when they let a team test the risky assumption faster.

If five customers won't use a manually assisted workflow, automating the whole thing probably won't rescue the idea.

The opposite is valuable too. If the manual process is obviously useful but painful to operate, you've just learned where software can create leverage.

Teams sometimes spend weeks debating MVP scope when the faster move is to run the ugly version with a handful of users and watch what happens.

Ugly can be informative.

Expensive and polished can still be wrong.

This is also why I separate MVPs from roadmaps. A [product roadmap can contain bets with different confidence levels](/blog/2026/08/11/a-roadmap-is-a-portfolio-of-bets-not-a-list-of-promises/). The MVP is one way to retire uncertainty before the bet becomes a larger commitment.

**The product question:** What is the most important thing this version must teach us?

The objective isn't to launch something small for its own sake. It's to become less wrong while you still have the freedom to change direction.

If the MVP ships features but leaves the riskiest question untouched, you shipped something. You just didn't learn much.

## Sources

- [Silicon Valley Product Group: Build to Learn vs Build to Earn](https://www.svpg.com/build-to-learn-vs-build-to-earn/)
