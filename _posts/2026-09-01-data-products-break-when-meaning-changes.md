---
layout: post
title: "Data Products Break When Meaning Changes"
date: 2026-09-01 10:42:00 -0500
category: Data Products + Product
description: "Data products need compatibility promises beyond schema. A pipeline can stay green while changed field meaning quietly breaks downstream decisions."
read_time: "4 min read"
---

Databricks updated its schema-enforcement documentation on August 25, and the mechanics are sensible: Delta Lake validates columns and types on write. Separate schema-evolution features can add new columns when producers change, while Snowflake can automatically add columns and relax NOT NULL constraints as incoming data changes.

Useful plumbing, although automatic schema evolution can make a product team feel safer than its consumers are.

## A green pipeline can carry a breaking change

Imagine a field called `revenue` keeps the same name and numeric type, so nothing fails at ingestion. Then the producer changes its definition from booked revenue to recognized revenue, or dollars become cents during a billing-system migration.

Nulls might also start appearing during a monthly reconciliation window. The schema survived; the product contract didn't.

Consumers build dashboards, forecasts, alerts, APIs, finance models, and ML features on meaning rather than column existence. Once another team writes logic against a field, semantics become part of the interface whether anybody documented them or not.

Databricks' newer Zerobus documentation puts this neatly at the technical layer: "the table is the contract." I'd extend that one floor upward because the table is only the syntax; consumers also depend on semantics, operating behavior, timing guarantees, historical treatment, and definitions absent from the schema.

A useful compatibility promise therefore needs more than types. I want to know whether a field can disappear, change units, become nullable, arrive late, be recomputed historically, or acquire a new definition. Those are product questions wearing SQL clothes, and a green pipeline won't answer them.

## Version meaning when meaning changes

Automatic evolution is valuable for additive changes because a new optional column shouldn't require a committee meeting or manual DDL. Semantic changes deserve more friction, especially when downstream teams have encoded the old definition into decisions made without checking the source table.

VMO2's published Google Cloud implementation uses YAML data contracts with ownership, schema, quality rules, and service-level expectations, committed through GitOps. The interesting part isn't YAML; context travels with the data instead of a stale wiki page.

For a product team, I'd borrow a familiar API habit and distinguish additive changes from breaking ones before deciding how much ceremony belongs around them. New optional fields can usually ride forward, because consumers that ignore them keep working without a migration.

A changed definition is different: it may deserve a new field, migration window, consumer notification, explicit retirement date, and telemetry showing who still queries the old version before anyone removes it from production systems with undocumented downstream dependencies. The storage engine doesn't know that distinction because both versions may be perfectly valid columns, which is exactly why ownership can't stop at the ingestion boundary.

That connects to my earlier [API deprecation argument](/blog/2026/08/24/api-deprecation-customer-migration/): publishing a replacement doesn't finish migration. Data producers have the same obligation: know which consumers still depend on the old contract before changing what their fields mean.

Schema evolution keeps those data pipes flowing without manual intervention. That's useful infrastructure, and exactly what it promises.

If the column still loads while the decision it feeds changes underneath it, though, the data product broke anyway.

## Sources

- [Databricks: Schema enforcement](https://docs.databricks.com/aws/en/tables/schema-enforcement)
- [Databricks: Zerobus Ingest schema management](https://docs.databricks.com/aws/en/ingestion/zerobus-schema-management)
- [Snowflake: Enable automatic table schema evolution](https://docs.snowflake.com/en/en/user-guide/data-load-schema-evolution)
- [Google Cloud: VMO2 uses data contracts to build scalable AI and data products](https://cloud.google.com/blog/products/data-analytics/vmo2-uses-data-contracts-to-build-scalable-ai-and-data-products)
