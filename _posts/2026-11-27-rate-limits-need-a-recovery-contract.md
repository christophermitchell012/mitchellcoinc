---
layout: post
title: "Rate Limits Need a Recovery Contract"
date: 2026-11-27 10:27:40 -0600
category: APIs + Reliability
description: "Rate limits should expose budgets, scope, retry timing, request cost, and recovery behavior so customers can slow down without guessing or losing work."
read_time: 6 min
---

A customer syncs twelve thousand records overnight. The first eleven thousand succeed. Then the API starts returning `429`, the integration retries every request at once, and the remaining work fails for three more hours.

The limit protected the service. The product left the customer to invent the recovery plan.

Rate limiting is necessary shared-capacity control. It becomes a product failure when customers cannot predict depletion, identify the affected budget, or know when work can safely resume.

## Define what the limit protects

A published number such as 5,000 requests per hour sounds precise. It says little without a scope.

The counter might apply per user, token, account, application, tenant, IP address, endpoint family, region, or some combination. One expensive request may cost more than one simple read. A concurrent-request ceiling can trigger while the hourly budget still looks healthy.

RFC 6585 defines `429 Too Many Requests`, but it deliberately leaves identity and counting policy to the server. The same status can therefore describe several different constraints. The product has to supply the missing model.

Document each budget with a name, scope, unit, window, reset behavior, and request cost. State whether failed requests count. Explain how pagination, batch operations, GraphQL complexity, file transfer, and asynchronous jobs consume capacity.

I call an undocumented mixture of counters **quota fog**. Customers see a number move, but they cannot connect it to the work that caused the change.

Do not hide dynamic protection behind a static quota page. Abuse controls may remain partly undisclosed, but the response should still distinguish a depleted published budget from a temporary concurrency or service-protection limit.

## Return a usable recovery signal

Every limited response should answer four product questions:

1. **What happened:** identify the policy or budget that blocked the request.
2. **Who is affected:** identify the relevant scope without exposing sensitive identifiers.
3. **When to continue:** provide a retry delay or reset time.
4. **What remains safe:** state whether the rejected operation changed anything.

RFC 6585 allows a `Retry-After` field on a `429` response. RFC 9110 defines that field as either an HTTP date or a number of seconds. Use it when the server can provide a meaningful minimum wait.

The response body should carry a stable machine-readable error code, a human explanation, a policy identifier, and a support reference. Avoid making clients parse prose for control flow.

Reset timestamps need clear semantics. A fixed-window reset is not the same as permission to release an entire backlog at that instant. Thousands of clients resuming together can produce another spike. Recommend jitter and gradual recovery.

If a limit is temporary and has no exact reset, say so. An honest lower bound is more useful than a false countdown.

## Make clients slow down before failure

The best limited request is often the one a client postpones.

Expose current allowance information on successful responses when practical. Show the governing budget, remaining capacity, reset point, and request cost. Keep those values consistent enough for pacing, while warning that concurrent traffic can change them before the next request.

GitHub provides a useful example. Its REST API reports limit, remaining requests, usage, reset time, and resource family in response headers. It also separates primary limits from secondary limits for concurrency, endpoint traffic, compute, and content creation.

That distinction changes client behavior. A depleted hourly allowance calls for waiting until reset. A concurrency limit calls for fewer parallel workers. A costly query may need a smaller page or a different shape. One generic exponential backoff loop cannot solve every case well.

Give customers visibility before production traffic is blocked. A dashboard should show consumption by policy, credential, tenant, endpoint, and operation. Add alerts at useful thresholds. Export the same measures so customers can connect them to queues and job schedules.

## Preserve work across the boundary

A rejected request is not always safe to repeat blindly.

For reads, a later retry is usually straightforward. For writes, the client needs idempotency support or a status lookup that resolves whether the operation committed before the response arrived. A rate-limit response should never conceal an ambiguous write outcome.

Batch workflows need a receipt. Record completed items, rejected items, request identifiers, policy, retry eligibility, and the earliest continuation time. The customer should resume from a checkpoint rather than replay the entire batch.

Priorities matter too. Reserve capacity for interactive work, safety actions, cancellation, and status checks when those paths must remain available during bulk traffic. Otherwise, a background import can prevent the customer from stopping the import.

Keep this boundary distinct from [API pricing and its billing unit](/blog/2026/08/27/api-pricing-billing-unit-product/). A billing unit explains what costs money. A rate-limit unit explains what consumes protected capacity. The two may use related measures, but customers should not have to reverse-engineer either.

## Test recovery, not only rejection

Load tests often stop after confirming that the service returns `429`. Continue through recovery.

Test clients with clock skew, many workers, shared credentials, mixed-cost endpoints, partial batches, and retry storms. Change a policy while jobs are queued. Verify that dashboards, headers, documentation, and support tools describe the same counter.

Measure limited requests, time to successful recovery, repeated violations, abandoned jobs, duplicate writes, capacity stranded by conservative clients, and traffic surges at reset boundaries. Segment by policy and customer workload.

A limit should protect reliable service without turning capacity into a guessing game. Name the budget. Expose the boundary. Preserve the work. Then give the client a safe route back in.

## Sources

- [RFC 6585: Additional HTTP Status Codes](https://www.rfc-editor.org/rfc/rfc6585.html), RFC Editor.
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), RFC Editor.
- [Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api), GitHub Docs.
