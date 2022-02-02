class Money:
    def __init__(self,amount, currency):
        self.amount = amount
        self.currency = currency
    
    def divide(self, divider):
        return Money(self.amount / divider, self.currency)

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency 

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
   
    def __repr__(self):
       return f'<{self.currency} {self.amount}>'