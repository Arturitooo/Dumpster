#d15_coffeeMachine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
paid_sum = 0
action = 'off'

def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money:",money)

def check_resources(coffee):
    if coffee == "espresso":
        if resources["water"] >= MENU[coffee]['ingredients']['water'] and resources["coffee"] >= MENU[coffee]['ingredients']['coffee']:
            return True      
        else:
            print(f"Sorry, we don't heve enough resources. We can't prepare you the {action}.")
            return False
    else:
        if resources["water"] >= MENU[coffee]['ingredients']['water'] and resources["milk"] >= MENU[coffee]['ingredients']['milk'] and resources["coffee"] >= MENU[coffee]['ingredients']['coffee']:
            return True
        else:
            print(f"Sorry, we don't heve enough resources. We can't prepare you the {action}.")
            return False   

def process_coins(gotResources):
    if gotResources == True:
        print("Please insert your coins")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        paid_sum = round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01),2)
        return paid_sum

def check_transaction(ClientPaid):
        print(f"here's how much you paid {ClientPaid}")
        moneyBack = ClientPaid - MENU[action]['cost']
        moneyBack = round(moneyBack,2)
        print(f"Here's ${moneyBack} in change")
        global money
        money = money + ClientPaid - moneyBack
        money = round(money,2)
        return

def make_coffee(coffee):
    if coffee == "espresso":
        print(f"Here's your {coffee}")
        for resource in MENU[coffee]['ingredients']:
            resources[resource] = resources[resource] - MENU[coffee]['ingredients'][resource]
    elif coffee == "latte":
        print(f"Here's your {coffee}")
        for resource in MENU[coffee]['ingredients']:
            resources[resource] = resources[resource] - MENU[coffee]['ingredients'][resource]
    elif coffee == "cappuccino":
        print(f"Here's your {coffee}") 
        for resource in MENU[coffee]['ingredients']:
            resources[resource] = resources[resource] - MENU[coffee]['ingredients'][resource]
    return resources


while action == 'off' or action == 'latte' or action == 'cappuccino' or action == 'espresso' or action == 'report':
    action = input("What would you like? (espresso/latte/cappucino): ").lower()
    if action == "report":
        report()
    elif action == "off":
        quit()
    else:
        haveResources = check_resources(action)
        if haveResources == True:
            check_transaction(process_coins(haveResources))
            print(f"Here are the resources left: {make_coffee(action)} \n")