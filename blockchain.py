blockchain = [[1]]


def get_last_value():
    """Returns the last value of the current blockchain"""
    return blockchain[-1]

def add_value(transaction_ammount,last_transaction_ammount=[1]):
     """Append new value as well as the last block chain value to the blockchain
     arguements:
     :transaction_ammount:The ammount that should be added.
     :last_transaction_ammount:The last transaction ammount(default[1])
     """
     blockchain.append([last_transaction_ammount,transaction_ammount])

def get_user_input():
    """Returns the input of the user as float"""
    return float(input("Enter the ammount: "))

   
amount = get_user_input()
add_value(amount)
amount = get_user_input()
add_value(last_transaction_ammount=get_last_value(),transaction_ammount = amount)
amount = get_user_input()
add_value(amount,get_last_value())
print(blockchain)