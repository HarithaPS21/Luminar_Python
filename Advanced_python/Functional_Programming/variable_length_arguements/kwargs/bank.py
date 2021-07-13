users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}
def authenticate(**kwags):# kwags={}
    user=kwags["accno"]
    password=kwags["password"]
    if user in users:
        if password==users[user]["password"]:
            print("success")
        else:
            print("failed")
    else:
        print("invalid account no.")
def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("invalid account no.")
authenticate(accno=1000,password="user2")
get_balance(1000)    # this user can get details of other users.......security issue...make changes in get_balance() function