def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money): #출금
    if balance >=money:
        print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
        return balance - money
    else: 
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): 
    comission = 100
    return comission, balance - money - comission      

balance = 0
balance = deposit(0, 1000)
# print(balance)
# balance = withdraw(balance, 1500)
# balance = withdraw(balance, 500)
comission, balance = withdraw_night(balance, 500)
print("수수료는 {}원이며, 잔액은 {}원입니다.".format(comission,balance))