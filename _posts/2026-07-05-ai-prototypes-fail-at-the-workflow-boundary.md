---
layout: post
title: "AI Prototypes Usually Fail at the Workflow Boundary"
date: 2026-07-05 14:10:00 -0500
category: AI + Product
description: "A model can work perfectly in a demo and still fail as a product if it does not fit the surrounding workflow."
read_time: "4 min read"
---

AI demos are unusually good at creating false confidence.

A model answers a question correctly, summarizes a document, classifies an image, or generates a useful recommendation.

Everyone in the room sees the capability and assumes the hard part is mostly solved.

Often it isn't.

The hard part is what happens **before and after the model runs.**

## The model is only one step

Imagine a team building an AI assistant for customer support.

The prototype works like this:

1. Paste a customer message into the model.
2. The model generates a good response.
3. A support agent copies the response into the ticketing system.

The model may be excellent.

But the actual production workflow needs to answer questions such as:

- How does the model get the right customer history?
- Which account data is safe to expose?
- How does it know which product version the customer uses?
- What happens when the model is uncertain?
- Can the agent edit the answer before sending it?
- How is the final response logged?
- Can we measure whether the suggestion was helpful?

Those are not edge cases. They are the product.

## Look for the handoffs

A useful way to evaluate an AI feature is to draw the workflow around it.

For example:

> incoming ticket → retrieve context → generate draft → human review → send response → measure outcome

Then inspect every arrow.

The failures often occur at those boundaries:

- wrong context retrieved
- stale data passed to the model
- permissions ignored
- output returned in an unusable format
- no obvious escalation path
- no feedback captured after the decision

The model can be 95% accurate and the overall workflow can still be frustrating.

## Prototype the ugly parts early

Teams naturally prototype the impressive part first.

That is understandable. The AI capability is usually the uncertain technical question.

But once the capability is demonstrated, the next prototype should often focus on something much less exciting:

**Can this fit into the real job without creating more work?**

Suppose an analyst currently reviews 30 cases each morning.

An AI system that generates a prediction for each case sounds useful.

But if the analyst has to open another application, search for the case, copy an identifier, wait for the model, interpret an unstructured answer, and then return to the original system, the feature may actually slow the job down.

A better product might place one ranked recommendation directly inside the analyst's existing queue.

Same model. Very different product value.

## Measure the whole workflow

AI teams often measure model quality because it is easy to define.

Precision, recall, accuracy, latency, and token cost matter.

But product success may depend on different metrics:

- time saved per task
- percentage of suggestions accepted
- percentage edited before use
- escalation rate
- error-recovery time
- user trust
- completion rate

If the model gets better but users accept fewer suggestions, you may have improved the wrong thing.

## The strongest AI products disappear into the work

The goal usually should not be to make users admire the model.

The goal should be to make a difficult task easier.

That means AI product design is partly model design, but it is also integration design, permissions design, interface design, measurement design, and exception handling.

A useful test is:

> If we removed the word "AI" from the product description, would the workflow still sound valuable?

If the answer is yes, you are probably building a product.

If the answer is no, you may still be building a demo.
