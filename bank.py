# Banking system made with python

# Create Account
def create_acc():
    name = input('Enter your name :')
    balance = float('Enter initial balance :')
    print('Account created Sucessfully fror {name} with {balance} initial balance')
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
    if(account>amount['balance']):
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
        print('\n===Menu===')