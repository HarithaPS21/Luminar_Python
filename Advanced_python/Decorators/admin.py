def admin_required(func):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("You are not authorised to change pin")
        else:
            return func(user,pin)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_acc(user,accno):
    return str(accno)+" deleted"

print(change_pin("admin",32617859))
print(delete_acc("admin",23768238229))

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