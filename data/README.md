# Data Folder Descriptions

## app_data

Contains the data used by the app (called using the function in `src\app\app_wrangling.py`).

## raw

Data downloaded that still needs to be processed by `wrangle_data.py`.
The raw data is first filtered to only contain entries with greater than or equal to 50 user ratings, and to be within the years of 1950 and 2021.
Also the raw data has ids instead of names for several columns (eg mechanic or category). So this script converts the ids to the corresponding names via a look up table.

## processed

Data from the `raw` folder that has been processed by `wrangle_data.py`. Data in this folder is directly useable by the app.

## lookups

json files used by `wrangle_data.py` to process raw data, i.e convert columns that contain ids into columns that contain names.
