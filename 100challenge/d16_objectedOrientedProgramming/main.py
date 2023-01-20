#d16_objectedOrientedProgramming
"""
import another_module

print(another_module.another_variable, type(another_module.another_variable))

from turtle import Turtle, Screen


tommy = Turtle()
print(tommy)

tommy.shape('turtle')
tommy.color('aquamarine')
tommy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)

"""

#print report
#check resources sufficient
#process coins
#check transaction successful
#make coffee

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

still_works = True

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

while still_works == True:
    options = menu.get_items()
    action = input(f"What would you like? {options}: ").lower()
    if action == "report":
        money_machine.report()
        coffe_maker.report()
    elif action == "off":
        still_works = False
    else:
        drink = menu.find_drink(action)
        print(drink)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

