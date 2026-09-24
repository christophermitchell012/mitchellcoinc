---
layout: post
title: "SDK Product Strategy: Build a Paved Road With Exits"
date: 2026-09-24 10:57:00 -0500
category: "Developer Experience + Product Strategy"
description: "A good SDK shortens the path to a valid business flow without trapping developers. Ship the common implementation, but preserve the API escape hatch."
read_time: "4 min read"
---

An SDK can be excellent documentation wearing a fake mustache, but the better ones do something documentation cannot: they ship an opinionated working path.

Holibob's new SDK is a useful example because the company already had an API for partners building their own integrations; its claim isn't that developers suddenly gained access to experiences inventory or booking operations that were previously closed to them. The SDK packages search, product display, availability, booking, and checkout into web components plus a small server-side proxy, with sandbox credentials and a versioned browser bundle.

Holibob says a native integration that commonly takes about six months can be running in three days with the SDK. That's a vendor claim rather than an independent benchmark, but the architecture behind it is more interesting than the headline number.

## Pave the common road

The SDK starts with code that already knows the sequence of operations required to complete a booking from discovery through checkout. A developer doesn't first have to learn the GraphQL schema, wire HMAC request signing, build product search, model availability, and discover which booking questions appear for each supplier.

That removes a particular kind of integration work: decisions the platform already knows how to make and customers rarely benefit from rediscovering.

I've built integration-heavy products, and this is where SDK strategy gets uncomfortable because convenience and constraint often arrive in the same package; every abstraction that saves a developer from understanding your API also creates an opinion about how their application should work. Push that too far and onboarding gets fast while customization gets progressively stranger, usually at exactly the moment a serious customer arrives.

Holibob handles that tension in a way I like. The browser elements use the same API operations available to partners directly, while the proxy runs in the customer's infrastructure and keeps credentials server-side. Developers can use the prebuilt storefront, individual components, or call the underlying API directly when the supplied UI no longer fits.

The SDK is therefore a paved road with exits, rather than a separate road that eventually dead-ends beside the API.

A wrapper that makes the first demo easy and the fifth requirement painful has simply moved integration cost later. Some customers will need custom checkout logic or a native mobile surface. Their escape route shouldn't require throwing away the integration underneath it when loyalty logic, unusual screens, or other product-specific behavior appears.

## Measure the distance to an exit

SDK adoption metrics can hide this problem surprisingly well. Downloads, successful installs, and time to first request describe the entrance while saying little about what happens after customers encounter a nonstandard requirement.

I'd track where developers leave the supplied path, which component gets replaced first, and which API operations repeatedly appear beside the SDK. Starter code that survives six months after launch would tell me more than another download counter ever could.

Those exits aren't necessarily defects in the product. Repeated exits at the same place may identify the next extension point, while customers abandoning the SDK entirely can reveal an abstraction that's too rigid.

This connects to [developer onboarding that manufactures first success](/blog/2026/09/07/developer-onboarding-manufacture-first-success/), but it extends the idea beyond the first successful transaction. A sandbox and working starter implementation collapse the distance to evidence, while a good escape path prevents that first success from becoming architectural debt later.

Holibob's sandbox makes the distinction unusually concrete. Developers can search the live catalogue and exercise booking flows without sending bookings to suppliers or settling payments, then move the same integration toward production after commercial approval.

For a product manager, there's a useful SDK question. How much unnecessary choice disappears without removing necessary choice from developers whose products eventually stop looking like your starter implementation?

Pave the road customers travel most, then leave exits where their product becomes theirs again.

## Sources

- [Holibob: The Holibob SDK, three days not six months](https://holibob.tech/holibob-sdk)
- [PhocusWire: Holibob launches SDK for embedding experiences storefronts](https://www.phocuswire.com/news/technology/holibob-launches-software-development-kit-embedding-experiences-storefronts)
- [Holibob API documentation: Introduction](https://partner.documentation.holibob.tech/general-api/Working-version/the-holibob-api-introduction)
