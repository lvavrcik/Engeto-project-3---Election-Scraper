# Engeto-project-3---Election-Scraper
Kód pro 3. projekt Engeto - Election scraper

# Election scraper #
## Popis projektu ##
Cílem tohoto projektu je získat [výsledky voleb do Poslanecké sněmovny Parlamentu České republiky v roce 2017](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) pomocí scrapingu. 
Skript po zadání vybrané URL adresy stáhne data příslušných měst spolu s výsledky voleb a uloží je do vybraného CSV souboru.

### Instalace knihoven ###
Seznam požadovaných knihoven a jejich verzí je uložen v souboru `requirements.txt`.

Pro instalaci se doporučuje vytvořit nové virtuální prostředí.
Po vytvoření nainstalujte knihovny knihovny následujícím způsobem:

| Příkaz                                 | Popis                                   |
|----------------------------------------|----------------------------------------|
| `$ pip3 --version`                     | Ověří verzi správce balíčků             |
| `$ pip install -r requirements.txt`    | Nainstaluje knihovny z requirements.txt |

 ### Spuštění projektu ###
 Spuštění projektu se provádí přes terminál/příkazový řádek a vyžaduje 2 argumenty:
* Prvním argumentem je URL adresa odkazující na územní celek, který chceme scrapovat 
* Druhým argumentem je název výsledného souboru, do kterého bude tabulka uložena. Tento soubor musí končit příponou „.csv“

Celý příkaz vč. argumentů může vypadat takto:  
`Engeto-project3-Election_scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'vysledky_benesov.csv'`

### Ukázka projektu ###
Volební výsledky v okrese Benešov.
* 1. argument `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101`
* 2. argument `vysledky_benesov.csv`

**Spuštění skriptu**:  
`python Engeto-project3-Election_scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'vysledky_benesov.csv'`

**Průběh stahování/skriptu**:  
CONNECTING to: 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'  
DOWNLOADING DATA from: 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'  
SAVING DATA to: '<pathdescription>/vysledky_benesov.csv'  
Closing program 

**Částečný výstup**:
| Code   | City        | Registered | Envelopes | Valid | Občanská demokratická strana | ... |
|--------|-------------|------------|-----------|-------|------------------------------|-----|
| 529303 | Benešov     | 13 104     | 8 485     | 8 437 | 1 052                        | ... |
| 532568 | Bernartice  | 191        | 148       | 148   | 4                            | ... |
| ...    | ...         | ...        | ...       | ...   | ...                          | ... |