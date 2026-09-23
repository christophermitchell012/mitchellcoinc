---
layout: post
title: "When Hosting Location Becomes a Product Feature"
date: 2026-09-23 10:54:30 -0500
category: "Product Strategy + Enterprise Infrastructure"
description: "Customer-hosted software changes product scope. Treat data location, control boundaries, upgrades, and support economics as discovery inputs."
read_time: "3 min read"
---

A product requirement can arrive disguised as a deployment diagram, especially when the customer operates infrastructure that can't casually leave its own boundary.

Ericsson announced NetCloud Private today, a customer-hosted version of its cellular lifecycle-management platform for government agencies, critical infrastructure, and other regulated organizations. Network-management and telemetry data can stay inside an on-premises data center or a trusted in-country cloud, while administrators still manage distributed Cradlepoint routers centrally.

The boundary has moved. Hosting location becomes a feature customers can reject a purchase over, even when every visible workflow already meets their needs.

## The deployment model belongs in discovery

I've worked on defense and enterprise products where the technical question wasn't simply whether software worked inside the intended workflow and environment. Where it ran, which network boundary it crossed, who could administer it, and what left the customer's environment could decide whether deployment happened at all.

Those constraints are easy to discover late because conventional product discovery tends to center the user doing a task. Regulated infrastructure adds another user of sorts: the organization's operating model, with residency rules, security controls, disconnected environments, procurement requirements and ownership rules that don't care how pleasant the dashboard is or how quickly the normal cloud version can be provisioned.

The design is concrete. NetCloud Private keeps centralized onboarding, configuration, monitoring, troubleshooting, and software updates for thousands of distributed routers, but packages those capabilities for customer-controlled infrastructure without forcing the management data back through Ericsson's public-cloud operating model. Ericsson says the software can run in the customer's data center or an in-country provider's environment, and global availability is planned for October.

The Gulf deployments make the distinction useful rather than theoretical for buyers. In the UAE, a communications service provider will host NetCloud Private for multiple enterprise customers; in Saudi Arabia, a customer will host it for its own operations. Same product, different boundary.

## Private deployment creates a second cost curve

Product teams sometimes treat self-hosting as SaaS with a different installer and a few extra deployment notes. It isn't quite that simple once the vendor loses direct control of the runtime.

Once software moves into somebody else's environment, the team inherits version skew, upgrade coordination, capacity assumptions, certificate handling, backup expectations, local infrastructure dependencies, and support cases with thinner observability and fewer direct ways to inspect the runtime. Every convenience the SaaS control plane previously supplied has to be replaced, constrained, or explicitly abandoned.

That cost can still be rational for both sides of the purchase. A customer who can't send network telemetry to a public cloud isn't comparing private deployment with SaaS convenience; they're comparing it with no purchase, a different vendor, or local tools.

This is why [product tiers should be separated by real constraints](/blog/2026/09/02/product-tiers-constraints-draw-the-line/), not a feature-checkbox staircase. Deployment topology is about as real a constraint as you can get in enterprise software.

I'd put four things into discovery before promising a private edition: the exact data that must remain local, permitted outbound connections, upgrade tolerance, and infrastructure ownership during failures. Those answers shape architecture and support economics before they shape packaging, which is an expensive sequence to discover after the contract is signed.

The useful product insight in NetCloud Private is smaller than “digital sovereignty is growing,” and more actionable for a product team. Some customers aren't buying your software alone; they're also buying the right to decide where the software ends.

If that boundary appears only in the security questionnaire, product discovery found it too late.

## Sources

- [Ericsson: NetCloud Private for customer-controlled Wireless WAN operations](https://www.ericsson.com/en/press-releases/5/2026/ericsson-netcloud-private-boosts-gulf-wireless-wan)
- [Ericsson: NetCloud Private product overview](https://cradlepoint.ericsson.com/products/netcloud/netcloud-private/)
