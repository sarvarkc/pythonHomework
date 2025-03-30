import pandas as pd

df = pd.read_csv("data/movie.csv")

print(df.sample(10))

df_new = df[df['duration']>120]
print(df_new.sort_values(by='director_facebook_likes', ascending=False)) 

director = df.sort_values(by='director_facebook_likes', ascending=False).head(1)
print(director["director_name"].values[0])

longest_df = df.sort_values(by='duration', ascending=False).head(5)
for director,movie in zip(longest_df['director_name'],longest_df['movie_title']):
    print(f"{movie} by {director}")