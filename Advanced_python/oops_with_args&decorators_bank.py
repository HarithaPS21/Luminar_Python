
class Bank:
    users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
    }
    session={}  # to store details of logged in users
    def validate_account(self,accno):
        if accno in Bank.users:
            return True
        else:
            return False

    def authenticate(self,**kwargs):
        accno=kwargs["accno"]
        password=kwargs["password"]
        user=self.validate_account(accno)
        if user:
            if (password == self.users[accno]["password"]):
                self.session["user"]=accno
                return accno
            else:
                return -1
        else:
            print("invalid account no.")
            return -1

    def balance_enquiry(self,accno):
        if accno==self.session["user"]:
            print(self.users[accno]["balance"])
        else:
            print("You must log in")
    def fund_transfer(self,user,to_acc,amnt):
        if self.validate_account(to_acc):
            balance=self.users[user]["balance"]
            if balance<amnt:
                print("Insufficient balance")
            else:
                self.users[user]["balance"]-=amnt
                self.users[to_acc]["balance"]+=amnt

obj = Bank()
user=obj.authenticate(accno=1000, password="user1")
obj.balance_enquiry(user)
obj.fund_transfer(1000,1002,2000)
obj.balance_enquiry(1000)
user=obj.authenticate(accno=1002,password="user2")
obj.balance_enquiry(user)

# obj2=Bank()
# user=obj.authenticate(accno=1001, password="user3")
# if (user==-1) | (user==0):
#     print("Authentication Failed")
# else:
#     obj2.balance_enquiry(user)

