---
layout: post
title: "Bulk Imports Need a Reconciliation Receipt"
date: 2026-11-14 10:34:00 -0600
category: Data Products + Product
description: "Bulk import products should preview changes, quarantine invalid rows, and issue a durable reconciliation receipt that explains every outcome."
read_time: "5 min read"
---

An operations manager uploads 8,214 customer records on Friday afternoon. The import page spins, reports `Completed`, and sends her back to the customer list.

On Monday, support finds 7,981 new records. Some existing customers were updated. Others appear twice. Nobody can explain the remaining 233 rows.

The upload succeeded. The operating decision did not.

A bulk import is a controlled migration into a live product. It needs a preview before execution, a quarantine path for uncertain rows, and a reconciliation receipt after the write.

## Treat the file as untrusted input

CSV looks simple because people can open it in a spreadsheet. Its edge cases are not simple.

RFC 4180 documented a common CSV format after years of inconsistent implementations. Records may include an optional header. Quoted fields may contain commas, quotation marks, and line breaks. Character encoding and header presence may be declared separately from the file itself.

The first product step should therefore identify the file before interpreting its business meaning. Detect or request the delimiter, encoding, header row, line ending, and locale assumptions. Preserve the original file and a hash of its bytes.

Then parse into a staging area. Do not write directly into production records while discovering whether `03/04/26` means March 4 or April 3.

Security belongs at this boundary too. OWASP warns that spreadsheet applications may treat cells beginning with characters such as `=`, `+`, `-`, or `@` as formulas. A value that looks harmless in the application can become active when someone exports and opens it elsewhere.

There is no universal cleanup rule that makes every spreadsheet consumer safe. Keep the original value, flag risky prefixes, and make the export policy explicit for the destination.

## Preview decisions, not just rows

Most previews show the first ten lines. That confirms the file opened. It does not reveal what the import will do.

A useful dry run applies the same mapping, normalization, matching, validation, permissions, and business rules as the real import. The preview should summarize expected outcomes:

- Records to create.
- Existing records to update.
- Rows to skip as exact duplicates.
- Rows blocked by validation or permissions.
- Ambiguous matches that require a choice.

Show representative examples from every outcome, not only the top of the file. Sampling should include the longest values, missing identifiers, unusual characters, and each detected error class.

Field mapping needs the same honesty. Display source header, destination field, transformation, required status, and a sample converted value. If a saved mapping came from an older schema, name the changed fields before execution.

Shopify uses a preview step for product CSV imports and requires UTF-8 files with case-sensitive headers. Its documentation also calls out quotation problems and conflicting product data. Those constraints are a reminder that valid CSV and valid product change are separate tests.

## Quarantine uncertainty without losing the batch

One bad row should not erase evidence about the other 8,213. Nor should a product quietly drop that row and call the batch complete.

Put rejected and ambiguous rows into a quarantine queue. Each item should retain its source row number, stable row identifier, original values, normalized values, failed rule, and proposed repair.

I call a row that disappears between upload and destination **row limbo**. It is missing from the product, absent from the success count, and difficult to recover from the original file. A quarantine queue turns that absence into owned work.

Let an operator correct a row and replay only that row. The replay should use the same import definition unless the operator deliberately selects a newer one. Keep the original outcome beside the corrected outcome.

Matching rules deserve special care. Email address, external ID, SKU, and account number may each look unique until normalization or legacy data proves otherwise. When two destination records match, do not choose one by position. Stop that row and expose the candidates.

The same discipline helps with changing meaning. If a field definition has shifted, the importer should not silently reinterpret old values. This is one reason [data products break when meaning changes](/blog/2026/09/01/data-products-break-when-meaning-changes/). Mapping versions need effective dates and owners, just like schemas.

## Issue a receipt that can close the loop

`Completed` describes a process state. A reconciliation receipt describes the result.

The receipt should include the original filename and hash, uploader, start and finish times, import definition version, schema version, matching policy, and execution identifier. It should reconcile the input total exactly:

`input rows = created + updated + skipped + quarantined + rejected`

Attach a downloadable row-level result with source identifier, destination identifier when one exists, outcome, and reason. Protect that file with the same access controls and retention rules as the underlying records.

Counts alone are not enough. If 2,410 records were updated, identify which fields changed and whether blank source values were allowed to overwrite populated destination values. If duplicates were skipped, identify the matching key and matched record.

Design reversal before launch. Some imports can be rolled back safely. Others trigger messages, invoices, permissions, or downstream synchronization that cannot simply be undone. The receipt should state the supported recovery action, its deadline, and the side effects that require manual repair.

Finally, measure the workflow rather than the upload endpoint. Track preview abandonment, quarantined-row rate, repair time, replay success, duplicate creation, unintended overwrite, and support cases per import. Break those measures down by mapping version and error class.

A trustworthy import does not ask operators to believe a green banner. It lets them account for every row, inspect every rule, and recover from every uncertain decision.

That is the product promise: no row disappears, no change arrives unexplained, and every batch leaves a receipt.

## Sources

- [RFC 4180: Common Format and MIME Type for Comma-Separated Values Files](https://www.rfc-editor.org/rfc/rfc4180)
- [OWASP: CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection)
- [Shopify Help Center: Importing products with a CSV file](https://help.shopify.com/en/manual/products/import-export/import-products/)
