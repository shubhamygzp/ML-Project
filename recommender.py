from vectorizer import text_to_vector, cosine_similarity

def recommend_movies(df, movie_title):
    movie = df[df['title'] == movie_title].iloc[0]
    movie_vec = text_to_vector(movie['overview'])
    
    similarities = []
    for _, row in df.iterrows():
        if row['title'] != movie_title:
            sim = cosine_similarity(movie_vec, text_to_vector(row['overview']))
            similarities.append((row['title'], sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:5]