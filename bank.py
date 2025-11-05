# Banking system made with python

# Create Account
def create_acc():
    name = input('Enter your name :')
    balance = float('Enter initial balance :')
    print('Account created Sucessfully fror {name} with {balance} initial balance')
    return {'name': name,'balance':balance }

# Debit
def debit():
    amount = float(input('Enter amount to deposit :'))
    amount['balance'] += amount
    print(f"₹{amount:.2f} deposited successfully!")
    print(f"New Balance: ₹{account['balance']:.2f}")

# Cre