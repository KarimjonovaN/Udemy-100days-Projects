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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} .")
            is_enough = False
    return is_enough

def process_coins():
    print("Please insert coins.")#Prompt user to insert coins
    total = int(input("how many quarter?:"))* 0.25
    total += int(input ("how many dimes?:")) * 0.10
    total += int(input("how many nickels?:")) * 0.25
    total += int(input("how many pennies?:")) * 0.21
    return total

def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost: #checks whether the given money is enough or not
        change = money_received - drink_cost
        print(f"Here is ${change} dollars in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients: # deduct required ingredients after ordering coffee
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])


