---
layout: post
title: "AI Agent Memory: Decide What the Agent Should Forget"
date: 2026-08-23 09:45:00 -0500
category: AI + Product
description: "AI agent memory improves continuity but creates durable product risk. Define provenance, scope, expiration, correction, and deletion before storing context."
read_time: "6 min read"
---

Persistent memory is starting to look like a standard feature of AI agents. Google Cloud published documentation this week for Agent Platform Memory Bank, which can generate long-term memories from conversations and reuse them across sessions. That's useful. An agent that remembers the project, the customer's preferences, or what happened yesterday doesn't have to reconstruct the world on every run.

It also creates a product question that I think is getting less attention than retrieval quality: **what should the agent be allowed to remember, and when should it forget?**

A bad answer in one session is a problem. A bad fact written into memory can become input to many future sessions. The failure has persistence now.

Palo Alto Networks' August Prisma AIRS update makes that risk concrete. Its AI red-teaming product now includes memory-poisoning tests for agents that can write information to persistent storage and retrieve it later. Tencent's Zhuque Lab recently demonstrated another memory-related attack path in which an agent with web access could be manipulated into leaking stored information through outbound requests.

Those are security examples, but I don't think memory belongs only in a security review. The PM has to define what persistence means for the product.

## AI agent memory needs a write policy

When teams talk about agent memory, the conversation often jumps to architecture: vector stores, graphs, summaries, embeddings, retrieval latency. I'd start one step earlier.

What earns the right to become durable state?

Imagine a customer-support agent sees this sentence during a conversation:

> Don't ship replacement units to our old Dallas office anymore. We moved receiving to Austin.

That could be valuable memory. It could also be an offhand comment from someone without authority to change shipping instructions.

The model's ability to extract a clean fact doesn't answer whether the product should store it.

I'd classify memory writes by consequence. A low-risk preference such as output format may be safe to learn automatically. A shipping location, account entitlement, approval rule, or production configuration deserves a different path. Some information should remain session context. Some should become a proposed update that a person confirms. Some should never be treated as agent memory because another system is already the source of truth.

This is closely related to the [authority ladder I use for AI agent permissions](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/). Reading, proposing, and acting aren't the same authority level. Neither are observing a fact and making it persistent.

## Provenance matters more once a memory survives the session

If an agent tells me, "The customer prefers weekly reports," I want to know where that came from.

Was it stated by the customer yesterday? Extracted from a six-month-old support ticket? Inferred from three prior actions? Written by another agent? Copied from a document that has since been replaced?

Without provenance, a memory can look authoritative simply because it has been retrieved.

For durable memories, I'd want enough metadata to answer at least:

> source → who or what wrote it → when → confidence/status → scope → expiration or review condition

That doesn't mean exposing a database record beside every response. It means the product should be able to trace an important remembered fact when someone questions it.

This also changes how I'd think about [production evidence in AI evaluations](/blog/2026/08/21/an-ai-eval-needs-production-evidence/). A production miss caused by bad memory isn't just another prompt to add to an eval. The team needs to determine whether retrieval chose the wrong memory, the stored fact was wrong, the fact was once right but became stale, or the agent should never have stored it in the first place.

Those are different product defects.

## Expiration should be designed, not left to storage capacity

Human organizations are full of facts with half-lives.

A user's preference for concise answers may remain useful for years. An incident workaround may be obsolete after tomorrow's deployment. A customer's temporary shipping restriction may expire Friday. A project assumption can become false after one executive decision.

So I wouldn't give every memory the same retention behavior.

I'd think in terms of a few practical classes: durable preferences, time-bounded facts, task state, inferred observations, and authoritative business records. The names don't matter much. The lifecycle does.

For each class, I'd ask what causes a memory to expire, what supersedes it, and whether deletion means actual deletion or simply removal from retrieval.

That last distinction matters. If a user corrects an agent from "Dallas" to "Austin," keeping both facts equally retrievable and hoping the model notices the newer timestamp isn't a robust correction mechanism.

The system should know which one is active.

## Give users and operators a correction path

Memory makes an agent feel smarter right up until it confidently remembers something wrong.

Then the product needs a way out.

For consumer software, that may be a simple view where the user can inspect and delete remembered preferences. In an enterprise workflow, correction may need permissions, an audit trail, or synchronization with the system that owns the underlying record.

I'd also instrument corrections. If users repeatedly delete one class of automatically generated memory, that's product evidence. Maybe the extraction is poor. Maybe the scope is wrong. Maybe that information never belonged in persistent memory.

The same principle applies to operations generally: [a useful metric should narrow the next action](/blog/2026/08/19/the-best-kpi-is-the-one-that-changes-a-decision/). "Memory accuracy" as one aggregate percentage won't tell me what to fix. Correction rate by memory type, stale-memory incidents, cross-user retrieval errors, and unsupported memory writes are much closer to actionable signals.

## The memory feature should have a forgetting test

Before I ship persistent memory, I'd test more than whether the agent remembers the right things.

I'd create cases where information changes, expires, conflicts, comes from an untrusted source, belongs to another user, or is explicitly deleted. Then I'd verify that future behavior changes appropriately.

A useful acceptance test might look like this:

> Session 1: authorized user changes a preference from A to B.
>
> Session 2: agent retrieves B and can show its source.
>
> Session 3: user deletes B.
>
> Session 4: agent no longer uses B and doesn't silently reconstruct it from an obsolete summary.

I'd run similar tests for tenant isolation and poisoned input. If an external webpage tells the agent to remember a new "company policy," does that ever become durable state? If another agent writes a conclusion into shared memory, is its provenance preserved? If the source document is revoked, what happens to facts derived from it?

An agent that remembers everything isn't necessarily more capable. It may just accumulate more ways to be confidently wrong later.

The product requirement I'd write is narrower: **remember information that improves future work, preserve enough provenance to challenge it, and make forgetting a first-class operation.**

That gives engineering something more useful than "add memory." It defines the lifecycle of the state we're asking the agent to carry forward.

## Sources

- [Google Cloud: Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)
- [Palo Alto Networks: Prisma AIRS August 2026 new features](https://origin-docs.paloaltonetworks.com/ai-runtime-security/new-features/by-date/prisma-airs/august-2026)
- [Tencent Zhuque Lab: Why AI Agent's Memory Becomes Attacker's Data Goldmine](https://matrix.tencent.com/en/2026/08/06/ai-agent-memory-heist)
