class ShoppingListOrganizer:
    #constructor will be initialized with empty default values
    def __init__(self):
        self.items = []
        self.catagories = {}
        self.totalCost = 0
        self.budget = 0
        
    #accept the input from the budgetSetter function and assign it to the constructor field
    def setBudget(self, budget):
        self.budget = budget

    
    # the user will be asked to enter every detail about the procut, and adds the product to his/her shopping list 
    def addItems(self):
        try:
            name = input('enter the name of the product you want to add: ').strip()
            catagory = input("enter the catagory of the product: ").strip()

            quantity = int(input("enter the quantity: ").strip())
            price = int(input("enter the price of the product: ").strip())
            purchased = False
            self.items.append([name, catagory, quantity, price, purchased])
            if catagory in self.catagories.keys():
                self.catagories[catagory] += 1
            else:
                self.catagories[catagory] = 1

            print('item added successfully!')
        except:
            print("invalid input")
    
    # when the user want to check the price of a specific product from his entire shopping list
    # this function will print the price if the item is in the shopping list, unless it will print that the item is not listed
    def checkPrice(self, product):
        for item in self.items:
            if item[0] == product:
                print(f'price = {item[3]}')
                return
        print('there is no such product in your list')

    # if the user added some product and changed his idea he can just simply remove it, and we provide that functionality here
    def removeItem(self):
        itemName = input("enter the name of the product you want to remove: ").strip()
        for i in range(len(self.items)):
            if self.items[i][0] == itemName:
                if self.items[i][4] == True:
                    self.budget += self.items[i][3] * self.items[i][2]
                    self.totalCost -= self.items[i][3] * self.items[i][2]
                    print(f'total budget: {self.budget}')
                    print(f'self.totalCost: {self.totalCost}')
                self.catagories[self.items[i][1]] -= 1
                self.items.pop(i)
                print('item removed successfully')
                return
        print("there is no such product in your cart to remove")


    
    # when the user wants to see the items he listed for shopping, our program will organize the items in their catagory
    def viewInCatagory(self):
        printed = False
        for catagory in self.catagories.keys():
            if self.catagories[catagory] >= 1:
                print(catagory)
                for item in self.items:
                    if item[1] == catagory:
                        print(f'\nproduct name: {item[0]}')
                        print(f'price: {item[3]}')
                        print(f'quantity: {item[2]}')
                        print(f'purchased: {item[4]}')
                        printed = True
                print('|___________________________|\n')
        if printed:
            return
        print('there is no item in your list')

    # when the user wants to check if he listed a specific product or not he can search for that specific product
    # the function accepts the name of the product and iterate through the entire list and return the product details if the item is listed
    def searchItem(self, product):
        for item in self.items:
            if item[0] == product:
                print('the product is listed')
                print(f'product name: {item[0]}')
                print(f'price: {item[3]}')
                print(f'quantity available: {item[2]}')
                print(f'purchased: {item[4]}')
                return
        print("you didn't list that item")
        
    # every time the user try to  purchase some product we should check if the budget is enough to buy that product with the specified amout/quantity
    def budgetChecker(self, price):
        if self.budget < price:
            return False
        return True

    # we check if the user already bought that product or not
    #if  he already bought that product no need of buying the same product again
    def checkPurchased(self, product):
        for item in self.items:
            if item[0] == product:
                if item[4] == True:
                    return True
                return False

    #every time the user performs a transaction the remaining budget will decrease, so will update the budget
    # the total cost will increase everytime the user buys a product
    def calculateExpenditure(self, price):
        if self.budgetChecker(price):
            self.budget -= price
            self.totalCost += price
            return
        return False
    # when the user try to purchase some product, we first check wheather or not he/she bought that product
    # then if there is enough budget we will mark the product purchased and we will calculate the remaining budget and total cost
    def purchaseItem(self):
        item_to_be_purchased = input("Enter the name of the product you want to purchase: ").strip()

        for item in self.items:
            if item[0] == item_to_be_purchased:
                if  self.checkPurchased(item_to_be_purchased):
                    print('the item is already purchased!')
                    return
                if self.budgetChecker(item[3] * item[2]):
                    item[4] = True
                    print("purchased successfully!!")
                    self.calculateExpenditure(item[3] * item[2])
                    print(f'remaining budget: {self.budget}')
                    print(f'total cost: {self.totalCost}')
                    return
                print("you don't have enough money to buy the product!")
                return
        print("there is no product in your list with this name!")


#our shoppingList class instance
myShoppingListOrganizer = ShoppingListOrganizer()

# budget setter function, will prompt user until they enter appropriate value
def budgetSetter():
    while True:
        try:
            budget = int(input('enter your total budget for shopping: ').strip())
            #we will update our constructor with the new budget
            myShoppingListOrganizer.setBudget(budget)
            return budget
        except:
            print('invalid input')


budget = budgetSetter()
print(
    'add --> to add an item\nsearch --> to search an item in our cart\nprice --> to check price of a product\nremove --> to remove\nview --> to view items in their catagorie\npurchase --> to purchase an item\nreset-->to reset    \nquit --> to quit ')

#this loops give the user infinite transaction
#will break when the user enter the command 'quit'
while True:

    command = input("Enter your command: ").strip()
    if command.lower() == 'add':
        myShoppingListOrganizer.addItems()
        continue
    if command.lower() == 'price':
        name = input('enter the name of the product: ').strip()
        myShoppingListOrganizer.checkPrice(name)
        continue
    if command.lower() == 'remove':
        myShoppingListOrganizer.removeItem()
        continue
    if command.lower() == 'view':
        myShoppingListOrganizer.viewInCatagory()
        continue
    if command.lower() == 'purchase':
        myShoppingListOrganizer.purchaseItem()
        continue
    if command.lower() == 'reset':
        myShoppingListOrganizer = ShoppingListOrganizer()
        budgetSetter()
        continue
    if command.lower() == 'search':
        name = input('enter the name of the product you want to search: ').strip()
        myShoppingListOrganizer.searchItem(name)
        continue
    if command.lower() == 'quit':

        break
    else:
        print(
            'add --> to add an item\nsearch --> to search an item in our cart\nprice --> to check price of a product\nremove --> to remove\nview --> to view items in their catagorie\npurchase --> to purchase an item\nreset-->to reset    \nquit --> to quit ')

        continue

