"""
projekt_03.py: třetí projekt do Engeto Online Python Akademie

author: Pavel Křivan
email: paja6700@gmail.com
discord: pavel007111
"""

#import necessary libraries
import sys
import requests
from bs4 import BeautifulSoup
import csv

#party names
party_names = [
    "Občanská demokratická strana",
    "Řád národa - Vlastenecká unie",
    "CESTA ODPOVĚDNÉ SPOLEČNOSTI",
    "Česká str.sociálně demokrat.",
    "Radostné Česko",
    "STAROSTOVÉ A NEZÁVISLÍ",
    "Komunistická str.Čech a Moravy",
    "Strana zelených",
    "ROZUMNÍ-stop migraci,diktát.EU",
    "Strana svobodných občanů",
    "Blok proti islam.-Obran.domova",
    "Občanská demokratická aliance",
    "Česká pirátská strana",
    "OBČANÉ 2011-SPRAVEDL. PRO LIDI",
    "Referendum o Evropské unii",
    "TOP 09",
    "ANO 2011",
    "SPR-Republ.str.Čsl. M.Sládka",
    "Křesť.demokr.unie-Čs.str.lid.",
    "Česká strana národně sociální",
    "REALISTÉ",
    "SPORTOVCI",
    "Dělnic.str.sociální spravedl.",
    "Svob.a př.dem.-T.Okamura (SPD)",
    "Strana Práv Občanů"
]

def format_number(value):
    try:
        clean_value = value.replace(" ", "")  
        return f"{int(clean_value):,}".replace(",", " ")  
    except (ValueError, AttributeError):
        return value

def get_page_content(link):
    response = requests.get(link)
    if response.status_code != 200:
        print(f"Error: Unable to fetch page {link}")
        return None
    return BeautifulSoup(response.text, 'html.parser')

def get_basic_info(soup):
    table = soup.find('table', {'id': 'ps311_t1'})
    if not table:
        print("Error: Table with ID 'ps311_t1' not found.")
        return None, None, None

    rows = table.find_all('tr')
    try:
        registered = format_number(rows[2].find_all('td')[3].text.strip())
        envelopes = format_number(rows[2].find_all('td')[4].text.strip())
        valid_votes = format_number(rows[2].find_all('td')[7].text.strip())
        return registered, envelopes, valid_votes
    except (IndexError, AttributeError):
        return None, None, None