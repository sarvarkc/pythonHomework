import sqlite3

class Library:
    def __init__(self):
        pass

    def create(self):
        create_table = """
            CREATE TABLE Books(
            Title TEXT,
            Author TEXT,
            Year_Published INT,
            Genre TEXT
            );"""
       
        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.execute(create_table)

    def insert(self):
        insert_values = (
            ("To Kill a Mockingbird","Harper Lee",1960,"Fiction"),
            ("1984","George Orwell",1949,"Dystopian"),
            ("The Great Gatsby","BF. Scott Fitzgerald",1925,"Classic")
        )

        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.executemany("INSERT INTO Books VALUES(?, ?, ?, ?)", insert_values)

    def update(self):
        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title == '1984'")

    def show_sorted(self):
        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT Title, Author FROM Books WHERE Genre == 'Dystopian';")
        for x in cursor.fetchall():
            print(x[0],",",x[1])

    def delete(self):
        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.execute("DELETE FROM Books WHERE Year_Published<1950")

    def add_column(self):
        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.execute("ALTER TABLE Books ADD COLUMN Rank TEXT")
            cursor.execute("UPDATE Books SET Rank = '4.8' WHERE Year_Published == 1960")
            cursor.execute("UPDATE Books SET Rank = '4.7' WHERE Year_Published == 1950")

    def sortt(self):
        with sqlite3.connect("library.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Books ORDER by Year_Published;")
        for x in cursor.fetchall():
            print(x[0],",",x[1],",",x[2])


library = Library()
#library.create()
#library.insert()
#library.update()
#library.show_sorted()
#library.delete()
#library.add_column()
#library.sortt()