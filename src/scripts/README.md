# Scripts directory description

This directory holds files for gathering and processing data.

Paths to the various data files are relative, thus all these scripts are to be run from the root of this repository.

There are two python files (`direct_api_caller.py` and `indirect_api_caller`) for creating id to name look up tables.
`direct_api_caller.py` uses the boardgame geeks' api for the group (publisher, artist, or designer).  
`indirect_api_caller` is for groups that do not have an api call (eg mechanic or category), so instead it finds the required data by calling the board game geeks' api for a boardgame, and gets the information that way.  

`wrangle_data.py` takes the raw data and turns it into our processed data by first applying our id name lookup tables, then applies some filtering.  

`compare_datasets.py` is to sanity check that our new processed dataset resembles the dataset we used in our initial EDA.  

`utils.py` contains helper functions for our api caller files.  
