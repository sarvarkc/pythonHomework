import pandas as pd

df = pd.read_csv("data/employee.csv")

df["Normalized_Salary"] = df.groupby("DEPARTMENT")["BASE_SALARY"].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

print(df)
