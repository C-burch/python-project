
def show_balance(balance):
     print("***********************************")
     print(f"**Your balance is £{balance:.2f}**")
     print("***********************************")

def deposit():
    amount = float(input("Enter the amount to be deposited"))

    if amount < 0:
        print("Thats not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("Insufficient funds")
        return 0 
    elif amount < 0:
        print("There isnt enough money in your account")
        return 0 
    else:
        return amount
        
    


def main(show_balance, deposit, withdraw):
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("**banking program**")
        print("*******************")
        print("1: Show Balance")
        print("2: Deposit")
        print("3: Withdraw") 
        print("4: Exit")

        choice = input("Enter your choice. 1 - 4: ")

        if choice == '1':
            show_balance()
        elif choice =='2':
            balance += deposit()
        elif choice =='3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice! ")

    print("Thank you. Have a wonderful day!")