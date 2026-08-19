---
layout: post
title: "Build Dashboards Around Exceptions, Not Averages"
date: 2026-06-26 09:20:00 -0500
category: Product + Analytics
description: "Operational dashboards are most useful when they make the few abnormal things easier to find than the many normal ones."
read_time: "4 min read"
---

I like operational dashboards that get boring when everything is working.

That sounds a little backwards because most dashboard demos try to look busy: maps, gauges, trend lines, counters and enough color to make the system feel alive.

But if I'm running an operation, I don't need the dashboard to entertain me. I need it to tell me which few things deserve attention.

I saw this pretty clearly working on fleet products. When most vehicles are behaving normally, a screen full of healthy units is reassuring, but it doesn't help much with the next decision. The useful part is finding the robot that stopped progressing, the route that suddenly looks wrong, the telemetry that disappeared, or the same failure showing up often enough that it may be turning into a pattern.

That's why I tend to think of a good operations dashboard as an **exception queue with context**.

## Averages are still useful

Average delivery time, completion rate, uptime and support volume can all tell you whether the system is generally getting better or worse. I'd keep those.

I just wouldn't make an operator hunt through summary charts to discover a problem that's already visible in the underlying data.

If ten units are behaving abnormally, show me those ten units.

Then tell me what's weird about them.

Maybe several share the same software build. Maybe the failures started after entering the same geographic area. Maybe a sensor stopped reporting. Maybe four events are still classified as "unknown," which can be more interesting than it sounds because it may point to a gap in the telemetry itself.

Those details are much closer to the actual job.

## "Worst first" isn't always the right sort order

One thing I've learned from operational products is that the biggest number isn't automatically the most important problem.

I may care more about a moderate issue affecting twenty units than a severe one affecting a single unit. A safety-related event can outrank a larger efficiency problem. Something that's been unresolved for forty minutes may matter more than a spike that started thirty seconds ago.

So the queue needs some product judgment.

Severity matters, but so can duration, customer impact, number of affected assets, recurrence and confidence in the diagnosis. You don't need an elaborate scoring model on day one. You just need to acknowledge that operators are prioritizing constantly, whether the software helps them or not.

A weak alert basically says:

> Something is wrong.

A useful exception card gets closer to:

> This asset has been outside its normal operating pattern for 18 minutes, three similar assets are showing the same behavior, and all four changed after the same deployment.

Now I know where I'd start.

I usually want current state, recent history, likely contributing factors and a quick path to the underlying records. Not every case needs all of that. Every extra click should earn its keep.

The dashboard doesn't need to explain the entire system. It needs to make the abnormal thing hard to miss and cheap to investigate.

And if everything is healthy, I'm perfectly happy for that screen to look quiet.
