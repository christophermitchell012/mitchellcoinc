---
layout: post
title: "Product Adjacency: Price the Missing Seam"
date: 2026-09-20 10:05:00 -0500
category: "Product Strategy + Pricing"
description: "Adjacent products win when shared data removes synchronization work. Mercury Books shows why teams should price the missing seam before copying features."
read_time: "4 min read"
---

Accounting software has spent decades importing the bank statement. On September 16, Mercury flipped that relationship around by launching Mercury Books, a double-entry accounting product inside the banking account itself.

That sounds like bundling; the more interesting product move is architectural, because owning the source transaction lets one entire class of synchronization work disappear.

Mercury checking, savings, and credit accounts flow into Books automatically, while Mercury invoices and bills arrive without another connector; external banks come through Plaid, and Stripe, PayPal, and Gusto need their own connections, which makes the boundary unusually easy to see.

The advantage isn't “one app.” It's fewer seams around data Mercury already owns, and those seams are often where software gets expensive.

## Adjacency has data gravity

I've built integration-heavy products where the annoying work wasn't making the API call. The pain came later, when we had to decide which system was authoritative after retries, stale records, duplicate events, partial failures, and somebody's CSV import quietly entered the picture.

Feature checklists make me suspicious here. A narrower adjacent product can still hold a structural advantage when it removes reconciliation at the boundary.

Mercury Books continuously reconciles Mercury accounts because the ledger and banking activity live in the same system; its documentation says every Mercury account is included by design, including closed accounts, and customers can't exclude an individual one from Books.

Convenience carries a tradeoff here: tighter coupling removes sync work while making the product boundary less portable for customers whose financial lives don't fit neatly inside it.

Books currently works in USD, doesn't offer read-only access inside Books, and can't show reports on both cash and accrual bases simultaneously. Those aren't footnotes for an accounting buyer. They show exactly where an adjacency strategy stops and specialist depth starts mattering more.

## Price the missing seam

Books costs $35 monthly after December 31. I'd resist comparing that price through a giant spreadsheet of feature rows.

Instead, calculate the seam: time spent matching transactions, reconnecting feeds, resolving duplicate records, explaining mismatches to a bookkeeper, and waiting for yesterday's financial state to become trustworthy.

RidgeWood, a Mercury Books beta partner serving more than 200 monthly clients, says the product cut its manual bookkeeping time roughly in half. That's a vendor customer story rather than an independent benchmark, so I wouldn't plug 50% into a business case and declare victory.

Still, it points directly at the mechanism a pilot should measure.

The pattern travels beyond fintech, although the economics change by category and the underlying shared data has to be genuinely useful. Consider payroll adding benefits, or an IoT platform adding device diagnostics. The adjacency earns an advantage when shared context removes work customers previously stitched together.

Sometimes the specialist's deeper product wins anyway. Complex accounting, unusual permissions, multi-currency operations, or established workflows that are costly to move can matter more than the seam.

Product teams entering an adjacent category should inventory synchronization tax before copying the incumbent's feature list, then measure how much of that tax their shared data actually removes.

If the new product merely shares a navigation bar, it's bundling with nicer plumbing. If it deletes reconciliation work because both sides share the same underlying truth, the adjacency has earned its keep.

Mercury Books is interesting because the bank account isn't merely where accounting data comes from anymore. For customers who fit its current boundaries, the bank account is becoming the accounting product.

Related: [Build vs. Buy: Price Product Freedom, Not Just Cost](/blog/2026/08/31/build-vs-buy-price-product-freedom/).

## Sources

- [Mercury: Introducing Mercury Books](https://mercury.com/blog/introducing-mercury-books)
- [Mercury Support: Getting started with Mercury Books](https://support.mercury.com/hc/en-us/articles/53480926332052-Getting-started-with-Mercury-Books)
- [Mercury Support: Sharing access to your books](https://support.mercury.com/hc/en-us/articles/53486200402196-Sharing-access-to-your-books)
- [Mercury: RidgeWood customer story](https://mercury.com/blog/ridgewood-mercury-books-story)
