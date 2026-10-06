"""
Card & Krueger (1994) - Minimum Wage and Employment
Replication and Extension
=====================================================

Replicates the main results of Card & Krueger (1994) using the restaurant
survey data (public.csv), and adds an independent extension that estimates
the effect separately by chain.

Input:
    data file: 01_DID/data/public.csv

Output (written to the output/ folder):
    table2_means.csv         mean FTE by wave and state (Table 2)
    table3_did.csv           DID regression, robust SEs (Table 3)
    table4_controls.csv      DID regression with controls (Table 4)
    extension_by_chain.csv   DID estimated separately for each chain
    figure1_did.png          employment in NJ vs PA, before and after
    figure2_chain.png        DID by chain, with error bars

Usage:
    python code/analysis.py
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pathlib import Path

# ---- paths ----------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "01_DID" / "data" / "public.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

# ---- 1. read the data -----------------------------------------------------
df = pd.read_csv(DATA)
print(f"Loaded {len(df)} stores, {df.shape[1]} columns")

# ---- 2. build full-time-equivalent (FTE) employment -----------------------
# The paper's measure: FTE = full-time + managers + 0.5 * part-time.
df["fte1"] = df["EMPFT"] + df["NMGRS"] + 0.5 * df["EMPPT"]
df["fte2"] = df["EMPFT2"] + df["NMGRS2"] + 0.5 * df["EMPPT2"]

# ---- 3. Table 2: means by wave and state ----------------------------------
table2 = df.groupby("STATE")[["fte1", "fte2"]].mean().round(2)
table2.index = table2.index.map({1: "New Jersey", 0: "Pennsylvania"})
table2.to_csv(OUT / "table2_means.csv")
print("\nTable 2 - mean FTE by wave and state:")
print(table2)

# ---- 4. Table 3: DID regression (robust SEs) ------------------------------
bal = df.dropna(subset=["fte1", "fte2"]).copy()
bal["d_fte"] = bal["fte2"] - bal["fte1"]

X = sm.add_constant(bal["STATE"])
m3 = sm.OLS(bal["d_fte"], X).fit(cov_type="HC1")

res3 = pd.DataFrame({"coef": m3.params, "se": m3.bse,
                     "t": m3.tvalues, "pvalue": m3.pvalues})
res3.to_csv(OUT / "table3_did.csv")
print("\nTable 3 - DID regression (robust SEs):")
print(res3.round(3))

# ---- 5. Table 4: DID with controls ----------------------------------------
chain = pd.get_dummies(bal["CHAIN"], prefix="chain", drop_first=True).astype(int)
Xc = sm.add_constant(pd.concat([bal[["STATE", "CO_OWNED"]], chain], axis=1))
m4 = sm.OLS(bal["d_fte"], Xc).fit(cov_type="HC1")

res4 = pd.DataFrame({"coef": m4.params, "se": m4.bse,
                     "t": m4.tvalues, "pvalue": m4.pvalues})
res4.to_csv(OUT / "table4_controls.csv")
print("\nTable 4 - DID with controls (chain + ownership):")
print(res4.round(3))

# ---- 6. Extension: DID by chain -------------------------------------------
chain_names = {1: "Burger King", 2: "KFC", 3: "Roy Rogers", 4: "Wendy's"}
rows = []
for cid in [1, 2, 3, 4]:
    sub = bal[bal["CHAIN"] == cid]
    m = sm.OLS(sub["d_fte"], sm.add_constant(sub["STATE"])).fit(cov_type="HC1")
    rows.append({"chain": chain_names[cid], "n": len(sub),
                 "did": m.params["STATE"], "se": m.bse["STATE"]})
ext = pd.DataFrame(rows).set_index("chain")
ext.to_csv(OUT / "extension_by_chain.csv")
print("\nExtension - DID by chain:")
print(ext.round(2))

# ---- 7. Figure 1: employment in NJ vs PA ----------------------------------
means = df.groupby("STATE")[["fte1", "fte2"]].mean()
waves = ["Before (Feb 1992)", "After (Nov 1992)"]

plt.figure(figsize=(6, 4))
plt.plot(waves, means.loc[1].values, marker="o", label="New Jersey (treated)")
plt.plot(waves, means.loc[0].values, marker="o", label="Pennsylvania (control)")
plt.ylabel("Mean full-time-equivalent employment")
plt.title("Employment in NJ vs PA before and after the minimum-wage increase")
plt.legend()
plt.savefig(OUT / "figure1_did.png", dpi=150, bbox_inches="tight")
plt.close()

# ---- 8. Figure 2: DID by chain (bar chart) --------------------------------
plt.figure(figsize=(7, 4))
plt.bar(ext.index, ext["did"], yerr=ext["se"], capsize=4)
plt.axhline(0, color="gray", linewidth=0.8)
plt.ylabel("DID estimate (FTE employees)")
plt.title("Effect of the minimum-wage increase, by chain")
plt.savefig(OUT / "figure2_chain.png", dpi=150, bbox_inches="tight")
plt.close()

# ---- summary --------------------------------------------------------------
print("\n===== SUMMARY =====")
print(f"DID (no controls)   = {m3.params['STATE']:+.2f}  (robust SE {m3.bse['STATE']:.2f})")
print(f"DID (with controls) = {m4.params['STATE']:+.2f}  (robust SE {m4.bse['STATE']:.2f})")
print(f"\nDone. Results saved to {OUT}")
