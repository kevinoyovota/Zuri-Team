class Budget:
    def __init__(self, category, balance = 0.00):
        self.category = category
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited %.2f Naira in '%s' budget.\n" % (amount, self.category))
        return

    def withdraw(self, amount = 0.00):
        if(self.balance >= amount):
            self.balance -= amount
            print("You have withdrawn %.2f Naira from '%s' budget.\n" % (amount, self.category))
        else:
            print("You do not have sufficient funds in '%s' for this withdrawal.\n" % self.category)
        return

    def checkBalance(self):
        print("You have %.2f Naira in '%s' budget.\n" % (self.balance, self.category))
        return

    def transfer(self, budgetName, amount):
        if(isinstance(budgetName, Budget)):
            budgetName.balance += amount
            self.balance -= amount
            print("You have transferred %.2f from '%s' to '%s'.\n" % (amount, self.category, budgetName.category))
        else:
            print("Nonexistent budget.\n")


########################################################################################


food = Budget('Food', 5000.00) #Instantiate 'food' object

clothing = Budget('Clothes', 45000.00) #Instantiate 'clothing' object

entertainment = Budget("Entertainment") #instantiate 'entertainment' object

utilities = Budget('utilities') #Instantiate 'utilities' budget


########################################################################################


entertainment.deposit(12000) #Deposit 12000 Naira for entertainment

food.withdraw(2000) #Withdraw 2000 Naira for food

clothing.transfer(food, 10000) #Clearly, there is not enough funds in the food budget, so transfer 10000 from the clothes budget

entertainment.withdraw(1500) #Now I want to see a movie. The ticket costs 1500 Naira

utilities.withdraw(10000) #But first, let me pay my PHCN bill.

#Finally, let's see how much I have left in each budget
food.checkBalance()
clothing.checkBalance()
entertainment.checkBalance()
utilities.checkBalance()

#Side note: It turns out that I didn't deposit any money in the utilities object. So...
