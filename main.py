from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from process_coins import MoneyMachine
is_on=True
money=MoneyMachine()
coffee=CoffeeMaker()
# coffee.report()
# money.report()
men=Menu()
# p=men.get_items()
# order=input(p)
# p1=men.find_drink(order)
while  is_on:
   options=men.get_items()
   choice=input(f"what would you like ({options})")
   if choice=='off':
       is_on=False
   elif choice=='report':
       coffee.report()
       money.report()
   else:
       drink=men.find_drink(choice)
       print(drink)
       if coffee.is_resource_sufficient(drink) and  money.make_payment(drink.cost):
               coffee.make_coffee(drink)