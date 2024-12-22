from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Power = True
m1 = Menu()
Maker = CoffeeMaker()
money_counter = MoneyMachine()
while(Power):
    print("What would you like? ",m1.get_items())
    str = input()
    if str == "off":
        Power = False
    elif str == "report":
        Maker.report()
        money_counter.report()
    else:
        drink = m1.find_drink(str)
        if not drink:
            print("Wrong item ordered")
            continue
        if Maker.is_resource_sufficient(drink):
            if money_counter.make_payment(drink.cost):
                Maker.make_coffee(drink)

print("Coffee Machine Powered off")