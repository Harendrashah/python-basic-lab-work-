class BankAccount:
    def _init_(self, accNo, money=100):
        self.__acc_number = accNo
        self.__balance = money

    def get_account(self):
        return self.__acc_number

    def get_balance(self):
        return self._balance
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount
    def transfer(self, amount, acc):
        self._balance -= amount,acc.deposit(amount)