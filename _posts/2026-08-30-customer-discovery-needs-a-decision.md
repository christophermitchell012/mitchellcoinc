---
layout: post
title: "Customer Discovery Needs a Decision Before an Interview"
date: 2026-08-30 10:25:00 -0500
category: Customer Discovery + Product
description: "Customer discovery works better when research starts with a decision. Define what evidence could change the roadmap before scheduling interviews."
read_time: "4 min read"
---

## TL;DR

Customer discovery gets expensive when every interview creates another interview instead of a decision. Before recruiting participants, write down what evidence would change the roadmap, narrow the problem, or kill the idea; research without a decision boundary can become very thoughtful procrastination.

GitLab's current handbook treats customer discovery as a continuous product-management activity, recommending dedicated discovery meetings, continuous interviews, documented findings, and adjustments to strategy, epics, and personas afterward. I like the continuity, although the dangerous word is continuous.

A team can always learn one more thing from one more customer, particularly in B2B products where workflows vary by company, role, regulation, and installed software. Eventually the research repository gets richer while the product decision stays exactly where it started.

The fix is small: define the decision before scheduling the research.

## Give the interview somewhere to land

Suppose the open question is whether an integration deserves roadmap space. The useful research question isn't "Would customers use this integration?" because that invites polite speculation. Look instead for the existing workaround, how often the job occurs, who owns it, what breaks, and whether customers already spend money or labor getting around the gap. Those observations can change a decision, while enthusiasm is cheaper.

GOV.UK's service manual makes a similar distinction between evidence and assumption. It recommends researching how users currently accomplish a job, the problems they encounter, and what they need to reach the outcome. The guidance also says teams should turn unfounded assumptions into research questions, focus rounds on the highest-priority questions, and avoid research the team can't respond to.

That's easy to violate when customer interviews become a ritual, especially when "talk to customers" is treated as evidence of good product management regardless of what happens afterward. Notes accumulate and themes get tagged, yet nobody can point to the assumption that became weaker, the requirement that changed, or the roadmap item that disappeared.

I'd put a small decision header on a discovery plan: current belief, evidence that would strengthen it, evidence that would weaken it, and the decision waiting on the answer. Four lines are enough.

This doesn't turn qualitative research into a fake statistical test. Four interviews don't produce a population estimate, and repeated stories from a narrow recruiting channel can still mislead; the header simply makes the team's prior belief inspectable before memorable customer stories start tugging it around.

## Match the evidence to the question

GitLab's own Deploy Freezes example shows why mixing methods matters. The team surveyed more than 200 participants and interviewed five customers, using the combination to understand both demand and workflow context before shaping the feature.

Different questions deserve different evidence: interviews are good at mechanisms, language, constraints, and surprises, while surveys and product data can test prevalence at larger scale. A prototype can expose whether the proposed solution makes sense once somebody has to use it.

This connects to my earlier argument that [an MVP should remove uncertainty rather than maximize features](/blog/2026/07/18/an-mvp-should-remove-uncertainty-not-maximize-features/). Customer discovery has the same job upstream: spend research effort against the uncertainty most capable of changing what the team does next.

A research repository is useful memory, but it isn't the finish line. Before the next customer call, I'd want one sentence completed: "After this research, we may decide to ___." If nobody can fill in the blank, the calendar invite is probably early.

## Sources

- [GitLab Handbook: Product Processes](https://handbook.gitlab.com/handbook/product/product-processes/)
- [GitLab Handbook: Continuous Interviews](https://handbook.gitlab.com/handbook/product/product-processes/continuous-interviewing/)
- [GOV.UK Service Manual: Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service)
- [GitLab: Improving iteration and collaboration with user stories](https://about.gitlab.com/blog/how-we-utilize-user-stories-as-a-collaborative-design-tool/)
