import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

url = 'https://realpython.github.io/fake-jobs/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

jobs_data = [

]

def addData():
    for x in soup.find_all("footer", {"class": "card-footer"}):
        new_url = x.find_all('a')[1].get('href')
        new_res = requests.get(new_url)
        new_soup = BeautifulSoup(new_res.content, 'html.parser')

        JobTitle = new_soup.find("h1", {"class": "is-2"}).text
        CompanyName = new_soup.find("h2", {"class": "company"}).text
        Location = new_soup.find("p", {"id": "location"}).text[10:]
        Description = new_soup.find("div", {"class": "content"}).p.text
        Link = x.find_all('a')[1].get('href')
        jobs_data.append((JobTitle,CompanyName,Location,Description,Link))

def addToSql():
    create_table = """
        CREATE TABLE Jobs(
        JobTitle TEXT,
        CompanyName TEXT,
        Location TEXT,
        Description TEXT,
        Link TEXT
        );"""
    
    with sqlite3.connect("jobs.db") as con:
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS Jobs")
        cursor.execute(create_table)
        cursor.executemany("INSERT INTO Jobs VALUES(?, ?, ?, ?, ?)", jobs_data)

def addToCSV():
    columns = ["Job Title", "Company Name", "Location"]
    with sqlite3.connect("jobs.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT JobTitle, CompanyName, Location FROM Jobs")
        with open("jobs.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows(rows)    
addData()
addToSql()
addToCSV()