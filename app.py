from flask import Flask, render_template, request

app = Flask(__name__)

class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
            Hello, how would you like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit 
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Goodbye!")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Deposited successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount < self.balance:
                self.balance -= amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Your balance is: ", self.balance)
        else:
            print("Invalid pin")

@app.route('/', methods=['GET', 'POST'])
def index():
    atm = Atm()

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        atm.user_input = user_input

        if user_input == "1":
            atm.create_pin()
        elif user_input == "2":
            atm.deposit()
        elif user_input == "3":
            atm.withdraw()
        elif user_input == "4":
            atm.check_balance()
        else:
            return render_template('result.html', message="Goodbye!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000)
