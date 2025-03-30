import pandas as pd

df = pd.read_json('data/iris.json')
print(df.shape)
print(df.columns)

new_columns = [column.lower() for column in df.columns]
df.columns = new_columns
print(df)
print(df[['sepallength','sepalwidth']])

print(df.select_dtypes('number').mean())
print(df.select_dtypes('number').median())
print(df.select_dtypes('number').std())