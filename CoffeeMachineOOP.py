from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
MoneyMachine = MoneyMachine()
menu = Menu()

coffee_maker.report()
MoneyMachine.report()

is_on = True
while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  if menu.find_drink(choice):
    MoneyMachine.process_coins()
    MoneyMachine.make_payment(menu.find_drink(choice).cost)

  is_on = False