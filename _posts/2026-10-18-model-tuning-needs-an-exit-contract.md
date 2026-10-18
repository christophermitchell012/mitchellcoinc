---
layout: post
title: "Model Tuning Needs an Exit Contract"
date: 2026-10-18 10:56:47 -0500
category: Product Strategy
description: "An exit contract gives model tuning a fixed objective, resource ceiling, stopping rule, and promotion bar before the first trial starts."
read_time: 5 min
---

Forty-two model trials have finished. Trial 31 leads the chart by 0.4 percentage points, trial 38 costs half as much to serve, and six runs are still consuming GPUs. The team has found better configurations. It has not found a reason to stop.

That gap turns hyperparameter optimization into an open-ended product expense. Search tools can sample intelligently, end weak trials early, and distribute work across a cluster. None of them can decide how much improvement is worth another day, whether latency matters more than accuracy, or what evidence makes a candidate safe to release.

Before the first trial starts, write an **exit contract**: a compact agreement that defines the target, the constraints, the resource ceiling, the stopping rule, and the promotion bar.

## A leaderboard is not an objective

Most tuning jobs begin with one metric because software needs a direction such as minimize validation loss or maximize recall. Products usually have several obligations. A fraud model may need better recall without exceeding a false-positive limit. Meanwhile, a vision model can gain accuracy while missing its device latency target, and a ranking model can improve offline relevance without making a measurable difference to customers.

The contract should name one primary objective and turn the other obligations into constraints. Maximizing recall is incomplete. Maximizing recall at or below a 1.5 percent false-positive rate, 80 milliseconds of p95 latency, and the current serving cost creates a decision boundary.

It also prevents metric substitution. When the chosen score stops improving, teams often celebrate a secondary number that moved instead. That may reveal something useful. It should not silently rewrite the job.

## Put two stop rules in the same contract

Optimization libraries already provide a trial-level stop. Optuna calls this pruning: a training run reports intermediate objective values, and the pruner can terminate an unpromising trial. Ray Tune's asynchronous successive-halving scheduler adds explicit controls for maximum progress, a grace period, and a reduction factor.

Those mechanisms decide whether a trial should keep running. The product team still needs a study-level decision about whether the search should continue at all.

Use both:

1. **Trial stop:** end a configuration when its intermediate evidence cannot justify more resources.
2. **Study stop:** end the search when it hits the first agreed boundary: a compute ceiling, wall-clock deadline, target score, or diminishing-return threshold.

A useful diminishing-return rule is deliberately plain: stop when the best eligible candidate has not improved the primary metric by at least the minimum valuable delta across the last fixed batch of completed trials. The delta should reflect product value, not floating-point motion.

Google's Vertex AI study specification makes the distinction visible. It supports automated rules for stopping pending trials and a separate study stopping configuration. Tooling can execute both layers, but the team must supply the judgment behind them.

## Budget the search in product units

Using eight GPUs describes capacity, not a budget. The exit contract should state the maximum GPU-hours, dollar cost, elapsed time, and completed trials. One limit may bind before the others.

Now add the opportunity cost. A tuning cluster can delay evaluation work, consume scarce engineering attention, or block another team's experiment. Those costs belong beside infrastructure spend because they change whether the next batch is rational.

This is where a small dashboard earns its place. Show cumulative cost, eligible best score, constraint violations, improvement per batch, and remaining budget. Do not plot only the winning line. A flat best score with rising spend is the signal the contract exists to catch.

## Promotion is a new decision

The top trial should not become the production model automatically. Search has optimized against evidence it has already seen, and repeated comparison can reward noise. The candidate still needs a clean promotion test on untouched data, plus checks for latency, memory, cost, calibration, and segment-level regressions.

That is the same reason a [self-improving AI system needs a holdout set](/blog/2026/10/12/self-improving-ai-needs-a-holdout-set/). Optimization evidence chooses what deserves a final test. It is not the final test.

The promotion bar should be written before results arrive. Require the minimum valuable improvement, every hard constraint, a reproducible artifact, and an owner willing to sign the release decision. A candidate that misses one of those conditions can still teach the team something. It does not ship.

More trials are easy to request because their cost arrives gradually and their promise stays vague. An exit contract makes the trade visible before momentum takes over. The search ends when the product case ends.

## Sources

- [Optuna documentation: Efficient optimization algorithms](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html)
- [Ray documentation: AsyncHyperBandScheduler](https://docs.ray.io/en/latest/tune/api/doc/ray.tune.schedulers.AsyncHyperBandScheduler.html)
- [Google Cloud documentation: Vertex AI StudySpec](https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1StudySpec)
