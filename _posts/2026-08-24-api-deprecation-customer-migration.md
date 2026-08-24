---
layout: post
title: "API Deprecation: Who Owns the Customer Migration?"
date: 2026-08-24 09:00:00 -0500
category: APIs + Product
description: "API deprecation succeeds when customers actually migrate. Treat adoption, compatibility, testing, support, and shutdown readiness as product work."
read_time: "5 min read"
---

An API team can finish a migration months before its customers do.

That's the awkward economics of deprecation. Engineering ships the replacement, documentation publishes a migration guide, and the old endpoint is officially living on borrowed time. Meanwhile, customer code keeps calling it every minute of every day.

This month offers two examples. Contentful deprecated two legacy usage endpoints on August 18 and gave customers until February 28, 2027, before they return `410 Gone`. Schiphol is running its old and new API platforms in parallel until October 1 while customers change endpoints, move from static API keys to JWT-based OAuth 2.0 authentication, request access, and validate integrations in acceptance.

Those are customer migrations with technical work inside them. I'd manage them more like product launches than cleanup projects.

## The migration funnel I'd want on day one

If I owned an API deprecation, the first dashboard I'd ask for would show customer state. Error rate still matters; it just answers a different question.

| Migration state | What I need to know |
| --- | --- |
| Not identified | Can we tell which customers still call the legacy API? |
| Identified | Do we know the technical and business owner? |
| Aware | Have they actually received and acknowledged the change? |
| Testing | Are they sending traffic to the replacement in a non-production environment? |
| Partial | Is some production traffic still hitting legacy endpoints? |
| Migrated | Has legacy traffic reached zero for a meaningful period? |
| Blocked | What dependency prevents migration, and who owns removing it? |

Once the dashboard is organized this way, a release note stops being enough. It can tell me the replacement API exists. It can't tell me whether a customer still sending legacy traffic has budgeted the engineering work, whether its security team approved the new authentication flow, or whether testing uncovered a behavior difference.

At that point the product manager is dealing with dependencies outside the company's backlog. The customer's piece of the work lives inside somebody else's planning cycle, security review, or release calendar.

## Compatibility is a budget you spend

Breaking changes should be rare. Stable contracts are part of the value of an API, and every migration consumes customer engineering time and creates regression risk. The work also competes with things the customer would rather be doing.

Permanent backward compatibility has a cost too. Old authentication schemes, duplicate endpoints, legacy data models, and special-case behavior accumulate. Eventually the platform team is maintaining old versions of history alongside the current one.

I tend to think of compatibility as a budget because a breaking change spends customer time. That cost belongs in the decision.

When a breaking change is worth the cost, make the customer burden explicit before approving it:

> customers affected × estimated migration effort × consequence of failure

I wouldn't pretend that's a financial model. I use it because it forces the discussion onto the customer burden instead of the elegance of the new API. A partner base where every integration has a reachable owner and a clean SDK upgrade is one problem. A long tail of integrations with owners you can't reliably contact is another.

## The shutdown date needs evidence

I like that Schiphol explicitly supports running both platforms in parallel during the migration window. Contentful similarly gives customers more than six months between deprecation and removal of its legacy usage endpoints. Time helps, but it doesn't create readiness by itself.

Before shutdown, I'd want legacy traffic trending toward zero, high-value customers confirmed migrated, known blockers classified, support volume understood, and a deliberate decision for any remaining stragglers.

For a high-risk transition, I'd also consider a brownout: temporarily disable the old version before the permanent cutoff. StatusGator used progressively longer v2 API brownouts this summer ahead of its September 1 retirement date. Dormant dependencies have a habit of becoming visible only when they fail.

By the shutdown date, the stubborn dependencies should already be visible.

This connects to the way I think about [product roadmaps as different kinds of commitments](/blog/2026/08/11/a-roadmap-is-a-portfolio-of-bets-not-a-list-of-promises/). An API retirement date may be a real external commitment, but the migration plan underneath it still needs evidence. It also resembles [MVP strategy built around reducing uncertainty](/blog/2026/07/18/an-mvp-should-remove-uncertainty-not-maximize-features/): early migrations should expose the compatibility assumptions most likely to hurt the broader rollout.

For the API team, completion means `customer dependency moved`. Shipping the replacement is an earlier milestone.

Documentation, telemetry, developer support, compatibility tooling, account outreach, test environments, and migration status all belong in the plan. None of them are glamorous. Neither is explaining to a major customer why its integration stopped at midnight.

Who owns the customer migration?

If the answer is "the customer," the deprecation plan is missing half the product.

## Sources

- [Schiphol API Team: Developer Portal Migration Notice](https://developer.partner.schiphol.nl/news-and-updates/developer-portal-migration-notice)
- [Contentful: API Changes and legacy Usage API deprecation](https://www.contentful.com/developers/api-changes/)
- [StatusGator: Time to move to the v3 API](https://statusgator.com/blog/time-to-move-to-the-statusgator-v3-api-what-v2-users-need-to-know/)
