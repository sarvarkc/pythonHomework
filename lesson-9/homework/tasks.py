import json
import csv

class Manager:
    def __init__(self):
        self.path = "tasks.json"
        self.csv_path = "tasks.csv"
        self.list = []

    def open(self):
        with open(self.path, "r") as file:
            data = json.load(file)
            print(data)

    def stats(self):
        with open(self.path, "r") as file:
            data = json.load(file)
            print("Total tasks:",len(data))
           
            i = 0
            for x in data:
                if x["completed"] == True:
                    i += 1
            print("Total completed tasks:", i)

            q = 0
            for x in data:
                if x["completed"] == False:
                    q += 1
            print("Total pending tasks:", q)

            summ = 0
            p = 0
            for x in data:
                p += 1
                summ += x["priority"]
            print("Average priority:", summ/p)

    def transfrom(self):
        with open(self.path, "r") as file:
            data = json.load(file)
            columns = []
            for col in data:
                for i in col:
                    columns.append(i)
                break
            
            info = []
            for col in data:
                d = []
                for i in col:
                    d.append(col[i])
                info.append(d)
            print(info)

        with open(self.csv_path, "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(info)


manager = Manager()
manager.open()
manager.stats()
manager.transfrom()