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
Text here

## Description of App and Sketch
Text and image here
