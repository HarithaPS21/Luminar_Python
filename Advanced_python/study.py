# list all product details below 250

# products=[
#     {"item_name":"boost","mrp":290,"stock":50},
#     {"item_name":"complan","mrp":240,"stock":10},
#     {"item_name":"bournvita","mrp":320,"stock":20},
#     {"item_name":"horlicks","mrp":280,"stock":13},
#     {"item_name":"nutricharge","mrp":275,"stock":0},
# ]
# details=list(filter(lambda product:product["mrp"]<250,products))
# print(details)


# def details():
#     for product in products:
#         if product["mrp"]<250:
#             print(product)
# details()
#..........................................................................
#
# lst=[2,3,4,8,10,7]
# new_lst=list(map(lambda num:num-1 if num<5 else num+1,lst))
# print(new_lst)

# new_lst=[]
# def new_list():
#     for num in lst:
#         if num<5:
#             new_lst.append(num-1)
#         else:
#             new_lst.append(num+1)
#     print(new_lst)
# new_list()
#................................................

# num1=10
# num2=20
# res=num1 if num1>num2 else num2
# print(res)
#............................................................
# num1=-10
# res="positive" if num1>0 else "negative"
# print(res)

# if num1>0:
#     print("positive")
# else:
#     print("negative")
#...........................................................................

# num=7
# odd="odd" if num%2!=0 else "even"
# print(odd)

# def odd(num):
#     if num%2!=0:
#         return "odd"
#     else:
#         return "even"
# print(odd(num))
#.............................................................

# check prime
# def prime(num):
#     flag=1
#     for i in range(2,num):
#         if num%i==0:
#             flag=0
#             break
#     if flag==1:
#         return True
# lst=[12,13,14,15,17]
# prime=list(filter(prime,lst))
# print(prime)
#...............................................................

# lst=[1,2,3,4,5,6,7]
# total=sum(lst)
# print(total)

# Reduce
# from functools import reduce
# lst=[1,2,3,4,5,6,7]
# total=reduce(lambda num1,num2:num1+num2,lst)
# print(total)
#.........................................................

# from functools import reduce
# lst=[1,2,3,4,5,6,7]
# max=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(max)
#............................................................

# highest cost
from functools import reduce
# products=[
#     {"item_name":"boost","mrp":290,"stock":50},
#     {"item_name":"complan","mrp":240,"stock":10},
#     {"item_name":"bournvita","mrp":320,"stock":20},
#     {"item_name":"horlicks","mrp":280,"stock":13},
#     {"item_name":"nutricharge","mrp":275,"stock":0},
# ]
# # high_cost=reduce(lambda p1,p2:p1["mrp"] if p1["mrp"]>p2["mrp"] else p2["mrp"],products) # error........int obj not subscriptable

# prices=list(map(lambda product:product["mrp"],products))
# high_cost=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
# print(high_cost)
#...................................................................................

# lst=[0,2,3,4,5,8,10,7]
# new_lst=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
# print(new_lst)
#.......................................................................................

# Decorators

# def decorator_sub(func): # sub(2,10)
#     def wrapper(num1,num2): # (2,10)
#         if num1<num2: # 2<10
#             num1,num2=num2,num1
#         return func(num1,num2) # func(10,2)
#     return wrapper
# @decorator_sub
# def sub(num1,num2):
#     return num1-num2  # 10-2=8
# print(sub(2,10))
#............................................................................

# division
# def zeronotrequired(func):
#     def wrapper(num1,num2):
#         if (num1==0) | (num2==0):
#             raise Exception("cannot divide by zero")
#         return func(num1,num2)
#     return wrapper
# def decorator_div(func):
#     def wrapper(num1,num2):
#         if num1<num2:
#             (num1,num2)=(num2,num1)
#         return func(num1,num2)
#     return wrapper
# @zeronotrequired
# @decorator_div
# def div(num1,num2):
#     return num1/num2
# try:
#     print(div(1,0))
# except Exception as e:
#     print(e)
#...............................................................................
# def authenticate(func):
#     def wrapper(user,pin):
#         if user!="admin":
#             print("You are not authorised to change pin")
#         else:
#             return func(user,pin)
#     return wrapper
# @authenticate
# def change_pin(user,pin):
#     new_pin=int(input("enter your new_pin: "))
#     return new_pin
# @authenticate
# def delete_account(user,accno):
#     return str(accno)+'deleted'
#
# print(change_pin("admin", 123))
# print(delete_account("admin",1233454))
#..............................................

users = {
    1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}
# check if 1000 exists or not,if yes print balance of 1000
def authenticate(**kwargs):
    accno=kwargs["accno"]
    password=kwargs["password"]
    if accno in users:
        if password==users[accno]["password"]:
            print("Login success")
        else:
            print("Failed to login")
    else:
        print("Invalid user")
def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("invalid account no.")
authenticate(accno=1000,password="user1")
get_balance(1000)
get_balance(1002)
#.........................................................................


class Bank:
    users = {
        1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
        1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
        1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
        1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
    }
    def validate_account(self,accno):
        if accno in self.users:
            return True
        else:
            return False

    def authenticate(self,**kwargs):
        accno=kwargs["accno"]
        password=kwargs.get("password")
        # if accno in users:
        #     if password==users[accno]["password"]:
        if self.validate_account(accno):
            if password==self.users[accno]["password"]:
                print("Logged in successfully")
            else:
                print("Login Failed")
        else:
            print("invalid user")

    def balance_enquiry(self,accno):
        if self.validate_account(accno):
           balance=self.users[accno]["balance"]
           print("Your current balance is Rs.",balance)
    def fund_transfer(self,accno,to_acc,amnt):
        if





