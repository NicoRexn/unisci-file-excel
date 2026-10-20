import pandas as pd
from pathlib import Path

cartella = Path("file_da_unire")
tabelle = []

for f in cartella.glob("*.xlsx"):
    t = pd.read_excel(f)
    t["File"] = f.name
    tabelle.append(t)

unito = pd.concat(tabelle, ignore_index=True)
unito = unito.drop_duplicates(subset=["Prodotto", "Quantita"])

riepilogo = unito.groupby("Prodotto", as_index=False)["Quantita"].sum()

with pd.ExcelWriter("report_unito.xlsx") as writer:
    unito.to_excel(writer, sheet_name="Dati", index=False)
    riepilogo.to_excel(writer, sheet_name="Riepilogo", index=False)

print(f"Uniti {len(tabelle)} file, {len(unito)} righe, report salvato")