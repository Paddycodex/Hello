balance = 20000
# withdraw_ammount = int(0)
withdraw_ammount = int(input("Please enter withdraw amount :"))

if balance >= withdraw_ammount :
    print("Please take money")
    balance = balance-withdraw_ammount
else :
    print("withdraw amount is more than your balance")
print(" available amount =",balance)