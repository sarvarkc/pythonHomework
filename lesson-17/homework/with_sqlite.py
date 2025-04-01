import pandas as pd
import sqlite3

with sqlite3.connect('data/chinook.db') as connection:
    df_customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM customers", con=connection)
    df_invoices = pd.read_sql("SELECT CustomerId, InvoiceId FROM invoices", con=connection)

invoice_counts = df_invoices.groupby("CustomerId").size().reset_index(name="TotalInvoices")

result = df_customers.merge(invoice_counts, on="CustomerId", how="inner")

print(result)














"""
with sqlite3.connect('data/chinook.db') as connection:
    df_customers = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    )
    df_invoices = pd.read_sql(
        "SELECT * FROM invoices",
        con=connection
    )

merged_df = pd.merge(df_customers, df_invoices, on="CustomerId")
#print(merged_df)

merged_df_no_dublicates = merged_df.drop_duplicates(subset=["CustomerId"])
invoice_values = merged_df["CustomerId"].value_counts()
total_invoices = pd.merge(merged_df_no_dublicates, invoice_values, on="CustomerId")
dropped_result = total_invoices.drop(total_invoices.iloc[:, 3:21], axis=1)
print(dropped_result)"
"""