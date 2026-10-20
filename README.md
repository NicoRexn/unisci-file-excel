# Unisci file Excel

Script Python che unisce automaticamente tutti i file Excel di una cartella in un unico report.

## Cosa fa
- Unisce tutti i file .xlsx presenti nella cartella
- Aggiunge una colonna con il nome del file di origine
- Elimina le righe duplicate
- Crea un foglio di riepilogo con i totali per prodotto

## Come si usa
1. Installa Python e le librerie: `pip install pandas openpyxl`
2. Metti i file Excel nella cartella `file_da_unire`
3. Lancia `python unisci_v2.py`
4. Trovi il risultato in `report_unito.xlsx`

## Perché è utile
Evita di copiare e incollare a mano i dati di decine di file, risparmiando ore di lavoro e riducendo gli errori.
