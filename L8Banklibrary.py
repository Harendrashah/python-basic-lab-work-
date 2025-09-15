import BankAccount

acc1=BankAccount(1)
acc2=BankAccount(2)
acc3=BankAccount(3)
acc4=BankAccount(4)

acc1.withdraw(10)
acc2.withdraw(20)
acc3.withdraw(30)
acc4.withdraw(40)

print(acc1.get_account(),acc1.get_balance())
print(acc2.get_account(),acc2.get_balance())
print(acc3.get_account(),acc3.get_balance())
print(acc4.get_account(),acc4.get_balance())


acc1.deposit(20)
acc2.deposit(10)
acc3.deposit(20)
acc4.deposit(10)

print(acc1.get_account(),acc1.get_balance())
print(acc2.get_account(),acc2.get_balance())
print(acc3.get_account(),acc3.get_balance())
print(acc4.get_account(),acc4.get_balance())