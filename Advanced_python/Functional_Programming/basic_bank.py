
users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}
# accno=int(input("Enter account no."))
# password=input("Enter password ")
def authenticate(accno,password):
    if accno in users:
        if password==users[accno]["password"]:
         print("Login Success")
        else:
            print("Login Failed")
    else:
         print("invalid account no")

def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])

authenticate(1000,"user1")     # make it more readable.........use **args
get_balance(1000)
get_balance(1002)   # the loggedin user can get details of any other user......security issues