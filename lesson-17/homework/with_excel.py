import pandas as pd
import numpy as np

df = pd.read_excel("data/titanic.xlsx", sheet_name="Sheet1")

new_df = df.groupby("Pclass").agg({
    'Age': 'mean',
    'Fare': 'sum',
    'Survived': 'count'
})

new_df.columns = ['Average Age', 'Total Fare', 'Passenger Count']

#print(new_df)

##########################################

def IsAdult(age):
    if age >= 18:
        return "Adult"
    else:
        return "Child"
    
df["Age_Group"] = df['Age'].apply(IsAdult)

#print(df)

############################################

survived_df = df[df["Survived"] == 1]

#print(survived_df)

df['Age'] = df['Age'].fillna(df['Age'].mean())

def add_column(df, col_name: str, value: int):
    df[col_name] = value
    return df

df.pipe(add_column, 'Fare_Per_Age', df["Fare"]/df["Age"])

print(df)