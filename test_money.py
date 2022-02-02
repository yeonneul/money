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

    def test_evaluate_different_currency2(self):
        one_usd = Money(1,'USD')
        one_thou_krw = Money(1000,'KRW')
        wallet = Wallet()
        wallet.adds(one_usd, one_thou_krw)
        assert wallet.evaluate('KRW') == Money(2100,'KRW')



class Wallet:
    def __init__(self):
        self.moneys = []
        
    def adds(self, *moneys):
        for money in moneys:
            self.moneys.append(money)

    def evaluate(self, currency):
        money_sum = 0
        for money in self.moneys:
            if currency == money.currency:
                money_sum += money.amount
            else:
                converted_money = convert(money,currency)
                money_sum +=converted_money.amount
        return Money(money_sum, currency)

    

def test_convert():
    one_euro = Money(5,'EUR')
    expected = Money(6,'USD')
    actual = convert(one_euro,'USD')
    assert expected == actual

def convert(money,currency):
    exchange_rates = {'EUR->USD':1.2, 'USD->KRW':1100}
    if currency == money.currency:
        return money
    else:
        exchange_key = f'{money.currency}->{currency}'
        exchange_rate = exchange_rates[exchange_key]
        return Money(money.amount * exchange_rate, currency)

    pass




#def test_wallet_extraction(self):
 #   ten_dollar = Money(10,'USD')
  #  wallet = Wallet()
   # wallet.adds(ten_dollar)
    #wallet.extract(5,'USD')
     #assert wallet.evaluate('USD') == 5 