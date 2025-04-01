import pandas as pd

df = pd.read_csv("data/movie.csv")

df_color = df.drop(df.iloc[:, 2:], axis=1)
df_critic = df[['director_name', 'num_critic_for_reviews']]

left_join = df_color.merge(df_critic, on="director_name", how="left").shape[0]
outer_join = df_color.merge(df_critic, on="director_name", how="outer").shape[0]

#print(left_join)
#print(outer_join)

##############################################

df_grouped_color = df.groupby("color").agg({
    'num_critic_for_reviews':'sum',
    'duration': 'mean'
})

df_grouped_director = df.groupby("director_name").agg({
    'num_critic_for_reviews':'sum',
    'duration': 'mean'
})

#print(df_grouped_color)
#print(df_grouped_director)

#############################################

def HowLong(time):
    if time < 60:
        return "Short"
    elif 60<=time<120:
        return "Medium"
    else:
        return "Long"
    
df["HowLong"] = df['duration'].apply(HowLong)

print(df)