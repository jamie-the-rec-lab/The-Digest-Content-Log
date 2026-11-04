# What Uber's agentic shift teaches TA about implementing AI

- **Source:** TA Unboxed
- **Date:** 2026-08-07
- **Fetched:** 2026-08-07
- **Public URL:** https://taunboxed.substack.com/p/what-ubers-agentic-shift-teaches

## Newsletter

Most hiring advice focuses on doing more. My experience has been the opposite. The biggest breakthroughs often come from looking at the same problem from a different angle. That's what you'll find in every edition of TA Unboxed.

Starting today, I'm going to introduce you to a recent talk by the Uber development team at the Pragmatic Summit titled "Leading engineering through an agentic shift."

There were seven key points that I thought were most relevant to how we can adopt AI in TA. Because everyone is talking about AI, I'm finding the biggest issue is adoption, change management and implementation. Once the tools are in the hands of the people who know what to do, then the next issue becomes: why can't I have more tokens? But I see that as a good problem to have.

Treat these seven points as merely inspiration; some you might already be working on, and hopefully others will ignite your imagination for what you can do next.

Firstly, here is the technical overview of what Uber presented:

They started with Copilot-style assist (a ~10–15% velocity bump), then moved toward agentic workflows where work can be handed off asynchronously and returned as a PR. They built an internal "background AI helper" platform ("Minion") inside Uber's own systems, so the AI can see the real work context and make safe, useful changes. They started by using agents on small, low-risk tasks ("toil") where it is clear what "done" looks like (cleaning up old code, updating docs, upgrades, bug fixes). Once that was scaled, they invested in quality checks and risk controls, got people to use it, measured impact, and managed costs.

Why TA should care: We're all trying to use the same tools, but approaching it with different problems. You could argue it's the same implementation pattern, just applied to a different domain.
