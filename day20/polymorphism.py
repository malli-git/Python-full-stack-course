'''#polymorphism
class Snapchat:
    def __init__(self,username,password,friends):
        self.username = username
        self.__password = password
        self._friends = friends

    def getpassword(self):
        return self.__password
    
    def setpassword(self,new_password):
        self.__password = new_password

    @property
    def oprFriends(self):
        return self. friends
    @oprFriends.setter
    def oprFriends(self,newfriends):
        self._friends.append(newfriends)


saaketh = Snapchat('saaketh','12445',['praveen','nikhil'])

print(f'Name before modification: {saaketh.username}')
saaketh.username = 'sapnil'
print(f'Name after modification: {saaketh.username}')

print(f'password before modification: {saaketh.getpassword()}')
saaketh.setpassword('s@123')
print(f'password after modification: {saaketh.getpassword()}')

print(f'Friends before modification: {saaketh.oprFriends}')
saaketh.oprFriends = 'abhinandhan'
print(f'Friends before modification: {saaketh.oprFriends}')
'''
# data abstraction
from abc import ABC,abstraction

class BankAccount:
    def checkbalance(self):
        print("You can checkout your balance")

    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
class SavingsAccount(self):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakhs per day u can withdraw")
    
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited")
    def withdraw(self):
        print("unlimited")
    
class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")
    def withdraw(self):
        print("1-2 lakhs per day u can withdraw")
    
class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20,000 to 1lakh per day")

class penssionAccount(BankAccount):
    def deposit(self):
        print("No deposit")
    def withdraw(self):
        print("40k per day u can withdraw")

print("----abhinandan-----")
abhinandan=CurrentAccount()
abhinandan.checkbalance()
abhinandan.deposit()
abhinandan.withdraw()

print("----praveen-----")
praveen=CurrentAccount()
praveen.checkbalance()
praveen.deposit()
praveen.withdraw()

print("----saaketh_nikhil-----")
saaketh_nikhil=CurrentAccount()
saaketh_nikhil.checkbalance()
saaketh_nikhil.deposit()
saaketh_nikhil.withdraw()

print("----shanmukh-----")
shanmukh=CurrentAccount()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.withdraw()

print("----swapnil-----")
swapnil=CurrentAccount()
swapnil.checkbalance()
swapnil.deposit()
swapnil.withdraw()




