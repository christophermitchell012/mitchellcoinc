---
layout: post
title: "Enterprise Software Can Scale Without Feeling Heavy"
date: 2026-08-28 10:48:00 -0500
category: Enterprise + Product
description: "Enterprise software can add security, administration, and scale without burdening every user. Separate enterprise controls from the daily workflow."
read_time: "5 min read"
---

Linear passed $100 million in annual recurring revenue this week, and the number is interesting for a reason beyond startup scorekeeping.

The company says more than 40,000 organizations use its product, while its enterprise tier adds SAML, SCIM, granular administration, advanced organization modeling, migration help, priority support, account management, and other controls aimed at larger enterprise deployments today.

Those are unmistakably enterprise requirements, yet the daily product doesn't have to become a cockpit built from every procurement questionnaire the company has ever received.

Enterprise software gets enterpriseified in the name of growth. Controls become visible, exceptions become configuration, and large deals leave another switch behind.

My preferred rule is narrower: enterprise capability should expand faster than everyday interface complexity.

## The enterprise buyer and the daily user are buying different things

A security team may need SAML, SCIM, auditability, domain controls, and contractual commitments before a purchase can happen. An administrator needs migration tools, organization structure, permissions, and enough control to operate the system across hundreds or thousands of people.

The person opening an issue on Tuesday morning wants the tool to be fast and unsurprising, and those needs shouldn't automatically share the same surface area.

Linear's current pricing is a useful example. Its Enterprise plan adds administrative and security capabilities around the core product rather than replacing the core workflow with an entirely different enterprise edition.

Its published customer stories show the same product operating across sizable organizations. Automattic moved roughly 600 product, engineering, and design staff, while OpenAI expanded from an initial trial to thousands of users.

The interesting product mechanism is containment: put complexity where the person who needs it can reach it, whether that's administration, policy, migration, reporting, identity, procurement, or support.

Don't make every user carry those requirements through every ordinary interaction, because a product can support a complicated company without requiring each click to acknowledge that complication.

## Customization has a carrying cost

Enterprise customers will ask for flexibility, sometimes because their process genuinely requires it and sometimes because the old system already trained the organization to expect a knob.

Every knob has descendants: defaults, permissions, documentation, migration behavior, API semantics, support knowledge, test coverage, and some answer when two teams configure it differently.

The original feature request may be one sentence; its maintenance family gets large.

That doesn't make customization bad. It makes customization a product investment with a carrying cost, which is a different conversation from whether one customer asked loudly enough.

I'd separate requests into two buckets before building another setting. Some represent a real policy boundary, regulatory requirement, organizational structure, or integration constraint; others try to reproduce local habits that the new product may be better off refusing.

The second bucket deserves more skepticism.

Remote's published Linear case study describes its previous project-management tooling becoming harder to maintain as the company grew, with teams spending hours rearranging roadmaps, cleaning labels, and managing process.

Whether another company would see the same result is an open question. The failure mode is familiar, though: flexibility accumulates until maintaining the tool becomes part of the job.

That's configuration gravity, and once enough local process is encoded, removing a field can feel like changing company policy rather than deleting software clutter.

## Selling upmarket without dragging the product uphill

Linear's August 26 tender announcement says the company has passed $100 million in ARR and completed a $99 million employee tender at a $2.5 billion valuation.

Those figures don't prove that simplicity caused the growth.

Pricing, market timing, execution, brand, product quality, and the broader shift in software development are tangled together.

They do make one common assumption worth challenging: selling to larger companies doesn't automatically require turning the daily experience into enterprise software's traditional visual dialect.

Enterprise readiness is partly invisible when identity works, migration is credible, administrators have controls, security teams can inspect what they need, and procurement can buy the thing.

Support also needs to know who answers when the rollout gets weird, while the ordinary user should still be able to open the product and do the ordinary job.

I've written about [API deprecation as a customer migration problem](/blog/2026/08/24/api-deprecation-customer-migration/), where platform teams have to account for work that happens inside somebody else's organization.

Enterprise adoption has the same external dependency, but the answer shouldn't be pouring every rollout concern into the main interface.

It also connects to [product roadmaps as portfolios of different commitments](/blog/2026/08/11/a-roadmap-is-a-portfolio-of-bets-not-a-list-of-promises/). A contractual enterprise requirement may be a genuine promise; a requested workflow preference is still allowed to be a bet.

The product test I'd use is simple: if we add this enterprise capability, who should notice it?

Sometimes the answer is every user. I hope it isn't. Enterprise software has to fit a large organization without making every user feel the weight of one.

## Sources

- [Linear: Sharing Linear's growth with the people building it](https://linear.app/now/sharing-growth-with-the-people-building-linear)
- [Linear: Pricing and Enterprise features](https://linear.app/pricing)
- [Linear: How Automattic migrated to Linear and unified its product teams](https://linear.app/customers/automattic)
- [Linear: Remote switched its 1,000-person team to Linear](https://linear.app/customers/remote)
- [Linear: Why OpenAI chose Linear and scaled to 3,000 users](https://linear.app/customers/openai)
