from money import Money

class Bank:

    def __init__(self):
        self.exchange_rates = {}
    
    def add_exchange_rate(self, currency_from, currency_to, rate):
        key = currency_from + "->" + currency_to
        self.exchange_rates[key] = rate
    
    def convert(self, actual_money,actual_currency):
        if actual_currency == actual_money.currency:
            return Money(actual_money.amount, actual_currency)
        key = actual_money.currency + "->" + actual_currency
        if key in self.exchange_rates:
            return Money(actual_money.amount * self.exchange_rates[key], actual_currency)
        
        raise Exception(key)