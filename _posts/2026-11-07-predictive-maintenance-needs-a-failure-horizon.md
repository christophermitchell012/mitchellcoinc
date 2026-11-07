---
layout: post
title: "Predictive Maintenance Needs a Failure Horizon"
date: 2026-11-07 10:46:02 -0600
category: Product + Analytics
description: "Predictive maintenance alerts should reveal whether a team has enough time to plan a safe intervention, not merely detect an anomaly."
read_time: "5 min read"
---

A vibration model flags a bearing on Friday morning. The maintenance planner does not need another red badge. She needs to know whether the machine can finish its current run, whether a technician must come today, and whether a replacement is available.

Anomaly detection can tell her that the signal looks unusual. That is useful, but it stops one step before the operational decision.

Predictive maintenance becomes a product when it estimates a failure horizon: the interval between a trustworthy warning and the point when continued operation becomes unsafe or uneconomic.

That horizon creates room to schedule labor, order parts, protect production, and choose a controlled shutdown. Without it, prediction can become a faster way to create uncertainty.

## An anomaly is not yet a maintenance plan

Many monitoring products lead with an anomaly score. The score may be statistically sound and still leave the operator stranded.

A value of 0.91 does not say whether the asset has three hours or three weeks. It does not identify the likely failure mode, the operating conditions that could accelerate damage, or the consequence of waiting.

The product must connect four moments:

- The first detectable change in condition.
- The time when a prediction becomes reliable enough to use.
- The last practical moment to begin the intervention.
- The expected failure point or safety limit.

The distance between the second and third moments is the action window. That is the portion of the forecast an operator can spend.

If a plant needs five days to approve work, receive a bearing, and arrange access, a two-day warning is accurate but late. A thirty-day warning that changes every shift may be early but unusable.

## Measure timing, not only classification

Precision and recall still matter. False alerts consume attention, while missed failures create obvious risk. Yet those metrics treat every correct alert as equally valuable.

Maintenance teams experience a different distribution. Some alerts arrive early enough to plan. Some arrive after the cheapest options have disappeared. Others linger without a clear deadline, then become background noise.

NASA researchers developed prognostic metrics that evaluate when remaining-useful-life estimates enter an acceptable accuracy band. Their idea of a prognostic horizon is important because it rewards a forecast for becoming useful early, not merely for ending near the right answer.

A product team can translate that idea into an operating scorecard. For each alert, record its action window, forecast range, final outcome, intervention cost, and whether the team changed the plan.

I would also separate alerts into early and stable, early but unstable, actionable, late, false, and unresolved. Those categories reveal failure modes that one accuracy percentage hides.

## Show a range and the assumptions behind it

Remaining useful life is not a countdown clock. Load, temperature, duty cycle, maintenance history, and sensor quality can move the estimate.

A product should therefore show a range, not a theatrical timestamp. It should also expose the assumptions that matter to the range.

For example:

> Estimated intervention window: 6 to 11 days. Continued high-load operation may reduce the lower bound. Estimate based on vibration growth across 42 operating hours.

That message is less visually tidy than “failure in 8.4 days.” It is more honest and more useful.

The interface should make trend changes visible too. If the lower bound falls from nine days to four, the operator needs to see why the priority changed. Silent revisions teach people to distrust the model.

I call the gap between model timing and the operation's required lead time **horizon debt**. It accumulates when a team improves detection while leaving approvals, parts, access, and staffing outside the product design.

## Design the alert around the next commitment

The alert should carry enough context for a person to make the next safe commitment. That usually includes the asset, suspected failure mode, consequence, forecast range, confidence, relevant conditions, recommended inspection, owner, and decision deadline.

Not every recommendation should be a repair. The right next step may be collecting a better vibration sample, reducing load, checking lubrication, or moving production to another line.

This is where predictive maintenance joins the broader operating system. An [operational metric needs an owner, threshold, and first action](/blog/2026/08/02/every-operational-metric-needs-an-owner-threshold-and-action/). A failure forecast needs the same contract, plus time.

Feedback must close the loop. The technician should record what was found, what action was taken, and whether the forecast changed the schedule. That evidence can improve the model, but it also tests the product promise.

The useful question is not whether the system detected degradation. It is whether the warning arrived while the team still had a good choice.

## Sources

- [NASA: Evaluating Algorithm Performance Metrics Tailored for Prognostics](https://ntrs.nasa.gov/api/citations/20090033821/downloads/20090033821.pdf)
- [NIST: Manufacturing Machinery Maintenance](https://www.nist.gov/el/applied-economics-office/manufacturing/topics-manufacturing/manufacturing-machinery-maintenance)
- [U.S. Department of Energy: Operations & Maintenance Best Practices Guide](https://www.energy.gov/sites/prod/files/2020/04/f74/omguide_complete_w-eo-disclaimer.pdf)
