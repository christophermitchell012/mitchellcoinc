---
layout: post
title: "Synthetic Data Is Only as Good as Its Joins"
date: 2026-09-16 10:08:00 -0500
category: "Data Products + Product Strategy"
description: "Synthetic data becomes useful test infrastructure when relationships, constraints, and failure modes survive across the database, not just individual rows."
read_time: "4 min read"
---

A test database can look perfectly reasonable one table at a time and still be nonsense when the joins begin.

DataCebo released SDV 2.0 on September 15. The company says its software builds generative relational models of interconnected enterprise databases, then uses those models to create synthetic data for testing and other uses without moving production data outside the customer's environment.

That sounds like a data-science feature, although for a product team I think it's closer to test infrastructure.

A customer table with plausible ages and ZIP codes isn't enough when the application depends on orders, products, payments, entitlements, and support records agreeing with one another. Primary and foreign keys have to connect, cardinalities matter, and business rules hide in those relationships until staging breaks on Thursday afternoon.

## A synthetic row isn't the product

SDV's metadata describes tables, columns, data types, primary keys, foreign keys, and relationships. Its documentation explicitly treats that metadata as ground truth, and recommends checking automatically detected metadata because inference isn't guaranteed to be complete or correct.

That distinction matters. Generating believable rows is useful for screenshots and simple component tests; generating a believable database supports integration testing, performance work, scenario simulation, and safer development where production records are too sensitive to copy around casually.

I've spent enough time around SQL-backed products to distrust a clean-looking table on sight because the interesting bugs, the expensive and deeply annoying ones, usually wait one JOIN away.

![Synthetic data quality diagram showing plausible rows becoming useful test data only when relationships and constraints survive](/assets/images/synthetic-data-relational-integrity.svg)

Referential integrity comes first. SDV's own multi-table guidance says synthesizers work best when foreign-key references resolve to existing primary-key values, and it provides tooling to remove unknown references before modeling.

The harder layer is semantic integrity: whether combinations that are technically valid still make sense together. A generated order might reference a real synthetic customer and product yet violate a discount rule, subscription state, regional restriction, or sequence that the application quietly assumes.

## Test the database like a product dependency

I'd evaluate synthetic data with the same suspicion I bring to an external API, starting with schema validity and referential integrity. Then I'd test distributions, cross-table relationships, edge cases, and the downstream decisions the data is supposed to exercise.

For product managers, this changes the acceptance criterion because “we generated 10 million safe test rows” says little about whether those rows reproduce the failure modes engineering needs.

My kids can generate synthetic household data indefinitely: apparently every missing snack was consumed by an unnamed sibling, and the records are plentiful. Referential integrity remains under investigation, along with the location of several granola bars.

Synthetic data earns its keep when developers can stop borrowing production data without making their test environment pleasantly fake. The useful unit isn't a synthetic row; it's a synthetic system that still behaves badly in the same important places developers need to find before customers do.

Related: [Data Products Break When Meaning Changes](/blog/2026/09/01/data-products-break-when-meaning-changes/).

## Sources

- [DataCebo: SDV 2.0 release](https://www.prnewswire.com/news-releases/datacebo-releases-sdv-2-0-for-building-generative-relational-models-of-enterprise-data-302879009.html)
- [SDV documentation: Metadata](https://docs.sdv.dev/sdv/concepts/metadata)
- [SDV documentation: Cleaning multi-table data](https://docs.sdv.dev/sdv/multi-table-data/data-preparation/cleaning-your-data)
