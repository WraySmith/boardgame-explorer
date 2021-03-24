# Scripts directory description

This directory holds files for gathering and processing data.

Paths to the various data files are relative, thus all these scripts are to be run from the root of this repository.

`data/raw/bgg_GameItem.csv` is an updated board game dataset, it is used for its updated list of board game ids for bgg.

Run `bgg_api_querier.py` to get a dataframe of all board games with names in the columns. Produces `./data/raw/bgg_data_from_api.csv`

Then run `wrangle.py` to filter `./data/raw/bgg_data_from_api.csv` to have published year greater than 1950, and to only include board games with atleast 50 user reviews. Also drops rows with non valid year published data. This files output is 

`utils.py` contains helper functions for our api caller files.  

`tsne_analysis.py` adds the x, y, z coordinates for the 3d plot in the application, and out puts the file `./data/app_data/bgg_data_tsne.csv`

Order of files run:

1) `bgg_api_querier.py`

2) `wrangle.py`

3) `tsne_analysis.py`
