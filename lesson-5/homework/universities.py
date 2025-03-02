import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(info):
    students = []
    tutition = []
    for x in info:
        students.append(x[1])
        tutition.append(x[2])

    print("Total students", sum(students))
    print("Total tuition: $", sum(tutition))

def mean(info, do):
    students = []
    tutition = []
    for x in info:
        students.append(x[1])
        tutition.append(x[2])

    if do == True:
        print("Student mean:", round(statistics.mean(students),2))
    else:
        print("Tuition mean: $", round(statistics.mean(tutition),2))

def median(info, do):
    students = []
    tutition = []
    for x in info:
        students.append(x[1])
        tutition.append(x[2])

    if do == True:
        print("Student median:", statistics.median(students))
        print('\n')
    else:
        print("Tuition median: $", statistics.median(tutition))

enrollment_stats(universities)
print('\n')
mean(universities, True)
median(universities, True)
mean(universities, False)
median(universities, False)