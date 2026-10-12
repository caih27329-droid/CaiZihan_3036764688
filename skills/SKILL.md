---
name: card-krueger-replication
description: Replicate Card & Krueger (1994) and generate the main tables and figures from the restaurant survey data.
---

# Card & Krueger (1994) Replication Skill

This skill regenerates the main tables and figures of the Card & Krueger (1994)
replication and its chain-level extension.

## When to use

Use this skill to reproduce the project's tables and figures from the raw
restaurant survey data.

## Steps

1. Confirm the raw data is at `data/raw/public.csv`.
2. From the project root, run `python code/run_all.py`.
3. Check the generated files in `outputs/tables/` and `outputs/figures/`.

## What it produces

- Table 2: mean FTE by wave and state.
- Table 3: difference-in-differences regression (robust SEs).
- Table 4: DID with chain and ownership controls.
- Extension: DID estimated separately by chain.
- Figure 1: employment in NJ vs PA before and after.
- Figure 2: DID by chain with error bars.

## Checks

- The DID estimate should be about 2.75 (robust SE about 1.34).
- The result should be close to the original paper (DID 2.76, SE 1.36).
