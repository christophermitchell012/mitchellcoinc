---
layout: post
title: "When AI Should Stop Writing and Start Choosing"
date: 2026-10-14 10:14:47 -0500
category: AI Product Strategy
description: "Decision models can replace generated prose with bounded choices, but product teams still need calibration, thresholds, and an escape route."
read_time: 4 minutes
---

Many AI features write a paragraph so the application can extract one word from it. A support router asks for an explanation, parses the answer, and eventually discovers that the model meant billing. The prose takes the scenic route. The product needed a choice.

Hugging Face merged a useful alternative into Transformers Serve on October 12. Its new `/v1/systemone` endpoint can use an autoregressive model to score a fixed set of answer options from the model's logits. It stops after the forward pass, returns typed answers and probabilities, and generates no text.

That small change separates language understanding from language production. Product teams should notice.

## Choose the output before choosing the model

Generated text is valuable when the output itself must be written: a response, summary, plan, or draft. It is awkward when software needs a bounded decision such as billing versus technical support, approve versus review, or a score from zero to four.

Typed choices reduce integration ambiguity. The application does not need to parse a polite essay, defend against a surprise label, or wonder whether "probably billing" equals `billing`. The contract is set before inference. Code receives one of the allowed answers.

This also changes model selection. A small local model may route tickets well enough even if nobody would hire it to write the apology. Accuracy on the actual choice set matters more than general eloquence. That is a healthier requirement and, occasionally, a cheaper invoice.

## Probability is not permission

A probability-looking number invites automation. It also wears a tie it may not have earned.

Purpose-trained decision models can be calibrated so that groups of answers labeled 80 percent are correct roughly 80 percent of the time. Raw logits from a general language model do not automatically provide that guarantee. A score of 0.92 can rank options correctly while still overstating certainty.

Run the model in shadow mode before connecting it to a consequential action. Compare its choices against resolved production cases. Measure error by class, workflow, language, and input quality. Recheck after model, prompt, label, or quantization changes.

Then set separate thresholds for separate consequences. Auto-routing a ticket can tolerate more error than issuing a refund. The existing article on [AI agent permissions](/blog/2026/08/20/ai-agent-permissions-are-a-product-decision/) makes the broader point: authority should follow the cost of a mistake.

## Give uncertainty somewhere to go

A closed answer set creates a tidy API. Reality remains under no obligation to be tidy.

Include an unknown, other, or needs-review path when the world can produce cases outside the listed options. Test whether the model uses that exit appropriately. If every input must become billing, sales, or technical, a legal request will still receive a confident badge. It may even look handsome while being wrong.

The escalation path should preserve the original state, the options considered, the returned scores, and the rule that blocked automation. A reviewer needs the evidence, not just a red flag.

## Treat the choice set as product behavior

Labels are not implementation trivia. They define which distinctions the product can make.

Changing two support queues into six may improve routing, reduce confidence, and expose training-data gaps. Adding descriptions can change results even when the labels stay fixed. Hugging Face's llama.cpp guidance shows this directly: a small decision model routed an ambiguous billing example incorrectly with bare labels and correctly after the options received descriptions.

Version the choice set with the workflow. Evaluate it like a feature. Assign an owner to every answer and to the escape route between them.

Decision endpoints make a useful promise: the model will choose instead of compose. Product discipline supplies the missing half. Decide what choices are legitimate, how much confidence earns action, and where uncertainty goes when the model has met a case that product taxonomy forgot.

## Sources

- [New in llama.cpp: Decision Models](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp)
- [System One: TypeSafe documentation](https://docs.typesafe.ai/concepts/system-one)
- [Transformers pull request 49322: v1/systemone endpoint](https://github.com/huggingface/transformers/pull/49322)
