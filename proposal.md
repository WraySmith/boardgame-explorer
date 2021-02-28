# Board Game Dashboard Proposal

**Team:** Nathan Smith, Mitch Harris, Ryan Koenig, Sophia Bulcock

## Motivation and Purpose

Our role: Data scientist consultancy firm

Target Audience: Board game companies, board game designers and board game hobbyists

Board games have been a popular past time since the 1950’s. Starting up and owning a board game company, as well as designing board games, can pay very well and be a personally rewarding career or hobby. To maximize profit and popularity, it is important to understand the trends seen in board games over time, to make games that people are interesting in buying and playing. To address this, we are proposing to design a data visualization app that allows board game companies, game designers and board game hobbyists to visually explore a dataset from the [Board Game Geek website](https://boardgamegeek.com/). Users can use the app to identify trends in board games over a period from 1950 to 2021. Our app will be able to show the distributions of factors contributing to board game popularity and ratings, as well as investigate the trends seen over time with respect these factors. Users will be able to explore these trends by filtering by time period and can use this information to make decisions about what types of games and game factors contribute to a successful board game.

## Description of the Data

The proposed dashboard will visualize a dataset of approximately 10,000 boardgames published between 1950 and 2021. The dataset comes from the [Board Game Geek website](https://boardgamegeek.com/) and includes boardgames with descriptions, general game details, publisher, and user ratings. The dataset is available on [Kaggle](https://www.kaggle.com/mshepherd/board-games) and is regularly updated with the latest data.

Numerical game details include features such as min/max players and min/max/ave playing time, while categorical game details include features such as `category` and  `mechanic`. Note that the categorical features can have multiple values. For example, the `mechanic` feature for an individual board game may have both "Area Control" and "Area Influence" as values. The publishing information includes `year_published` and features for the `author`, `designer`, and `publisher`. The `publisher` feature is missing the least amount of values in the datasets compared with `author` and `designer`. The user rating features include the board game average user rating (`average_rating`) as well as the number of users that have provided a rating (`users_rated`).  There are currently no derived features anticipated for the dataset.

## Research Questions and Usage Scenario

To get an idea of how one would use this dashboard, we can look at a scenario:

Sarah is a long time board game hobbyist and has always wanted to develop one on her own. One of her friends discovered the Board Game dashboard and showed it to her. Looking through the dashboard, Sarah decided she now had the tools to start her game development. Her primary interests were to try and find out why some board games are immensly popular and why some are not. She first set about looking at which category of game she should develop. She wanted to build a game where there was a high amount of interest but not a flooded market and found that Trains and City Building games generally recieved high reviews but there were not too many of them in the market. She was also discovered that having a game that functioned with two to four players were the most typical. She was then able to filter the data by these variables in order to see what games already exist and also to compare how succesful each of these games were compared to the amount of mechanics they have.  She now has a good idea of what parameters she wants to develop her game within.

## Description of App and Sketch

The app includes two tabs. The first tab allows the user to explore board game trends using game categories, mechanics and publishers. The upper section of this tab allows the user to select subsets of these features from dropdown menus. The selections will be presented on a histogram of annual published counts and will also be highlighted on a scatter plot of average game ratings versus published year. The lower portion of the tab allows the user to select a subset of years using a slider and the top five to ten categories, mechanics, and publishers will be presented on bar charts.

The second tab allows the user to explore the most popular boardgames (based on average user rating) filtering on some or all of: categories, mechanics, publisher (using dropdown menus) and published year (using a slider). The user can also select the number of games they want shown using a slider. Features for each of these top selected games will be shown in table format and the average user ratings will also be shown on a bar chart.

An additional tab that may be provided as part of the app (not shown in the sketch below) depending on the timeline includes a two- or three-dimensional plot showing clustering of similar board games likely completed using a dimensionality reducing technique such as Principle Component Analysis. The plot would allow a user to highlight specific categories, mechanics, and publishers.

![dashboard 1](./images/dashboard_sketch_1.PNG)
*Figure 1: Board Game Dashboard Sketch (Tab 1)*

![dashboard 2](./images/dashboard_sketch_2.PNG)
*Figure 2: Board Game Dashboard Sketch (Tab 2)*