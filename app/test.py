
import pandas as pd

data = pd.read_csv('board_game.csv')

category_ratings_df = data.copy()
category_ratings_df['category'] = category_ratings_df['category'].str.split(",")
category_ratings_df = category_ratings_df.explode('category')
list_categories=list(category_ratings_df.category.unique())

print(list_categories)

print(type(list_categories))
new=['Economic', 'Negotiation', 'Political']

print(new)
print(type(new))