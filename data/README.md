# Data Folder Descriptions

Data within these folder are processed using the scripts in the `src/scripts/` folder.
## raw

Data retrieved from the bgg api using `bgg_api_querier.py` that still needs to be processed by `wrangle_data.py`. The raw data is first filtered to only contain entries with greater than or equal to 100 user ratings, and having a publishing year of 1950 or greater.

Also contains `bgg_GameItem.csv`, which the `bgg_api_querier.py` uses to get a list of board game ids to ask the api for.
We need to find a way to get an updated list of board game ids.

## processed

Data from the `raw` folder that has been processed by `wrangle_data.py` and results in the file `bgg_wrangled.csv`. `bgg_wrangled.csv` is then processed by `tsne_analysis.py` which creates `bgg_data_tsne.csv`. `bgg_data_tsne.csv` is used directly by the app from this folder.
