from class_money import Money

class TestMoney:
    def test_multiplication(self):
        five_dollar = Money(5, 'USD')
        assert five_dollar * 2 == Money(10,'USD')
    
    def test_division(self):
        won_4000000 = Money(4000000, 'WON')
        won_4000 = won_4000000.divide(1000)
        assert won_4000 == Money(4000,'WON')

class TestWallet:
    def test_addition(self):
        one_dollar = Money(1, 'USD')
        two_dollae = Money(2, 'USD')
        three_dollar = Money(3, 'USD')
        assert one_dollar + two_dollae == three_dollar


class Wallet:
    def __init__(self):
        self.moneys = []
        self.amount = 0
        
    def adds(self, *moneys):
        for money in moneys:
            self.moneys.append(money)
            self.amount += money.amount

    #def extract(self, amount, currency):
    #    self.amount -= amount

    def evaluate(self, moneys):
        for money in moneys:
            self.moneys.append(money)





#def test_wallet_extraction(self):
 #   ten_dollar = Money(10,'USD')
  #  wallet = Wallet()
   # wallet.adds(ten_dollar)
    #wallet.extract(5,'USD')
     #assert wallet.evaluate('USD') == 5    