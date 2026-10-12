# AI Use Disclosure

This project uses AI assistance. This document records where and how AI was
used at each stage, and how its output was checked.

## 1. Understanding the paper

AI (Claude) helped explain Card & Krueger (1994): the research question, the
difference-in-differences design, and the full-time-equivalent (FTE) variable.
I checked this against the paper and the course data dictionary myself.

## 2. Data and variables

AI helped locate the relevant variables in `public.csv` (EMPFT, EMPPT, NMGRS,
STATE, CHAIN). I verified every variable against `data/raw/DATA_DICTIONARY.md`
and built the FTE measure myself: FTE = full-time + managers + 0.5 * part-time.

## 3. Code

AI drafted the Python code. I ran every line myself, fixed the file paths, and
confirmed the regressions used robust standard errors (HC1).

## 4. Results and checking

I compared every number with the original paper's Table 3 (DID = 2.76, SE =
1.36). My DID = 2.75, SE = 1.34. I also checked the balanced sample size
(384 stores) and the chain-level sample sizes.

## 5. Report writing

AI helped outline the report. I wrote and checked the final text myself.

## AI errors I corrected

At first, the AI said my standard error differed from the paper because I used
fewer control variables. I checked and found the real reason was the
robust-standard-error setting, not the number of controls.
