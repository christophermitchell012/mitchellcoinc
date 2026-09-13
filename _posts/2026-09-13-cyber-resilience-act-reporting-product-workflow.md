---
layout: post
title: "Cyber Resilience Act Reporting Is a Product Workflow"
date: 2026-09-13 10:34:00 -0500
category: "IoT + Product Strategy"
description: "Cyber Resilience Act reporting puts security evidence on a clock. Product teams need traceable incident data before the 24-hour window starts."
read_time: "4 min read"
---

A 24-hour reporting deadline has a funny way of turning an organizational chart into a product requirement.

On September 11, the EU Cyber Resilience Act's reporting rules became applicable to manufacturers of products with digital elements. An actively exploited vulnerability or severe security incident now starts a clock immediately: an early warning within 24 hours, a fuller notification within 72 hours, then a final report on a later deadline depending on the event and report type. ENISA launched its Single Reporting Platform the same day so manufacturers can report once to the appropriate authorities.

That sounds like compliance plumbing, but for a product team it is also an information architecture problem with a stopwatch attached.

![Cyber Resilience Act reporting clock showing awareness, 24-hour warning, 72-hour notification, and final reporting](/assets/images/cra-reporting-clock.svg)

## Start the clock where awareness actually happens

The dangerous word in the rule is “aware.” Security may first see an alert in a SIEM, support may hear from a customer, engineering may reproduce a defect, or a supplier might disclose a vulnerable component. Different queues turn reporting into archaeology.

I’d map the evidence chain before designing another compliance dashboard: product and version, affected customers or geographies, vulnerability identity, exploit evidence, severity, mitigation status, and who knows what. The point isn’t to collect every possible field immediately. It’s to make the first required decision from evidence the company can trace.

This resembles a crossword more than a form. You rarely fill the whole grid in order; one answer gives you letters that constrain another. Incident reporting should work similarly, with verified facts filling downstream fields while unknowns remain visibly unknown instead of being guessed into completeness.

## Design for progressive certainty

A 24-hour warning and a 72-hour notification imply different information states, and product systems should reflect that distinction explicitly.

The early workflow needs enough evidence to identify the product, event, likely impact, and responsible reporting path. Later stages can add investigation results, affected versions, corrective measures, and other details as they become known. Forcing the first reporter to complete a giant “final” form creates a predictable failure mode: people wait for certainty while the clock keeps moving.

The Single Reporting Platform helps at the external boundary because one submission can reach the relevant authorities, but inside the company someone still has to assemble the facts.

That makes incident data a product surface, where asset inventories, software bills of materials, release history, customer deployment records, vulnerability tracking, and support systems feed a time-bounded workflow. A missing version-to-customer relationship isn't merely untidy data once a reporting deadline depends on it.

There’s a counterweight. Automating evidence collection can create false confidence when stale inventory or an incomplete dependency graph produces a clean-looking answer. Every imported fact should retain its source and timestamp, especially when a human may need to defend the notification later.

I’ve written before that [data products break when meaning changes](/blog/2026/09/01/data-products-break-when-meaning-changes/). Regulatory reporting adds another constraint: meaning also has to arrive on time.

The product test is simple enough to state: when the 24-hour clock starts, can the team reconstruct what happened without opening twelve tabs and starting a Slack scavenger hunt? If not, the reporting problem began long before the incident.

## Sources

- [European Commission: Cyber Resilience Act reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- [ENISA: The CRA Single Reporting Platform is launched](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)
- [ENISA: Single Reporting Platform FAQ](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)
