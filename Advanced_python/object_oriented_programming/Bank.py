class Bank:
    bname="State Bank of Travancore"             # Static variable.......defined inside a class
    def accountCreation(self,name,accno,branch):
        self.name=name
        self.accno=accno
        self.branch=branch
        self.minimumbal=5000
        self.balance=self.minimumbal
        print("Congratulations.Your account is created successfully.")
        print("Name: ",self.name)
        print("Account no: ",self.accno)
        print("Branch: ",self.branch)
        print("Bank name: ",Bank.bname)
    def deposit(self,d_amnt):
        self.d_amnt=d_amnt
        self.balance+=self.d_amnt
        print("Your",self.bname," account is credited with Rs.",d_amnt)
        print("Your current balance is Rs.",self.balance)
    def withdraw(self,w_amnt):
        self.w_amnt=w_amnt
        if self.w_amnt>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=self.w_amnt
            print("Rs.",self.w_amnt," is debited from your account.")
            print("Your current balance is Rs.",self.balance)
bank=Bank()
count=0        # to count the no. of times an account is created
next=0
while next!=4:
    ch=int(input("Select an operation:1.accountCreation 2.deposit 3.withdraw "))
    if ch==1 and count!=0:
        print("You already have an account with this bank")
    elif ch==1:
        name=input("Enter your name ")
        accno=input("Enter your account number ")
        branch=input("Enter your bank branch ")
        bank.accountCreation(name,accno,branch)
        count+=1
    elif ch==2:
        d_amnt=int(input("Enter the amount you want to deposit "))
        bank.deposit(d_amnt)
    elif ch==3:
        w_amnt=int(input("Enter the amount you want to withdraw "))
        bank.withdraw(w_amnt)
    else:
        print("Please select a valid choice")
    next=int(input("Do you want to continue? Press 4 to exit "))