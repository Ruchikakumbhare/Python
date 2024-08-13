# PROGRAM1:

class bank :
    def __init__(self,fn,Accno,bal):
        self.fullname = fn
        self.Accountno = Accno
        self.balance = bal
        self.transaction = []
        
    def deposit(self,amt):
        self.balance = self.balance - amt
        self.transaction.append(amt)
        return self.balance
    
    def withdrwal(self,amt):
        if(amt<self.balance):
            self.balance = self.balance - amt
            self.transaction.append(-amt)
            return self.balance
        else:
            print("Insufficient balance :"+str(self.balance))

    def lastfivetrans(self):
          return self.transaction[-5::]
        
    

ruchi = bank('Ruchika Kumbhare',1234,8000)
ruchi.deposit(1000)
ruchi.withdrwal(500)
ruchi.withdrwal(500)
ruchi.withdrwal(1000)
ruchi.deposit(2000)
ruchi.withdrwal(5000)
print(ruchi.transaction)
print(ruchi.lastfivetrans())
print(ruchi.transaction)