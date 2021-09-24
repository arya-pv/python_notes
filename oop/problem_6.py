class Bank:
    bname="SBI"
    def acCreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amt):
        self.amt=amt
        self.balance=self.balance+self.amt
        print("your",Bank.bname,"account has been credited with amt",self.balance)
    def withdrawl(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insufficient balace")
        else:
            print("account debited with",self.amount)
            self.balance=self.balance-self.amount
            print("available balance",self.balance)

obj=Bank()
num=int(input("enter account no"))
obj.acCreate(num,"abc")
obj.deposit(25000)
obj.withdrawl(1000)

