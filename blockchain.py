blockchain = [[1]]


def get_last_value():
    return blockchain[-1]

def add_value(transaction_ammount,last_transaction_ammount=[1]):
    blockchain.append([last_transaction_ammount,transaction_ammount])

def get_user_input():
    return float(input("Enter the ammount: "))

   
amount = get_user_input()
add_value(amount)
amount = get_user_input()
add_value(last_transaction_ammount=get_last_value(),transaction_ammount = amount)
amount = get_user_input()
add_value(amount,get_last_value())
print(blockchain)