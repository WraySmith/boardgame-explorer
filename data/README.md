# Data Folder Descriptions


## raw

Data gotten from the bgg api that still needs to be processed by `wrangle_data.py`.
The raw data is first filtered to only contain entries with greater than or equal to 50 user ratings, and have a publishing year of 1950 or greater.
Also contains `bgg_GameItem.csv`, which the `bgg_api_querier.py` uses to get a list of board game ids to ask the api for.

## processed

Data from the `raw` folder that has been processed by `wrangle_data.py`. Data in this folder is directly useable by the app.
