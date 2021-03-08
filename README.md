# Board Game Dashboard

![GitHub](https://img.shields.io/github/license/ubco-mds-2020-labs/dashboard-project-group14) [![GitHub Super-Linter](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

**Team:** Nathan Smith, Mitch Harris, Ryan Koenig, Sophia Bulcock

**The Board Game Dashboard can be found [here](https://boardgame-dashboard-data551.herokuapp.com/)!**

## Description

The Board Game Dashboard provides interactive exploration of a dataset of approximately 10,000 board games from the [Board Game Geek website](https://boardgamegeek.com/). The data includes board games with their descriptions, general game details, and user ratings and was obtained from the [R4DS TidyTuesday 2019-03-12 Github repository](https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-03-12).

The dashboard has following general functionality:

- Exploration of trends in board game features from 1950 to 2016.
- Summary of most popular board game features and board games based on user selections of game category, mechanics, publisher, and/or published year.

The best way to understand the functionality is just to check it out!

An exploratory data analysis was also prepared prior to the dashboard and can be read [here](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/blob/main/reports/exploratory_data_analysis/boardgame_EDA.ipynb).

## Status

The dashboard is currently under active development and will soon include the following updates (stay tuned!):

- Improved layout and aesthetics
- Revised game count vs published year bar chart
- Additional in-app user instructions.

## Enhancements

Several larger enhancements are also underway for the dashboard!

- Updated board game dataset available on [Kaggle](https://www.kaggle.com/mshepherd/board-games). The updated dataset is provided by the author of [Recommend.Games](https://recommend.games/) (very cool board game recommender using machine learning) but requires additional wrangling into a useable state for the dashboard.
- 3D visualization of the board game data. The visualization uses [T-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding) dimensionality reduction to plot board game categories and mechanics on two dimensions and the third dimension represents user rating. An exploratory analysis completed for this functionality can be found [here](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/blob/main/reports/tsne_analysis/).

## Getting Help or Reporting an Issue

To report bugs/issues/feature requests, please file an
[issue](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues).

These are very welcome!

## How to Contribute

If you would like to contribute, please see our
[CONTRIBUTING](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/blob/main/CONTRIBUTING.md)
guidelines.

Please note that this project is released with a [Contributor Code of
Conduct](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/blob/main/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.
