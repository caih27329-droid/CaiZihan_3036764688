# Card & Krueger (1994) — Replication and Extension

Replication of *"Minimum Wages and Employment: A Case Study of the Fast-Food
Industry in New Jersey and Pennsylvania"* (Card & Krueger, 1994, *American
Economic Review*), plus an independent extension that estimates the effect of
the minimum-wage increase separately by restaurant chain.

## Requirements

- Python 3.8+
- Packages: `pandas`, `numpy`, `statsmodels`, `matplotlib`

Install with:

```
pip install pandas numpy statsmodels matplotlib
```

## Data

The raw data (`public.csv`) is the Card–Krueger restaurant survey data,
distributed by the course as Package 01. It contains 410 stores and two survey
waves (before and after the April 1992 minimum-wage increase in New Jersey).

Place the file at:

```
01_DID/data/public.csv
```

> The raw data is for coursework only. Do **not** upload it to a public
> repository; document how to obtain it instead.

## How to run

From the project root, run:

```
python code/analysis.py
```

The script reads the input data and writes all results to the `output/` folder.

## Output

| File | Content |
| --- | --- |
| `output/table2_means.csv` | Mean FTE employment by wave and state |
| `output/table3_did.csv` | Difference-in-differences regression (robust SEs) |
| `output/table4_controls.csv` | DID regression with chain and ownership controls |
| `output/extension_by_chain.csv` | DID estimated separately for each chain |
| `output/figure1_did.png` | Employment in NJ vs PA, before and after |
| `output/figure2_chain.png` | DID by chain, with error bars |

## Key results

- DID estimate = **2.75** FTE employees per store (robust SE = 1.34, p = 0.040)
- With controls = **2.78** (robust SE = 1.34)
- Original paper = **2.76** (SE = 1.36)

The results confirm Card & Krueger's finding: the New Jersey minimum-wage
increase did not reduce fast-food employment.
