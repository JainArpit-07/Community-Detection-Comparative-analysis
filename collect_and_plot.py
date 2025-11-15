import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv("results_cdnmf.csv")
b = pd.read_csv("results_cigcl.csv")

merged = a.copy()
merged["nmi_cigcl"] = b["nmi"]
merged["ari_cigcl"] = b["ari"]
merged["acc_cigcl"] = b["acc"]

plt.figure()
plt.plot(merged["dataset"], merged["nmi"], marker='o', label="CDNMF")
plt.plot(merged["dataset"], merged["nmi_cigcl"], marker='s', label="CI-GCL")
plt.legend()
plt.savefig("cmp_nmi.png")
