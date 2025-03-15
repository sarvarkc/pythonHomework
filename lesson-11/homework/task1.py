import sqlite3

class Roster:
    def __init__(self):
        pass

    def create(self):
        create_table = """
            CREATE TABLE Roster(
            Name TEXT,
            Species TEXT,
            Age INT
            );"""
       
        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            cursor.execute(create_table)

    def insert(self):
        insert_values = (
            ("Benjamin Sisko","Human",40),
            ("Jadzia Dax","Trill",300),
            ("Kira Nerys","Bajoran",29)
        )

        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?)", insert_values)

    def update(self):
        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Age == 300")

    def show_bajoran(self):
        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT Name, Age FROM Roster WHERE Species == 'Bajoran';")
        for x in cursor.fetchall():
            print(x[0],",",x[1])

    def delete(self):
        insert_values = (
            ("Someone","Something",400),
            ("Anyone","Anything",20)
        )

        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?)", insert_values)
            cursor.execute("DELETE FROM Roster WHERE Age>300")

    def add_column(self):
        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            #cursor.execute("ALTER TABLE Roster DROP COLUMN Rank")
            cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
            cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Age == 40")
            cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Age == 300")
            cursor.execute("UPDATE Roster SET Rank = 'Major' WHERE Age == 29")
            cursor.execute("UPDATE Roster SET Rank = 'Junior' WHERE Age == 20")

    def sortt(self):
        with sqlite3.connect("roster.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Roster ORDER by Age desc;") #if don't add desc it will show ascending
        for x in cursor.fetchall():
            print(x[0],",",x[1],",",x[2])


roster = Roster()
#roster.create()
#roster.insert()
#roster.update()
#roster.show_bajoran()
#roster.delete()
#roster.add_column()
#roster.sortt()