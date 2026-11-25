---
layout: post
title: "File Uploads Need a Quarantine State"
date: 2026-11-25 10:55:57 -0600
category: Security + Workflow
description: "File upload products need explicit quarantine, integrity checks, content validation, safe processing, release rules, and a durable custody receipt."
read_time: 6 min
---

The progress bar reached 100 percent. The user copied the new file link into a customer message. Thirty seconds later, the malware scan failed and the file disappeared.

The upload had completed, but the product had treated completion as acceptance.

That shortcut creates two bad outcomes. Unsafe content can become visible before controls finish, or safe content can vanish after the interface has already promised success.

A file upload is an admission workflow. Bytes arriving at the server are only the first state.

## Make quarantine visible

Use explicit states such as reception, received, under validation, quarantined, processed, ready, rejected, expired, and deleted. The names can change, but the transition into ready should require every release condition to pass.

The user should see the current state and what it permits. A quarantined file may be visible only to its uploader and security reviewers. It should remain unavailable to other users, automations, search indexes, previews, and downstream parsers.

Do not generate a public or broadly shareable link before release. If the product must return an identifier immediately, make it resolve to a status page with authorization checks rather than to the raw object.

OWASP recommends defense in depth for uploads. Its guidance includes extension allowlists, independent file-type validation, generated storage names, size limits, authorized uploaders, storage outside the web root, and antivirus or sandbox checks where available. No single check is enough.

Those controls take time. Quarantine makes that time an honest product state instead of an invisible race.

## Treat every client claim as untrusted metadata

The original filename, extension, media type, and directory path are useful for display. They are not proof of content or safe storage instructions.

RFC 7578 defines how multipart form data can carry a filename. It also warns receivers not to use that filename blindly and not to trust directory path information that may be present. The standard notes that uploaded files can contain arbitrary executable content.

Keep the original name as metadata, then generate an internal object identifier. Normalize names for display, enforce length limits, and handle duplicate names without overwriting another object. Preserve the original value for audit when policy allows it.

Validate what the product actually needs. An image workflow can decode and re-encode supported formats under strict resource limits. A document workflow can inspect structure, macros, encryption, and embedded objects. An archive workflow needs limits on expanded size, archive depth, file count, and time budget.

Reject a mismatch with a precise reason. “Upload failed” gives the user no path forward. “The file extension is PDF, but the content is not a readable PDF” is actionable without exposing internal security rules.

## Prove that the received bytes stayed intact

Large files often arrive in parts. A completed multipart request proves that the transport sequence ended. It does not by itself prove that the final object matches the bytes the sender intended.

Amazon S3 supports full-object and part-level checksums. It can calculate a checksum independently, compare it with the supplied value, reject a mismatch, and retain the checksum as object metadata. Its documentation also notes that a multipart ETag is not necessarily an MD5 digest of the whole object.

Store a strong checksum with the object record and use the same object version throughout validation. A scan result for one version should never authorize a replacement uploaded under the same visible name.

Record the uploader, request time, byte count, detected type, checksum, scanner versions, policy version, validation results, and release decision. Call this the **content custody receipt**. It connects the file a person selected to the object the product eventually released.

## Design failure and retry as product states

Scanners time out. Preview workers crash. Policy services become unavailable. These are not the same as a malicious file.

Separate rejected from failed. Rejected means a completed decision found that the file violated a rule. Failed means the product could not finish the decision. A failed file may support a bounded retry without asking the user to send the bytes again.

Retries should be idempotent and tied to the same object version. A new upload creates a new admission attempt, even when the visible filename is unchanged. Superseded attempts should remain unavailable and should age out under a documented retention rule.

For multi-file workflows, decide whether release is atomic. A contract package may need every attachment to pass before any become visible. A photo gallery may release clean images independently. State that behavior before processing begins.

After release, connect the outcome to the broader [reconciliation receipt used for bulk imports](/blog/2026/11/14/bulk-imports-need-a-reconciliation-receipt/). Upload admission answers whether the file is safe and intact. Import reconciliation answers what the product did with its contents.

Measure time in quarantine, scan failures, policy rejections, integrity mismatches, retry success, abandoned uploads, files released before all checks, and support cases caused by vague rejection messages. Track false positives through a controlled review path rather than weakening the default rule.

The progress bar measures transport. The product promise begins after the last byte arrives.

## Sources

- [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), OWASP Cheat Sheet Series.
- [Checking object integrity for data uploads in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html), Amazon Web Services.
- [Returning Values from Forms: multipart/form-data](https://www.rfc-editor.org/rfc/rfc7578.html), RFC Editor.
