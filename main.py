from data_handler import load_and_clean_data
from recommender import recommend_movies

df = load_and_clean_data('movies.csv')
movie_title = "Avatar"
recommendations = recommend_movies(df, movie_title)
print("Top recommendations for", movie_title)
for title, score in recommendations:
    print(f"{title}: {score:.2f}")
