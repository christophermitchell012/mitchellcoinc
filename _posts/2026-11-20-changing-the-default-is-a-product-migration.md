---
layout: post
title: "Changing the Default Is a Product Migration"
date: 2026-11-20 10:16:15 -0600
category: Product Operations
description: "Changing a product default creates cohorts, inherited values, and migration risk. Design the rollout around provenance, choice, and reversibility."
read_time: 6 min
---

The team changed the reminder default from seven days to one. New accounts behaved exactly as planned. Existing accounts did not change, except for a small group that had never saved the setting and suddenly began receiving reminders six days earlier.

Support saw one label, three behaviors, and no reliable way to explain which rule had won.

A default looks like a value. In a mature product, it is closer to a policy with a history. Changing it can divide customers by creation date, configuration state, account hierarchy, application version, and whether somebody once clicked Save without changing anything.

That is migration work, even when no database column moves.

## First decide who receives the new default

The phrase “change the default” hides the most important product decision. The team must decide whether the new value applies only to objects created after launch, to every object without an explicit choice, or to everyone regardless of prior behavior.

Those populations are not interchangeable. A sensible plan separates at least four states:

- **New:** the object does not exist yet.
- **Inherited:** the object follows a parent, organization, or system policy.
- **Implicit:** the object has no stored choice and receives a computed fallback.
- **Explicit:** a person or administrator selected a value.

Explicit choices usually deserve the strongest protection. MDN makes the same distinction for language selection: a request header is a hint when no better signal exists, and it should not override a language the user chose directly.

The product rule should therefore name precedence, not merely a number. For example, user choice can beat workspace policy, workspace policy can beat the system default, and the system default can fill only an otherwise empty state.

## Existing records carry yesterday's decision

Defaults enter data models in two common ways. A computed default is evaluated when the product reads an empty field. A materialized default is written into the record when the object is created.

Change a computed default and old empty records may change immediately. Change a materialized default and old records remain frozen until a migration rewrites them. A product can contain both patterns at once, which produces **default archaeology** when nobody recorded where a value came from.

GitHub exposes the cohort boundary clearly. Its account setting changes the default branch name for new repositories. Existing repositories have a separate operation. The word “default” does not imply retroactive change.

Kubernetes offers the more technical warning. Its API server fills certain omitted fields when an object is created. Later patch requests do not automatically recalculate those stored defaults unless the fields are explicitly cleared. A nearby field can change while the old derived value remains, sometimes creating an invalid combination.

The broader lesson is simple: absence, inheritance, and an explicit value that happens to equal the default are three different product states.

## Show the effective value and its source

An administrator should not need a database query to learn why a setting has its current value. The interface should show both the effective value and its provenance.

A useful detail view might say:

- Reminder window: one day.
- Source: inherited from North America workspace policy.
- System default: three days.
- Local override: none.
- Last policy change: November 20 by account administrator.

That explanation matters when the same visible value can come from several layers. It also makes support safer. An agent can fix the actual controlling rule instead of changing a child record that will be overwritten again at the next synchronization.

APIs and exports need the distinction too. Return the effective value for ordinary use, but provide source and override state where administrators reconcile configuration. Otherwise customers cannot tell whether exporting and reimporting a record will preserve its behavior.

## Roll out the default like a migration

Start with an inventory. Count records by explicit, implicit, and inherited state. Break the counts down by account tier, client version, geography, and any policy layer that can alter the result. Then simulate the proposed precedence rules against a production-shaped snapshot.

The rollout plan should state:

- Which cohorts change automatically.
- Which choices remain untouched.
- How customers will preview affected records.
- Whether an administrator can opt out or defer.
- What event records the change.
- How the team will reverse it without erasing later choices.

That last condition is easy to miss. A rollback should restore only values changed by the migration. It should not overwrite a choice made after launch. Store the prior state, migration identifier, applied rule, and timestamp so reversal can distinguish product action from customer action.

This resembles [API deprecation as a customer migration problem](/blog/2026/08/24/api-deprecation-customer-migration/). Both changes alter a contract that other people have already built behavior around. A quiet setting can carry as much operational dependency as a public endpoint.

Measure the rollout through support contacts, override rates, task failures, policy conflicts, and the percentage of affected records whose provenance is known. A low complaint count is weak evidence if customers cannot see that their behavior changed.

Defaults are valuable because they let people move without answering every question. That convenience depends on restraint. When the default changes, the product should preserve explicit intent, expose the winning rule, and migrate existing behavior deliberately rather than letting history choose at runtime.

## Sources

- [Managing the default branch name for your repositories](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-default-branch-name-for-your-repositories), GitHub Docs.
- [Accept-Language header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language), MDN Web Docs.
- [Declarative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/), Kubernetes Documentation.
