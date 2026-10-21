---
layout: post
title: "Robot Simulators Need a Fidelity Budget"
date: 2026-10-21 10:08:46 -0500
category: Product Strategy
description: "A robot simulator needs a fidelity budget that ties physics, sensors, timing, and world detail to the product decision being tested."
read_time: 5 min
---

The robot clears every corner in simulation. In the hallway, its wheel catches the threshold and the localization estimate drifts six inches. The team did not build a useless simulator. It built an accurate answer to the wrong question.

Simulator roadmaps often treat realism as a ladder. Add better lighting, finer meshes, richer weather, and more detailed physics; then climb toward reality. That framing hides the product choice. A simulator only needs to be faithful enough, in the right dimensions, for the decision at hand.

Call the remedy a **fidelity budget**: an explicit allocation of simulation effort across the properties that could change a product decision.

## Realism has several axes

A warehouse robot may need precise wheel slip and contact behavior but only crude wall textures. Vision models may need convincing glare, blur, and occlusion while tolerating simplified motor dynamics. Fleet schedulers may care about queue timing and charger availability, with no reason to render a photorealistic pallet.

Those are different products hiding inside the word “simulator.” Treating them as one realism problem invites expensive polish in places that cannot alter the answer.

The budget should name at least four accounts:

- dynamics: mass, friction, contacts, actuator delay, and control response;
- sensing: noise, calibration, occlusion, exposure, and timestamp behavior;
- world behavior: geometry, agents, traffic rules, weather, and rare events;
- compute timing: update rates, scheduling delay, dropped frames, and network jitter.

An account receives budget when its error could reverse a launch, safety, or architecture decision. Otherwise, approximation is a feature. It keeps runs cheap, scenarios editable, and causes legible.

## Tie fidelity to the decision

Start each simulation request with a sentence: “We will use this run to decide whether X.” The ending might be whether a gripper needs a softer pad, whether an autonomy release can handle a blind intersection, or whether ten robots can share two chargers.

Then list the variables capable of flipping that decision. This turns an argument about visual quality into a testable contract. CARLA, for example, separates server-side world state, physics, and sensor rendering, and its recorder can reenact a simulation. That architecture is useful because teams can locate which layer carries the evidence instead of assigning equal importance to every layer.

Each decision also needs a tolerance. “Wheel slip matters” is vague. “The simulator must predict stopping distance within eight centimeters on the three production floor coatings” can fail cleanly. A failed tolerance tells the team where to spend the next unit of fidelity budget.

## A smooth picture can hide bad evidence

Rendered motion can look persuasive while the underlying timing is wrong. Godot documents that physics runs on fixed ticks, while visual frames may arrive at another rate. Changing the physics tick rate can alter controls, collisions, and trajectories; interpolation can smooth the display, but it adds a small visual delay.

For robot products, this distinction is not cosmetic. A beautiful video may conceal stale sensor timestamps, unrealistic controller cadence, or impossible compute latency. Review the event clock and measurement path before reviewing the movie.

## Close the gap with recorded evidence

The strongest budget review compares simulation with production traces. NVIDIA’s Isaac Sim guidance makes a sharp point: matching one solver configuration to another proves consistency between simulations, not agreement with a physical robot. Its workflow uses recorded motion, separates calibration from validation, and asks whether the tuned model improves results on held-out data.

That is a good product habit. Preserve field runs, version their inputs, and link each fidelity claim to a replayable case. A simulator should produce a reality receipt: the trace, tolerance, and held-out result behind the claim. The same discipline that makes [robot incidents reproducible](/blog/2026/10/16/make-every-robot-incident-reproducible/) also makes simulator upgrades auditable.

## Spend where mistakes cost the most

Fidelity is not a permanent asset. It expires when hardware, firmware, environments, or operating policies change. Review the budget when a decision changes, not on a ceremonial quarterly cycle.

The goal is not a digital world that fools the eye. It is a model that earns trust for a named decision, reveals where that trust stops, and gets cheaper everywhere else. That simulator may look uneven. Good. Its realism has a job.

## Sources

- [CARLA Simulator: Introduction](https://carla.readthedocs.io/en/latest/start_introduction/)
- [NVIDIA Isaac Sim: Sim-to-Sim System Identification](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_system_identification_simsim.html)
- [Godot Engine: Introduction to Physics Interpolation](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/physics_interpolation_introduction.html)
