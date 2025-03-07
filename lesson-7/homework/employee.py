class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.file_path = 'employees.txt'
        self.loadEmployees()

    def loadEmployees(self):
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 4:
                        self.employees.append({
                            'ID': int(data[0]),
                            'Name': data[1],
                            'Position': data[2],
                            'Salary': int(data[3])
                        })
        except FileNotFoundError:
            pass

    def saveEmployees(self):
        with open(self.file_path, 'w') as f:
            for emp in self.employees:
                f.write(f"{emp['ID']},{emp['Name']},{emp['Position']},{emp['Salary']}\n")

    def addEmployee(self, emp_id, name, position, salary):
        self.employees.append({'ID': emp_id, 'Name': name, 'Position': position, 'Salary': salary})
        self.saveEmployees()
        print("Employee added successfully.")

    def viewEmployees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                print(f"{emp['ID']}, {emp['Name']}, {emp['Position']}, {emp['Salary']}")

    def searchEmployee(self, emp_id):
        for emp in self.employees:
            if emp['ID'] == emp_id:
                print(f"{emp['ID']}, {emp['Name']}, {emp['Position']}, {emp['Salary']}")
                return
        print("Employee not found.")

    def updateEmployee(self, emp_id):
        for emp in self.employees:
            if emp['ID'] == emp_id:
                print("Current Employee Details:")
                self.searchEmployee(emp_id)
                emp['Name'] = input("Write new name: ")
                emp['Position'] = input("Write new position: ")
                emp['Salary'] = int(input("Write new salary: "))
                self.saveEmployees()
                print("Employee information updated.")
                return
        print("Employee not found.")

    def delEmployee(self, emp_id):
        for emp in self.employees:
            if emp['ID'] == emp_id:
                self.employees.remove(emp)
                self.saveEmployees()
                print("Employee deleted.")
                return
        print("Employee not found.")


manager = EmployeeManager()
while True:
    choice = input("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n")

    if choice == '1':
        emp_id = int(input("Enter ID: "))
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = int(input("Enter salary: "))
        manager.addEmployee(emp_id, name, position, salary)
    elif choice == '2':
        manager.viewEmployees()
    elif choice == '3':
        emp_id = int(input("Enter Employee ID to search: "))
        manager.searchEmployee(emp_id)
    elif choice == '4':
        emp_id = int(input("Enter Employee ID to update: "))
        manager.updateEmployee(emp_id)
    elif choice == '5':
        emp_id = int(input("Enter Employee ID to delete: "))
        manager.delEmployee(emp_id)
    elif choice == '6':
        break
    else:
        print("Invalid option. Please try again.")
