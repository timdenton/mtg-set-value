from web_scraper import scrape_tcg
from data_handling import combine_data
from os import path
# from mtg_math import *
# from visualization import *
# import sys
# import pprint as pp


## Which sets should be compared?
sets = ['zendikar-rising', 'core-set-2021', 'ikoria-lair-of-behemoths', 'theros-beyond-death', 'throne-of-eldraine']

if len(sets) < 2:
    print("Warning: Number of sets must be 2 or greater.")

if path.exists('data/price_data.csv') is False:
    ## get prices from TCGPlayer
    prices_and_names = []
    for mtg_set in sets:
        prices_and_names.append(scrape_tcg(mtg_set))


    ## combine data into single dataframe/.csv file
    df = combine_data(prices_and_names, sets)
    df.to_csv('data/price_data.csv', index=False)
else:
    print('.csv file already exists')

## do set statistics


## plot graphs


print("Hello world")