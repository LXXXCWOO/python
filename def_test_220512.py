from math import *
import inspect
import random


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")

    for lang in language:
        print(lang, end=" ")
    print()


balance = 0
balance = deposit(balance, 1000)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")

print(floor(4.99))

print(inspect.getfile(random))
