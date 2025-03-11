import csv

class Students:
    def __init__(self):
        self.data = []
        self.grades_path = "grades.csv"
        self.average_grades_path = "average_grades.csv"
        self.columns = ["Subject", "Average Grade"]

    def open(self):
        with open(self.grades_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.data.append(row)

    def transform(self):
        subject_totals = {} 
        subject_counts = {}  

        for row in self.data:
            subject = row[1]
            grade = int(row[2])

            if subject in subject_totals:
                subject_totals[subject] += grade
                subject_counts[subject] += 1
            else:
                subject_totals[subject] = grade
                subject_counts[subject] = 1


        average_grades = [[subject, subject_totals[subject] / subject_counts[subject]] for subject in subject_totals]


        with open(self.average_grades_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.columns)
            writer.writerows(average_grades) 

        print("Computed Averages:", average_grades)


students = Students()
students.open()
students.transform()
