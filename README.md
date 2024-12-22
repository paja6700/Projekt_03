# Election Scraper pro výsledky voleb z roku 2017

## Python projekt 3 Engeto Akademie

Projekt využívající funkci Election scraper, který získává výsledky voleb z roku 2017 z webu volby.cz. 
Odkaz [ZDE](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

Příklad výběru lokality Kladno.
Odkaz [ZDE](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103)

Příklad výběru lokality Beroun.
Odkaz [ZDE](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102)

Data se stahují, ukládají a exportují v souboru CSV.

## Instalace a požadavky

Vytvoření virtuálního prostředí a nainstalování potřebných knihoven:

```bash
cd /cesta_k_projektu
python -m venv venv
source venv/bin/activate   # Pro Linux/Mac
venv\Scripts\activate      # Pro Windows
pip install -r requirements.txt
```

`````markdown
## Spuštění projektu

Spuštění souboru projekt_03.py

Skript vyžaduje dva argumenty: URL stránky s výsledky a název výstupního souboru CSV.

## Příklad spuštění:

Výsledky hlasování Plzeň město

1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103
2. argument: vysledky_kladno.csv

Kompletní příklad:
python projekt_03.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103" vysledky_kladno.csv
