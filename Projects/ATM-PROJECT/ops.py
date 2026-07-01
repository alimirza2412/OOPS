class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""

         Hello, you are welcome to our bank
         please select the option you need
         1. Create your pin
         2. Check your bank balance
         3. Deposit amount
         4. Withdraw amount
         5. Exit
""")
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.check_balance()
            elif user_input == "3":
                self.deposit()
            elif user_input == "4":
                self.withdrawal()
            elif user_input == "5":
                print("Thank you, hope you liked our services")
                break
            else:
                print("Invalid option, please try again")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Your pin has been successfully created", flush=True)

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid pin")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")

    def withdrawal(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance = self.balance - amount
                print("Withdrawal successful")
        else:
            print("Invalid pin")


Atm()