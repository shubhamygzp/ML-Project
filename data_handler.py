import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df = df[['title', 'genres', 'keywords', 'overview', 'cast', 'director']]
    df = df.dropna()
    return df