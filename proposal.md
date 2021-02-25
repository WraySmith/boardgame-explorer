# Boardgame Dashboard Proposal
**Team:** Nathan Smith, Mitch Harris, Ryan Koenig, Sophia Bulcock 

## Motivation and Purpose
Our role: Data scientist consultancy firm

Target Audience: Board game companies, board game designers and board game hobbyists

Board games have been a popular past time since the 1950’s. Starting up and owning a board game company, as well as designing board games, can pay very well and be a personally rewarding career or hobby. To maximize profit and popularity, it is important to understand the trends seen in board games over time, to make games that people are interesting in buying and playing. To address this, we are proposing to design a data visualization app that allows board game companies, game designers and board game hobbyists to visually explore a dataset from the [Board Game Geek website](https://boardgamegeek.com/). Users can use the app to identify trends in board games over a period from 1950 to 2021. Our app will be able to show the distributions of factors contributing to board game popularity and ratings, as well as investigate the trends seen over time with respect these factors. Users will be able to explore these trends by filtering by time period and can use this information to make decisions about what types of games and game factors contribute to a successful board game. 

## Description of the Data
The proposed dashboard will visualize a dataset of approximately 10,000 boardgames published between 1950 and 2021. The dataset comes from the [Board Game Geek website](https://boardgamegeek.com/) and includes boardgames with descriptions, general game details, publisher, and user ratings. The dataset is available on [Kaggle](https://www.kaggle.com/mshepherd/board-games) and is regularly updated with the latest data.

Numerical game details include features such as min/max players and min/max/ave playing time, while categorical game details include features such as `category` and  `mechanic`. Note that the categorical features can have multiple values. For example, the `mechanic` feature for an individual boardgame may have both "Area Control" and "Area Influence" as values. The publishing information includes `year_published` and features for the `author`, `designer`, and `publisher`. The `publisher` feature is missing the least amount of values in the datasets compared with `author` and `designer`. The user rating features include the boardgame average user rating (`average_rating`) as well as the number of users that have provided a rating (`users_rated`).  There are currently no derived features anticipated for the dataset.

## Research Questions and Usage Scenario
To get an idea of how one would use this dashboard, we can look at a scenario:

Sarah is a long time board game hobbyist and through some encouragment from her friends has decided to she is going to endevour in developing a board game of her own. She wants to try and find what are the reasons behind why some board games are immensly popular and why some are not. Sarah discovered the **Insert App Name Here** and first set about looking at which category of game she should develop. She wanted to build a game where there was a high amount of interest but not a flooded market and found that Trains and City Building games generally recieved high reviews but there were not too many of them in the market. She was also discovered that having a game that functioned with two to four players was the most typical. She was then able to filter the data by these variables in order to see what games already exist and also to compare how succesful each of these games were compared to the amount of mechanics they have.  She now has a good idea of what parameters she wants to develop her game within.

## Description of App and Sketch
Text and image here
