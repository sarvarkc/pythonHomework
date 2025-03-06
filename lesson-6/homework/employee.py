main_dict = []

def addEmployee(id,name,pos,sal):
    dict1 = {
        'ID': id,
        'Name': name,
        "Position": pos,
        "Salary": sal
    }
    main_dict.append(dict1)
    with open('employees.txt', 'w') as f:
        for x in main_dict:
            f.write(','.join(map(str,x.values()))+'\n')
    print("Employee is added")

def viewEmployees():
    with open('employees.txt') as f:
        return f.read()
    
def searchEmployee(id):
    toggle = 1
    for x in range(len(main_dict)):
        if id == main_dict[x]['ID'] and toggle == 1:
            print(','.join(map(str,main_dict[x].values()))+'\n')
            toggle = 0
            break
    if toggle == 1:
        print('Employee not found')
def updateEmployee(id):
    toggle = 1
    for x in range(len(main_dict)):
        if id == main_dict[x]['ID']:
            searchEmployee(id)
            main_dict[x]['Name'] = input("Write name:")
            main_dict[x]['Position'] = input("Write position: ")
            main_dict[x]['Salary'] = int(input("Write salary: "))
            with open('employees.txt', 'w') as f:
                for x in main_dict:
                    f.write(','.join(map(str,x.values()))+'\n')
            print("Information is changed")
            toggle = 0
    if toggle == 1:
        searchEmployee(id)

def delEmployee(id):
    toggle = 1
    for x in range(len(main_dict)):
        if id == main_dict[x]['ID']:
            main_dict.remove(main_dict[x])
            print("Info is deleted")
            toggle = 0
        with open('employees.txt', 'w') as f:
            for x in main_dict:
                f.write(','.join(map(str,x.values()))+'\n')
    if toggle == 1:
        searchEmployee(id)


while True:
    num = input("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n")
    if num == '1':
        add_id = int(input("Write ID: "))
        add_name = input("Write name: ")
        add_pos = input("Write position: ")
        add_salary = int(input("Write salary: "))
        addEmployee(add_id,add_name,add_pos,add_salary)
    elif num == '2':
        print(viewEmployees())
    elif num == '3':
        searchEmployee(int(input()))
    elif num == '4':
        updateEmployee(int(input()))
    elif num == '5':
        delEmployee(int(input()))
    elif num == '6':
        break
    else:
        print("Wrong number")
