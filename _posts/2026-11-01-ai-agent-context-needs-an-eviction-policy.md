---
layout: post
title: "AI Agent Context Needs an Eviction Policy"
date: 2026-11-01 10:26:52 -0600
category: Product Strategy
description: "AI agents need explicit rules for pinning, summarizing, and evicting context so long-running work stays accurate, affordable, and auditable."
read_time: 5 min
---

An agent spends two hours comparing vendor contracts. Near the end, it remembers a temporary login error and forgets the customer's nonnegotiable liability clause.

The model did not run out of intelligence. The product ran out of room and never decided what deserved to stay.

Long-running agents accumulate instructions, tool definitions, search results, file contents, intermediate calculations, and their own prior messages. A large context window delays the problem. It does not remove the need to choose.

AI agent context needs an eviction policy.

## Treat context as a working set

Context is the material available to the model for the next decision. It is not the system of record, and it should not become one by accident.

Start by classifying the contents of an agent run:

- **Pinned:** user goals, safety constraints, approved decisions, and definitions that must survive.
- **Active:** evidence and intermediate state needed for the current step.
- **Compressible:** material whose meaning can survive in a shorter summary.
- **Disposable:** stale tool output, duplicated text, and completed scaffolding.

That classification turns token pressure into a product choice. A 40-page contract may be active during comparison and compressible after its exceptions are captured. A shipping address can remain pinned until the order completes. A failed search page may be disposable as soon as the useful error is recorded.

Without these states, agents usually fall into one of two habits. They carry everything until a limit forces a crude truncation, or they summarize aggressively and hope the summary kept the right detail. Both approaches hide the decision.

## Make compaction observable

OpenAI's Responses API can trigger server-side compaction after a configured token threshold. The compaction item carries forward important prior state with fewer tokens, and older items can then be removed from subsequent requests.

That is useful infrastructure. The product still needs to know what promise the compacted state must preserve.

Define a compaction contract for each workflow. It should name the facts that cannot be reduced, the evidence that may be summarized, the owner of the summary format, and the tests that prove continuity afterward.

A support agent may need exact customer quotations. A coding agent may need the latest test failure and modified-file list. A purchasing agent must retain the approved amount and recipient without paraphrase.

Call the cost of carrying irrelevant material **context rent**. The bill appears as higher latency, higher token spend, and more competition for the details that matter. Removing material saves rent, but an undocumented eviction can cost more when the agent repeats work or violates an earlier constraint.

Every compaction event should leave a receipt: trigger, tokens before and after, items pinned, items summarized, items removed, and the identifier of the durable source. The receipt makes a smaller prompt inspectable instead of magical.

The user view can stay plain. “Conversation compressed” is not enough. Show that three earlier reports became one summary, two constraints stayed pinned, and the original files remain available. If a person corrects the summary, keep that correction with the receipt so the next compaction does not recreate the same mistake.

## Evict results, not evidence

Agent tools create a surprising amount of bulk. A web search can return pages of text. A database query can return thousands of rows. A tool catalog can consume space before the first useful action.

Anthropic separates several ways to manage that pressure. Tool search delays loading definitions, while programmatic tool calling keeps intermediate results out of conversation history. Prompt caching reduces repeated-input cost. Context editing removes older tool results after they have served their purpose.

Those are different levers. Caching does not create more context capacity. Deleting a raw tool result does not preserve its conclusion. Keeping a conclusion without a source makes later review harder.

Preserve the evidence chain outside the context window. Store the raw artifact durably, place a source identity and retrieval path in the active state, and carry only the excerpt or calculation needed for the next decision.

This extends the [source-aware memory rules for AI agents](/blog/2026/08/23/ai-agent-memory-product-requirements/) into the working context. Memory decides what the product retains across runs. Eviction decides what the model receives right now.

## Test the missing-detail cases

Google describes long context as short-term memory and notes that large windows support agentic work by keeping more state available. Even a very large window remains shared capacity. Input, reasoning, and output all need room somewhere.

Do not test context management only with smooth conversations. Fill the window with repetitive logs, then insert one critical constraint early. Compact during a tool failure. Resume after several summaries. Change a pinned instruction midway through the run. Remove a raw result, then ask the agent to cite its source.

Measure constraint retention, repeated tool calls, summary drift, retrieval success, token use per completed task, latency after compaction, and decisions made from evicted evidence. Compare those results with a full-context baseline on the same work.

The interface also needs an honest failure state. If the agent cannot prove that a critical detail survived, it should pause and retrieve the source instead of inventing continuity.

A context window is valuable because it lets the model work with a useful slice of the world. Product discipline decides which slice. Pin the promises, compress the history, keep the evidence retrievable, and make every eviction visible enough to challenge.

## Sources

- [OpenAI API: Compaction](https://developers.openai.com/api/docs/guides/compaction)
- [Claude Platform: Manage tool context](https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context)
- [Gemini API: Long context](https://ai.google.dev/gemini-api/docs/long-context)
