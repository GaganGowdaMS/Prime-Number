#Static Attributes
class User:
    user_count=0
    def __init__(self,username,email):
        self.username=username
        self.email=email
        User.user_count+=1

    def user(self):
        print(f"Username:{self.username},email:{self.email}")

user1=User("Danny","Danny@gmail.com")
user2=User("Sally","salamander@gmail.com")
user3=User("Gagan","Jonnybones@gmail.com")
print(User.user_count)

#BankAccount
import sys
class BankAccount:
    MIN_BALANCE=100
    def __init__(self, owner, Bankbalance):
        self.owner=owner
        self._Bankbalance=Bankbalance
        if self._Bankbalance==0:
            print("Min Balance is 100")
            sys.exit()

    @property
    def balance(self):
        return self._Bankbalance
    
    def Deposit(self,amount):
        if amount>0:
            self._Bankbalance+=amount
            print(f"{self.owner}'s New Balance:{self._Bankbalance}")
        else:
            print("Balance cannot be negative")

    def Withdraw(self,amount):
        if amount>0:
            self._Bankbalance-=amount
        if amount>self.balance:
            raise ValueError("Insufficient Funds")
        if amount<=0:
            raise ValueError("Withdraw Amount must be positive")
            print(f"{self.owner} withdrawed {amount}, New balnce is {self._Bankbalance}")

owner1=BankAccount("Alice Blue",700)
owner1.Withdraw(90)
owner1.Deposit(-54)
print(owner1.balance)