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

    def test_different_currency(self):
        five_dollar = Money(5,'USD')
        ten_euro = Money(10, 'EUR')
        wallet = Wallet()
        wallet.adds(five_dollar, ten_euro)
        assert wallet.evaluate('USD') == Money(17,'USD')



class Wallet:
    def __init__(self):
        self.moneys = []
        self.euro_to_usd = 1.2
        self.exchange_rate = {'USD->KWN':1100,'EUR->USD':1.2}
        
    def adds(self, *moneys):
        for money in moneys:
            self.moneys.append(money)

    #def extract(self, amount, currency):
    #    self.amount -= amount

    def evaluate(self, currency):
        money_sum = 0
        for money in self.moneys:
            if currency == money.currency:
                money_sum += money.amount
            else:
                exchange_key = f'{money.currency}->{currency}'
                exchange_rate = self.exchange_rate[exchange_key]
                money_sum += money.amount * exchange_rate
        return Money(money_sum, currency)






#def test_wallet_extraction(self):
 #   ten_dollar = Money(10,'USD')
  #  wallet = Wallet()
   # wallet.adds(ten_dollar)
    #wallet.extract(5,'USD')
     #assert wallet.evaluate('USD') == 5 