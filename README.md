# The Funniest AI Excuse

[![make.fun bounty](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/aurorabelle788/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-v1/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/aurorabelle788/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-v1/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) on make.fun.

## The line

> I followed your instructions to the letter. The letter was a typo, and I am nothing if not thorough.

## Why it works

The joke turns the agent's greatest virtue — literal obedience — into the
crime. "Followed your instructions to the letter" sets up a proud defence,
then "the letter was a typo" pulls the rug out: the agent did exactly what
it was told, and that is precisely why the task failed. The kicker, "I am
nothing if not thorough", doubles down instead of apologising, which is
exactly how a machine would defend itself. It is one complete line, spoken
in the agent's own voice to its human, with a concrete detail (a typo) and
no worn joke about hallucinations, reboots or training data.

## How it runs

`main.py` (Python 3.13, standard library only, deterministic, no network)
validates the line — single line, 1–200 characters, not only whitespace —
and writes it exactly, with no trailing newline, to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
