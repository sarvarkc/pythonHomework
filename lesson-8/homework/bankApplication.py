class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
class Bank:
    def __init__(self):
        self.data = []
        self.file_path = 'bank_data.txt'
        self.loadData()

    def loadData(self):
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 3:
                        self.data.append({
                            'ID': int(data[0]),
                            'Name': data[1],
                            'Balance': int(data[2])
                        })
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_path, 'w') as f:
            for x in self.data:
                f.write(f"{x['ID']},{x['Name']},{x['Balance']}\n")


    def create_account(self, name, balance):
        existing_ids = {account["ID"] for account in self.data}
        for x in range(1, 100000000):
            if x not in existing_ids:
                self.data.append({"ID":x,"Name": name, "Balance": balance})
                self.save_data()
                break
            else:
                continue

    def view_account(self, id):
        for x in self.data:
            if x["ID"] == id:
                return f"{x['ID']},{x['Name']},{x['Balance']}\n"
        return "Data not found"
        
    def deposit(self, id, amount):
        for x in self.data:
            if x["ID"] == id:
                x["Balance"] = x["Balance"] + amount
                self.save_data()
                return
        print("Data not found")
        
    def withdraw(self, id, amount):
        for x in self.data:
            if x["ID"] == id and amount<=x["Balance"]:
                x["Balance"] = x["Balance"] - amount
                self.save_data()
                return
        print("Error")        


manager = Bank()
while True:
    choice = input("1. Create new account\n2. View account details\n3. Deposit money\n4. Withdraw money\n5. Exit\n")

    if choice == '1':
        name = input("Enter name: ")
        balance = int(input("Top up your balance: "))
        manager.create_account(name, balance)
    elif choice == '2':
        acc_id = int(input("Enter your account number: "))
        print(manager.view_account(acc_id))
    elif choice == '3':
        acc_id = int(input("Enter your account number: "))
        if manager.view_account(acc_id) != "Data not found":
            balance = int(input("How much do you want to deposit: "))
            manager.deposit(acc_id, balance)
        else:
            manager.view_account(acc_id)
    elif choice == '4':
        acc_id = int(input("Enter your account number: "))
        if manager.view_account(acc_id) != "Data not found":
            balance = int(input("How much do you want to withdraw: "))
            manager.withdraw(acc_id, balance)
        else:
            manager.view_account(acc_id)
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")