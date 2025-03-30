import pandas as pd
import sqlite3

with sqlite3.connect('data/chinook.db') as connection:
    df = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    )

print(df.head(10))