import pandas as pd

def combine_data(scraper_data, sets):   
    """Combine all data into single dataframe and assign set names (=sets)"""

    frames = []
    for i, mtg_set in enumerate (scraper_data):

        data = {'Price $': mtg_set[0],
                'Card Name': mtg_set[1],
                'Rarity': mtg_set[2],
                'Set': [sets[i] for price in range(len(mtg_set[0]))],
        }

        frames.append(pd.DataFrame(data))

    return(pd.concat(frames, ignore_index=True))


