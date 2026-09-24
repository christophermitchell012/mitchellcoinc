---
layout: post
title: "Data Deletion Is a Product State Machine"
date: 2026-09-18 10:18:00 -0500
category: Data Products
description: "Data deletion works better as a reversible state machine: use policy and context to find candidates, quarantine first, and make deletion the last step."
read_time: 4
---

Storage charges for indecision. Keep a file because somebody might need it, copy it during a migration, back up the copy, then feed both versions into analytics. Nothing looks broken, yet the bill simply gets fatter while the organization's confidence about what can safely disappear gets thinner.

Varonis released Data Lifecycle Management on September 15, a product that identifies redundant, obsolete, and trivial data across connected sources. Its interesting design choice isn't the ROT acronym. DLM combines classification, permissions, and activity history, then quarantines candidates before deletion so the action remains reversible.

That sequence matters because deleting enterprise data is an inference problem disguised as housekeeping, with consequences that usually surface after somebody needs the missing thing.

![Data deletion state machine showing Active, Candidate, Quarantine, Delete, and a Restore path](/assets/images/data-deletion-state-machine.svg)

## Old doesn't mean disposable

A file being old tells you almost nothing by itself. An untouched seven-year-old contract may be exactly what a retention policy requires, while a three-month-old export containing customer data may already be an unnecessary duplicate. Last-access time, sensitivity, ownership, permissions, duplicate relationships, retention rules, and where the authoritative copy lives all change the decision.

This makes deletion a surprisingly product-shaped problem. The interface has to explain why an object is a candidate, what policy caught it, what else depends on it, and what happens next. A giant red DELETE button is technically complete in roughly the same way my cat Dogbert is technically qualified to manage household document retention: decisive, inexpensive, uninterested in appeals, and quite certain that anything left unattended belongs to him anyway.

Quarantine is the more interesting product primitive because it creates a reversible middle state between "we should probably keep this forever" and permanent deletion.

Teams can automate the low-risk transition into quarantine, observe exceptions, restore mistakes, and reserve irreversible deletion for a later policy boundary. That changes the economics of automation because confidence doesn't have to be perfect before the system does useful work, and mistakes don't immediately become recovery projects.

## Deletion needs metadata too

The same principle applies beyond security software. Product teams building data platforms should treat deletion metadata as seriously as creation metadata: provenance, owner, retention class, dependencies, last meaningful use, and disposition state. Those fields are the evidence behind a later removal decision. In [synthetic data work](/blog/2026/09/16/synthetic-data-only-good-as-joins/), relationships determine whether generated records behave like a system. Here, relationships determine whether removing a record damages one.

There's a counterweight: more context can become another excuse to retain everything, especially when legal, security, finance, and engineering each have a different definition of "needed." A good lifecycle product therefore needs explicit policy precedence and an audit trail, rather than a committee-shaped exception queue that grows forever while storage quietly compounds.

Creation gets the glamorous product work: upload, ingest, sync, import, and increasingly some AI-fied button that promises to organize the resulting pile. Deletion usually arrives later wearing a compliance badge, although its product mechanics are every bit as real as the ingestion path.

It deserves a real state machine with visible transitions, reversible actions, policy ownership, and enough context that an administrator can understand the consequence before approving it. Data shouldn't disappear because it got old; it should disappear because the product can explain why keeping it no longer earns its storage, risk, or operational cost.

## Sources

- [Varonis: Introducing Data Lifecycle Management](https://www.varonis.com/blog/introducing-data-lifecycle-management)
- [Varonis: Data Lifecycle Management product page](https://www.varonis.com/solutions/data-lifecycle-management)
- [Varonis: September 2026 product changelog](https://www.varonis.com/platform/changelog)
