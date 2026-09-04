---
layout: post
title: "Product Defaults Are Product Decisions"
date: 2026-09-04 10:18:00 -0500
category: Product Strategy + Developer Experience
description: "Product defaults quietly spend user time. Watch what experienced customers change immediately, then decide whether the baseline is serving the right user."
read_time: "4 min read"
---

A blank developer machine is rarely blank; it arrives carrying decisions about file visibility, paths, search, notifications, terminals, runtimes, and which tools deserve the first click.

Microsoft made that unusually visible today with Project Zenith, a developer-focused Windows configuration for machines with at least 64 GB of unified memory and 250 GB/s of memory bandwidth. The hardware headline is local AI. Microsoft says those systems can run 30B+ parameter models locally. The more interesting product choice is smaller: Zenith changes the defaults.

File extensions and hidden files are shown, long paths are turned on, and recent-file clutter, sync-provider tips, Start-menu tips, and account notifications are turned off. The tools are familiar. Windows Terminal and Visual Studio Code are pinned, while WSL becomes part of the baseline rather than another installation chore.

None of those changes is individually impressive, but together they make an argument product teams often dodge: defaults are part of the product, not neutral starting conditions.

## Every default spends somebody's time

A configurable product can technically serve two users while still favoring one of them every morning.

If an administrator must disable six notifications after every deployment, the product has chosen interruption as its default; if a developer always turns on file extensions, the product has chosen concealment first. A dashboard that opens to an all-company view before a regional operator narrows it has chosen extra scanning.

Settings pages don't erase those choices; they move the cost from the product team to the user, one toggle at a time, and that gets especially expensive in enterprise software because configuration multiplies across people, devices, roles, and resets. I wrote earlier about keeping [enterprise controls from weighing down the daily workflow](/blog/2026/08/28/enterprise-software-scale-without-complexity/). Defaults are the quieter version of the same problem; nobody files a procurement objection because file extensions are hidden; thousands of tiny corrections simply become normal.

## Configuration is evidence

There's a useful product-research trick hiding here: watch what experienced users change immediately after setup.

Repeated configuration isn't automatically a feature request because some preferences really are preferences, and forcing one expert's setup onto everyone would be personalization theater in reverse. But when the same user segment repeatedly changes the same defaults before doing useful work, that's behavioral evidence about the baseline.

The test I'd use considers frequency of the change, cost of leaving the default alone, and specificity to a coherent user group. High on all three deserves product attention; low frequency and low consequence probably belongs in Settings forever.

Project Zenith takes the segmentation route. Microsoft isn't changing every Windows installation into a developer workstation; it's creating a developer-class baseline while preserving customization. That distinction matters because a good default is contextual, and the right starting state for a software engineer can irritate an accountant sharing the same operating system.

Product teams spend a lot of energy designing what users can do, while the first state deserves equal suspicion.

If your best customers begin by changing the same five settings, they've already written part of your onboarding backlog.

## Sources

- [Microsoft Windows Developer Blog: Announcing Project Zenith](https://blogs.windows.com/windowsdeveloper/2026/09/04/announcing-project-zenith-the-ready-to-code-windows-experience/)
