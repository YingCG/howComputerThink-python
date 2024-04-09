class Checkout:
   def __init__(self):
       self.products = {}
    
   def addItemPrice(self, item, price):
        self.products[item] = price
            
   def addItem(self, item):
        self.item = item

   def calculateTotal(self):
        total = sum(self.products.values())
        return total