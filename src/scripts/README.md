# Scripts directory description

This directory holds files for gathering and processing data.

Paths to the various data files are relative, thus all these scripts are to be run from the root of this repository.

`data/raw/bgg_GameItem.csv` is an updated board game dataset, but it has ids for columns like category instead of names.

Run `scraper.py` to get a dataframe of all board games with names in the columns. Produces `./data/processed/bgg_with_scraped_names.csv`

Then run `wrangle.py` to join the scrapped dataframe from above with `data/raw/bgg_GameItem.csv` which gives us columns with names as well as user rating data. This file also filters rows to include only those with greater than 50 user reviews as well as rows between 1950 and 2021.

`utils.py` contains helper functions for our api caller files.  

`tsne_analysis.py` adds the x, y, z coordinates for the 3d plot in the application.

Order of files run:

1) `scraper.py`

2) `wrangle.py`

3) `tsne_analysis.py`
