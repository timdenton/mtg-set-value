from bs4 import BeautifulSoup
import requests
import os


def remove_whitespace(s, i):
    """removes whitespace, empty lines, and dollar sign, returns float"""
    text =  s.replace(' ', '')
    if os.linesep.join([s for s in text.splitlines() if s])[1:] == '':
        return('None')
    else:
        return(float(os.linesep.join([s for s in text.splitlines() if s])[1:]))

def remove_whitespace_rarity(s, i):
    """removes whitespace, empty lines, and dollar sign, returns float"""
    text =  s.replace(' ', '')
    if os.linesep.join([s for s in text.splitlines() if s]) == '':
        return('None')
    else:
        return(os.linesep.join([s for s in text.splitlines() if s]))


def scrape_tcg(mtg_set):
    url = 'https://shop.tcgplayer.com/price-guide/magic/' + mtg_set
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    trs = soup.find_all('tr')  ## each tr is a card, except the first one

    ## Create lists of card prices and names from selected set
    prices = []
    cardnames = []
    rarities = []

    for i, tr in enumerate(trs[1:]):  ## enumerate only for debug reasons
        raw_price = tr.find(class_='marketPrice')
        price = remove_whitespace(raw_price.text, i)

        if price == 'None':
            prices.append(0.0)
        else:
            prices.append(price)

        raw_name = tr.find_all('a')
        cardnames.append(raw_name[1].text)

        raw_rarity = tr.find(class_='rarity')
        rarity = remove_whitespace_rarity(raw_rarity.text, i)
        rarities.append(rarity)

    return(prices, cardnames, rarities)


