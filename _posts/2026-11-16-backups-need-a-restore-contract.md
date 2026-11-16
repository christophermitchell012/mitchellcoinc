---
layout: post
title: "Backups Need a Restore Contract"
date: 2026-11-16 10:09:07 -0600
category: Reliability + Product
description: "A backup product should prove what can be restored, how long recovery takes, which dependencies matter, and whether the result actually works."
read_time: "5 min read"
---

The backup dashboard is green on Tuesday morning. Every scheduled job completed. Storage is healthy. Retention policy checks passed.

Then a customer deletes the wrong workspace.

Operations selects the latest recovery point and discovers that the database can be restored only into an older application version. The encryption key lives in a different account. Uploaded files arrive, but several do not match their database records. The backup existed. Recovery did not.

Backup products often report the activity they can observe most easily: bytes copied, jobs completed, snapshots retained, and failures retried. Customers care about a harder outcome. They need a working system, with an understood amount of data loss, inside an acceptable time.

That outcome needs a restore contract.

## Define the recovery unit before the schedule

A backup schedule answers when copies are created. It does not answer what must return together.

Start with the recovery unit. For a SaaS workspace, that may include database rows, object storage, configuration, encryption material, identities, search indexes, integration state, and the application version capable of reading them. For a connected product, it may also include device certificates, fleet assignments, firmware compatibility, and queued commands.

The product should show which components are authoritative, derived, or excluded. Derived search indexes may be rebuilt. Missing encryption keys may make a complete database useless. A copied configuration file may contain a reference to a secret that was never captured.

GitLab tells administrators to back up configuration separately from application data and to keep encryption keys apart from encrypted archives. Its restore documentation also warns that backup and target versions must match. Those are not footnotes. They are dependencies in the recovery unit.

Expose them before failure. A customer should be able to see that a recovery point contains the database and uploads but depends on a separately managed key and a specific software version.

This is where [hosting location becomes a product feature](/blog/2026/09/23/hosting-location-product-feature/). Once software moves across customer environments or accounts, backup scope, credentials, versions, and restore ownership become part of the product promise.

## Separate captured, restorable, and validated

One green status cannot represent three different claims.

- **Captured:** the expected backup artifacts were created and retained.
- **Restorable:** the artifacts can be read and used to create the intended resources.
- **Validated:** the restored system passed product-level checks.

Call the habit of treating the first claim as proof of the third **green-check recovery**. It produces comforting dashboards and unpleasant incident calls.

AWS Backup supports scheduled restore testing with selected recovery points, target start times, monitored duration, and optional validation. The distinction matters. Completing a restore job proves that infrastructure was created. Validation determines whether the recovered resource is useful.

Product validation should reach beyond a service health check. Open representative records. Confirm file references. Decrypt protected values. Verify tenant boundaries. Exercise authentication without sending real customer notifications. Compare row counts and checksums where they are meaningful. Rebuild derived data, then confirm that the application can query it.

Store the validation rules with a version. A test written for last year's schema can pass while a newer feature remains unrecoverable.

## Make time and data loss visible

Recovery point objective and recovery time objective are often written in contracts, then hidden from the people operating the product.

Show the newest validated recovery point, not only the newest captured point. Display the potential data-loss window in ordinary time: “Validated through 9:42 a.m. Up to 24 minutes of newer work may be missing.”

Measure recovery time from the moment restoration is requested until the product is ready for its intended use. Infrastructure creation, data loading, index rebuilds, dependency changes, validation, and traffic cutover all count. A database that returns in twelve minutes may still leave the product unavailable for two hours.

NIST contingency-planning guidance recommends testing recovery on alternate platforms, connectivity, system performance, restoration of normal operations, and individual recovery procedures. It also calls for documenting results and corrective actions. The product version of that guidance is a restore history that shows what was tested, what failed, what changed, and whether the next test closed the gap.

Avoid presenting one average restore time. Break results down by data size, resource type, tenant shape, region, encryption path, and application version. The largest or strangest customer is unlikely to recover like the median one.

## Return a durable recovery record

Every test and real restore should end with a record that another person can review without reconstructing the incident from logs.

Include the requested recovery point, actual artifacts used, dependency versions, target environment, operator, approvals, start and finish times, validation suite, failed checks, data-loss window, cleanup status, and final disposition. Identify whether the restored environment was isolated, promoted, abandoned, or deleted.

The test boundary deserves special treatment. AWS recommends a designated account for restore testing and deletes test resources after the validation window. The interface should make the destination unmistakable before execution, keep test data isolated, and confirm cleanup after validation ends.

Track validated recovery coverage, restore-test age, objective breaches, dependency failures, validation failures, manual steps, cleanup failures, and corrective actions left open. Measure by recovery unit and customer tier. A high backup-success rate should not hide a product that has never restored its largest tenant.

Run tests after meaningful schema, infrastructure, identity, encryption, and deployment changes, not only on a calendar. Rotate recovery points and target environments. Occasionally exercise the people and approvals too. A technically valid procedure can still fail because nobody can obtain the right credential at 2:00 in the morning.

A backup is evidence that data was copied. A validated restore is evidence that the product can return.

Make that difference visible before customers need it.

## Sources

- [AWS Backup: Restore Testing](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html)
- [NIST SP 800-34 Rev. 1: Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
- [GitLab Docs: Get Started Administering GitLab](https://docs.gitlab.com/administration/get_started/)
