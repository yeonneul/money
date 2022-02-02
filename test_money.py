from class_money import Money
from exchange_rate import get_exchanged_rate

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
        assert wallet.evaluate('USD') 

    def test_evaluate_different_currency2(self):
        one_usd = Money(1,'USD')
        one_thou_krw = Money(1000,'KRW')
        wallet = Wallet()
        wallet.adds(one_usd, one_thou_krw)
        assert wallet.evaluate('KRW')



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
    assert expected 

def convert(money,currency):
    if currency == money.currency:
        return money
    else:
        exchange_rate = get_exchanged_rate(money.currency, currency)
        return Money(money.amount * exchange_rate, currency)

def test_evaluate_cifferent_currency(): 
    one_usd = Money(1,'USD')
    one_yan = Money(1,'JPY')
    wallet = Wallet()
    wallet.adds(one_usd, one_yan)
    assert wallet.evaluate('JPY')

