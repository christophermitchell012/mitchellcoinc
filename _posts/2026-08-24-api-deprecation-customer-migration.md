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

This month offers a useful pair of examples. Contentful deprecated two legacy usage endpoints on August 18 and gave customers until February 28, 2027, before they return `410 Gone`. Schiphol is running its old and new API platforms in parallel until October 1 while customers change endpoints, move from static API keys to JWT-based OAuth 2.0 authentication, request access, and validate integrations in acceptance.

Those aren't just technical transitions. They're customer migrations, and I'd manage them more like product launches than cleanup projects.

## The migration funnel I'd want on day one

If I owned an API deprecation, the first dashboard I'd ask for wouldn't start with error rate. It would start with customer state.

| Migration state | What I need to know |
| --- | --- |
| Not identified | Can we tell which customers still call the legacy API? |
| Identified | Do we know the technical and business owner? |
| Aware | Have they actually received and acknowledged the change? |
| Testing | Are they sending traffic to the replacement in a non-production environment? |
| Partial | Is some production traffic still hitting legacy endpoints? |
| Migrated | Has legacy traffic reached zero for a meaningful period? |
| Blocked | What dependency prevents migration, and who owns removing it? |

That funnel changes the conversation.

A release note can tell me the new API exists. It can't tell me whether the customer who sends 18% of legacy traffic has budgeted the engineering work, whether their security team approved the new authentication flow, or whether they discovered a behavior difference in testing.

This is one place where product management earns its keep. The dependency isn't sitting entirely in your backlog anymore.

## Compatibility is a budget you spend

There's an obvious counterargument: avoid breaking changes whenever possible.

I agree. Stable contracts are part of the value of an API. Every migration consumes customer engineering time, creates regression risk, and competes with work the customer would rather be doing.

But permanent backward compatibility has a cost too. Old authentication schemes, duplicate endpoints, legacy data models, and special-case behavior accumulate. Eventually, the platform team is maintaining several versions of history at once.

So I'd treat compatibility as a budget rather than a religion.

Spend it carefully. When a breaking change is worth the cost, make the customer burden explicit before approving it:

> customers affected × estimated migration effort × consequence of failure

That isn't a financial model. It's a forcing function. A change affecting twelve sophisticated partners with a clean SDK upgrade is a different product decision from one affecting 4,000 long-tail integrations whose owners you can't reliably contact.

The replacement API can be objectively better and still be a bad migration.

## The shutdown date needs evidence

I like that Schiphol explicitly supports running both platforms in parallel during the migration window. Contentful similarly gives customers more than six months between deprecation and removal of its legacy usage endpoints. Those windows create room for migration, but time by itself doesn't create readiness.

Before shutdown, I'd want evidence such as legacy traffic trending toward zero, high-value customers confirmed migrated, known blockers classified, support volume understood, and a deliberate decision for any remaining stragglers.

For a high-risk transition, I'd also consider a brownout: temporarily disable the old version before the permanent cutoff. StatusGator used progressively longer v2 API brownouts this summer ahead of its September 1 retirement date. That's a useful technique because dormant dependencies have a habit of becoming visible only when they fail.

The key is that the shutdown date shouldn't be the first time you discover who was still depending on the old system.

This connects to the way I think about [product roadmaps as different kinds of commitments](/blog/2026/08/11/a-roadmap-is-a-portfolio-of-bets-not-a-list-of-promises/). An API retirement date may be a real external commitment, but the migration plan underneath it still needs evidence. It also resembles [MVP strategy built around reducing uncertainty](/blog/2026/07/18/an-mvp-should-remove-uncertainty-not-maximize-features/): early migrations should expose the compatibility assumptions most likely to hurt the broader rollout.

There's a subtle product shift here. The API team's unit of completion isn't "replacement shipped." It's "customer dependency moved."

That means documentation, telemetry, developer support, compatibility tooling, account outreach, test environments, and migration status all belong in the plan. None of them are glamorous. Neither is explaining to a major customer why their integration stopped at midnight.

So, who owns the customer migration?

If the answer is "the customer," the deprecation plan is missing half the product.

## Sources

- [Schiphol API Team: Developer Portal Migration Notice](https://developer.partner.schiphol.nl/news-and-updates/developer-portal-migration-notice)
- [Contentful: API Changes and legacy Usage API deprecation](https://www.contentful.com/developers/api-changes/)
- [StatusGator: Time to move to the v3 API](https://statusgator.com/blog/time-to-move-to-the-statusgator-v3-api-what-v2-users-need-to-know/)
