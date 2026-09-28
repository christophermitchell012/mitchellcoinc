---
layout: post
title: "Data Freshness Is a Product Feature You Can Price"
date: 2026-09-28 16:00:00 -0500
category: "Data Products + Product Strategy"
description: "Data freshness changes which customer decisions a dataset can support. Price update cadence against the decision window, not a generic race to real time."
read_time: "3 min read"
---

A dataset can become a different product without adding a single column, because changing its update cadence changes the decisions customers can make with it.

Japan Exchange Group supplied a clean example today.

JPX Market Innovation & Research added one-minute stock-price data to J-Quants Pro and moved issue-level margin-trading balances from weekly distribution to daily distribution, while keeping the existing weekly series available for continuity with prior analysis.

That last detail matters to product people because freshness isn't merely an infrastructure setting; it's part of the product contract, and sometimes a separately valuable product tier.

Weekly margin balances can support research where yesterday versus six days ago doesn't materially alter the conclusion or change the action.

Daily balances support a different job: observing shifts in supply, demand, and leverage close enough to the event to change timing or risk decisions, which JPXI explicitly describes.

One-minute OHLC data moves the boundary again, preserving intraday price formation that daily bars erase while producing less data than tick-level feeds.

That middle cadence is a product choice, not some technical compromise hiding in a pipeline diagram.

## Price the decision window

Pricing discussions often start with storage, API calls, compute, or source-acquisition cost.

Those inputs matter internally, but customers are buying usefulness inside a decision window whose length depends on the job they're doing.

This isn't a pricing formula; it forces a better product conversation about which decisions disappear as latency grows.

For a compliance archive, another minute may be nearly worthless, while for intraday execution analysis a daily close has already thrown away the shape of the trading day.

The same market can therefore support products with very different freshness requirements.

JPXI's packaging makes that relationship unusually visible.

J-Quants Pro lets corporate customers subscribe monthly to specific datasets, while the new daily margin dataset carries a 75% early-contract discount through the March 2027 billing period for contracts signed by December 2026, regardless of intended use.

Cadence and packaging belong next to each other in product decisions.

## Freshness has a bill

Real-time-ish data gets expensive quickly, even before anyone starts arguing about whether 'real time' means milliseconds, seconds, or merely faster than yesterday.

Faster ingestion means more frequent upstream calls or streams, more writes, tighter recovery objectives, and less tolerance for a quietly stale partition.

Customers inherit integration work too when their own systems can't consume, validate, or reconcile the faster cadence.

So I wouldn't automatically push every data product toward real time; I'd ask what customer decision changes at one minute, one hour, one day, or one week, then price the cadence and engineer backward from that boundary.

There is another trap here: freshness theater, where a dashboard refreshes every minute but the source underneath updates nightly.

A shiny timestamp in the corner doesn't rescue stale source data.

Product managers should make source timestamp, ingestion timestamp, expected cadence, late-arrival handling, and stale-data behavior explicit in the product contract.

Those fields stop being plumbing once customers make time-sensitive decisions from the feed, because missing the promised window changes what the product can actually do.

The timestamp isn't metadata around the product; sometimes it's the feature the customer is paying for.

## Sources

- [Japan Exchange Group: New Datasets and Service Enhancements at J-Quants Pro](https://www.jpx.co.jp/english/corporate/news/news-releases/6020/20260928-01.html)
