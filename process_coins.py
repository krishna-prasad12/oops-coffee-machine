class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit=0
        self.money_received=0

    def report(self):
        print(f' profit:${self.profit}')


    def process_coins(self):
        for item in self.COIN_VALUES:
            self.money_received+=float(input(f'enter the amount of {item}'))*self.COIN_VALUES[item]
        return self.money_received


    def make_payment(self,cost):
        self.process_coins()
        if self.money_received>cost:
            change=self.money_received-cost
            print(f'Take the change :{change}')
            self.profit+=cost
            self.money_received=0
            return True
        else:
            print('There is not enough money')
            self.money_received=0
            return False

