# Banking system made with python

# Create Account
def create_acc():
    name = input('Enter your name :')
    balance = float(input('Enter initial balance :'))
    print(f'Account created successfully for {name} with ₹{balance:.2f} initial balance')
    return {'name': name,'balance':balance }

# Debit
def debit(account):
    amount = float(input('Enter amount to deposit :'))
    account['balance'] += amount
    print(f"₹{amount:.2f} deposited successfully!")
    print(f"New Balance: ₹{account['balance']:.2f}")

# Credit
def credit(account):
    amount = float(input('Enter amount to withdraw :'))
    if(amount>account['balance']):
        print('Insufficient balance!')
    else:
        account['balance'] -= amount
        print(f"₹{amount:.2f} withdrawn successfully!")
        print(f"Remaining Balance: ₹{account['balance']:.2f}")

# Check balance
def check_balance(account):
     print(f"Account Holder: {account['name']}")
     print(f"Current Balance: ₹{account['balance']:.2f}")

# main function
def main():
    print("🏦 Welcome to Simple Bank 🏦")
    account = create_acc() 

    while True:
        print('\n===Menu===')
        print('1. Debit')
        print('2. Credit')
        print('3. Check balance')
        print('4. Exit')

        choice = input('Enter choice (1-4)')

        # if
        if(choice=='1'):
            debit(account)
        elif(choice=='2'):
            credit(account)
        elif(choice=='3'):
            check_balance(account)
        elif(choice=='4'):
            print('Thanks fro using 🏦')
            break
        else:
            print('Error, Try again')

if __name__ == '__main__':
    main()