import pandas as pd
from pathlib import Path

cartella = Path("file_da_unire")
cartella.mkdir(exist_ok=True)

for i in range(1, 4):
    dati = pd.DataFrame({
        "Prodotto": [f"Articolo {i}-{n}" for n in range(1, 6)],
        "Quantita": [n * i for n in range(1, 6)],
    })
    dati.to_excel(cartella / f"ordini_{i}.xlsx", index=False)