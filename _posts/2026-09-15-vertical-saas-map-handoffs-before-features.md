---
layout: post
title: "Vertical SaaS Should Map Handoffs Before Features"
date: 2026-09-15 10:18:00 -0500
category: "SaaS + Product Strategy"
description: "Vertical SaaS earns its industry fit by removing costly handoffs between existing systems, not merely by adding industry vocabulary to another UI."
read_time: "4 min read"
---

Vertical software used to mean taking a horizontal product, adding industry vocabulary, and charging a little more for the privilege.

Anthropic's September 14 release of Claude for Financial Advisors points at a more demanding definition. The product connects to custodians, portfolio platforms, CRMs, planning tools, estate systems, and meeting software, then packages those connections into advisor-specific workflow skills. Charles Schwab provides the first RIA custodian integration for more than 16,000 independent registered investment advisers.

The interesting product decision isn't the finance-flavored interface. Anthropic put the work down in the seams between systems.

A financial advisor preparing for a meeting may need balances and positions from custody, portfolio performance elsewhere, CRM history, planning assumptions, estate documents, and notes from the last conversation, even though none of those systems is necessarily broken and each may be doing its own job perfectly well. The workflow can still fragment enough to consume hours around one meeting.

Vertical SaaS teams should notice that. Customers rarely wake up wishing for one more system of record.

They buy when an important job crosses existing boundaries badly, and fixing the handoffs is worth more than polishing another isolated screen.

![Vertical SaaS workflow graph showing product opportunity in handoffs between systems](/assets/images/vertical-saas-handoff-graph.svg)

## The edges are product surface

Claude for Financial Advisors makes that visible through connectors and skills covering meeting preparation, portfolio review, post-meeting work, prospect intake, and compliance review. Anthropic says regulated activities such as investment recommendations, client communications, and compliance determinations remain subject to human review and approval.

That boundary matters. In a regulated workflow, automation value doesn't rise monotonically with autonomy or with the number of buttons software can press. Sometimes the better product automates the scavenger hunt, assembles evidence, drafts the work, and stops exactly where accountable judgment begins.

I've seen the same shape in integration-heavy products outside finance: customer pain often lives between two perfectly respectable boxes on an architecture diagram. It hides in the arrow everyone labels “integration,” a wonderfully compact way to make six months of ugly product work disappear.

My cat Dogbert has a simpler integration model: food enters one interface, while complaints exit through several others with excellent uptime.

For product teams, I'd map a vertical workflow as a graph before writing the feature list, with systems and people as nodes and handoffs as edges. Then mark where context gets re-keyed, reconciled, approved, delayed, or lost. A dense cluster of ugly edges may be the better product opportunity.

## Connectors create a second product problem

There's a catch. Connector-heavy products inherit other companies' permissions, schemas, API limits, outages, version changes, and occasionally their very creative interpretation of backward compatibility. As the workflow becomes more useful, the product becomes more dependency-shaped too, which argues for explicit provenance, graceful partial failure, and clear ownership when a source can't answer.

This is also why [API deprecation is a customer migration problem](/blog/2026/08/24/api-deprecation-customer-migration/): every connector eventually changes underneath somebody.

This changes how I'd evaluate a vertical product: count fewer industry nouns in the UI and measure how much cross-system work actually disappears. Also measure whether users can trace an answer to its source, recover when one dependency fails, and see clearly where software hands judgment back to them.

Vertical SaaS earns its adjective when it understands the industry's handoffs, not merely its vocabulary.

## Sources

- [Anthropic: Claude for Financial Advisors](https://claude.com/blog/claude-for-financial-advisors)
- [Charles Schwab: Charles Schwab and Anthropic to Bring Claude to Independent Registered Investment Advisors](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-and-Anthropic-to-Bring-Claude-to-Independent-Registered-Investment-Advisors/default.aspx)
- [Reuters: Anthropic targets financial advisers with new Claude tool](https://www.reuters.com/business/anthropic-targets-financial-advisers-with-new-claude-tool-2026-09-14/)
