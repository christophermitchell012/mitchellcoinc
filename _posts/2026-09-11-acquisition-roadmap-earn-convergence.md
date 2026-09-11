---
layout: post
title: "An Acquisition Roadmap Should Earn Convergence"
date: 2026-09-11 10:14:06 -0500
category: Product Strategy
description: "Product acquisitions should preserve working workflows, connect useful capabilities, and converge only when customers benefit enough to switch."
read_time: 4 min
---

Two products can become one company long before they should become one product.

Envestnet's planned acquisition of Vestmark is a useful example because the September 9 announcement puts some unusually clear boundaries around integration. Vestmark supports more than $2 trillion across five million-plus accounts, while Envestnet reports about $8 trillion in platform assets. More interesting to a product manager, though, is what the companies aren't doing after the deal closes. Customers won't be forced to migrate because of the transaction, and both existing product roadmaps will keep moving.

Write that constraint down before drawing the new architecture.

When a platform acquisition closes, "integration" is dangerously vague because it can describe changes with radically different customer costs. A shared login, data moving between products, cross-product workflows, a common API, and one application replacing another are all technically integration. Product teams need a more useful sequence: preserve first, connect where there's customer value, and converge only when switching costs justify it.

Preservation means existing customers keep the workflows, APIs, permissions, and operating assumptions they already depend on while the companies combine behind them. In wealth technology, where portfolio management and trading systems touch real money, forced migration isn't merely an annoying redesign for an administrator. It can create testing, training, compliance review, and operational work before the customer receives a single new capability.

Connection is different, and the Envestnet announcement gives concrete examples of what that could mean without requiring a wholesale platform move. Vestmark clients are expected to gain access over time to Tamarac and MoneyGuide capabilities, while Envestnet clients can gain Vestmark's trading, rebalancing, and tax-transition capabilities. The products don't need to pretend they were secretly one architecture all along; sometimes a boring adapter is excellent product strategy.

Convergence comes later, selectively, when customers benefit enough to pay the switching cost rather than because an internal consolidation spreadsheet looks untidy. Shared identity might make sense early. A unified data model could take longer, and a mature trading workflow might remain separate indefinitely. Replacing that workflow simply because the org chart changed would be PowerPointification with a login screen.

![Acquisition integration ladder showing Preserve, Connect, and Converge](/assets/images/acquisition-integration-ladder.svg)

This sequencing also changes the acquisition KPI because "percent migrated" quietly assumes migration itself is the desired customer outcome. Better measures follow the layer: retained workflows during preservation, successful cross-product tasks during connection, then voluntary adoption when convergence actually removes customer work. Internal migration cost still matters. It just isn't customer value.

There is a legitimate counterargument: maintaining two products creates duplicate engineering, support, infrastructure, security, documentation, sales-training, and compliance work, sometimes for years, while finance keeps asking why the promised consolidation hasn't appeared yet. The mistake is treating those internal costs as proof that customers should absorb migration costs immediately, especially when the acquired product is already working.

I've worked on enough platform and integration problems to distrust diagrams where two boxes become one box with an arrow labeled "synergy." That arrow is usually where the product work lives, along with the ugly dependencies the acquisition deck didn't have room to draw.

Envestnet and Vestmark have publicly committed to no forced migration while continuing both roadmaps, so whether that holds through integration is the interesting product test. An acquisition roadmap should earn convergence by removing customer work; until then, connect the products without making customers reorganize their world because your company reorganized its own.

This is the same reason [build-vs-buy decisions should price the product freedom you lose](/blog/2026/08/31/build-vs-buy-price-product-freedom/): the architecture bill eventually lands on somebody's desk.

## Sources
- [Envestnet to acquire Vestmark](https://www.vestmark.com/press-releases/envestnet-to-acquire-vestmark-extending-its-capabilities-to-meet-the-advisor-markets-growing-demand-for-increasingly-sophisticated-trading-and-tax-solutions)
- [WealthManagement: Envestnet to acquire wealthtech provider Vestmark](https://www.wealthmanagement.com/advisor-support-platforms/envestnet-acquires-vestmark-in-wealth-tech-deal)
