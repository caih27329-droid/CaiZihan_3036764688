# Card & Krueger (1994) — Replication and Extension

Replication of *"Minimum Wages and Employment: A Case Study of the Fast-Food
Industry in New Jersey and Pennsylvania"* (Card & Krueger, 1994, *American
Economic Review*), plus an independent extension that estimates the effect of
the minimum-wage increase separately by restaurant chain.

## Requirements

- Python 3.8+
- Packages: `pandas`, `numpy`, `statsmodels`, `matplotlib`

```
pip install pandas numpy statsmodels matplotlib
```

## Project structure

| Path | Content |
| --- | --- |
| `report.pdf` | Final research report |
| `AI_USE_DISCLOSURE.md` | How AI was used at each stage |
| `code/run_all.py` | Single script that generates all tables and figures |
| `code/analysis_notebook.ipynb` | Exploratory notebook |
| `data/raw/` | Original input data (`public.csv`, restricted) |
| `data/processed/` | Processed data (balanced sample) |
| `outputs/tables/` | Generated tables (CSV) |
| `outputs/figures/` | Generated figures (PNG) |
| `skills/SKILL.md` | Reusable skill that generates the main tables and figures |

## Data

The raw data (`public.csv`) is the Card–Krueger restaurant survey data,
distributed by the course as Package 01. It contains 410 stores and two survey
waves (before and after the April 1992 minimum-wage increase in New Jersey).

Place the file at:

```
data/raw/public.csv
```

> The raw data is for coursework only. Do **not** upload it to a public
> repository; document how to obtain it instead. Column definitions are in
> `data/raw/DATA_DICTIONARY.md`.

## How to run

From the project root, run:

```
python code/run_all.py
```

The script reads `data/raw/public.csv` and writes all results to
`outputs/tables/` and `outputs/figures/`, plus the processed balanced sample
to `data/processed/`.

## Output

| File | Content |
| --- | --- |
| `outputs/tables/table2_means.csv` | Mean FTE employment by wave and state |
| `outputs/tables/table3_did.csv` | Difference-in-differences regression (robust SEs) |
| `outputs/tables/table4_controls.csv` | DID regression with chain and ownership controls |
| `outputs/tables/extension_by_chain.csv` | DID estimated separately for each chain |
| `outputs/figures/figure1_did.png` | Employment in NJ vs PA, before and after |
| `outputs/figures/figure2_chain.png` | DID by chain, with error bars |

## Key results

- DID estimate = **2.75** FTE employees per store (robust SE = 1.34, p = 0.040)
- With controls = **2.78** (robust SE = 1.34)
- Original paper = **2.76** (SE = 1.36)

The results confirm Card & Krueger's finding: the New Jersey minimum-wage
increase did not reduce fast-food employment.
