import pandas as pd
import numpy as np

df = pd.read_excel("data/titanic.xlsx", sheet_name="Sheet1")
print(df.head(5))

print(df[df['Age']>30])
print(df['Sex'].value_counts())

print(df['Age'].sum())
print(df['Age'].max())
print(df['Age'].min())