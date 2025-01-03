# Engeto-project-3---Election-Scraper
Code for 3rd Engeto project - Election scraper

**Čeština:**  
> [Přečtěte si českou verzi README](README_cs.md)

# Election scraper #
## Project description ##
The aim of this project is to extract the [results of the 2017 elections to the Chamber of Deputies of the Parliament of the Czech Republic](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) via scraping. 
The script, after specifying the selected URL, downloads the data of the corresponding cities along with the election results and saves them to the selected CSV file.

### Installation of libraries ###
The list of required libraries and their versions is stored in the requirements.txt file.

For installation, creating of a new virtual environment is recommended.
With the manager installed, you can install the libraries as follows:

| Command                                | Description                            |
|----------------------------------------|----------------------------------------|
| `$ pip3 --version`                     | Verifies the version of the package manager |
| `$ pip install -r requirements.txt`    | Installs libraries from requirements.txt |

 ### Starting the project ###
Starting the project is via terminal/command line and will require 2 arguments:
* First argument is the url from the "select municipality" column (marked with an "X")
* Second argument is the resulting file name in which the table will be saved. It must end with the extension ".csv".

The whole command then looks like this:  
`Engeto-project 3-Election scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'vysledky_benesov.csv'`

### Project example ###
Voting results for Benešov district.
* 1st argument `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101`
* 2nd argument `vysledky_benesov.csv`

**Running the script**:  
`Engeto-project 3-Election scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'vysledky_benesov.csv'`

**Download progress**:  
CONNECTING to: 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'  
DOWNLOADING DATA from: 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'  
SAVING DATA to: '<pathdescription>/vysledky_benesov.csv'  
Closing program 

**Partial output**:
| Code   | City        | Registered | Envelopes | Valid | Občanská demokratická strana | ... |
|--------|-------------|------------|-----------|-------|------------------------------|-----|
| 529303 | Benešov     | 13 104     | 8 485     | 8 437 | 1 052                        | ... |
| 532568 | Bernartice  | 191        | 148       | 148   | 4                            | ... |
| ...    | ...         | ...        | ...       | ...   | ...                          | ... |
