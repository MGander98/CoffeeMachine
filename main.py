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
    "coffee": 100
}


def sufficient_resources(order_ingredients):
    """Returns True if there is enough reources to make their drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry can't make your drink, not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total amount of money input against the required amount and provides any change."""
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.10
    total += int(input("How many nickels?:")) * 0.05
    total += int(input("How many cents?:")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Checks if the money inputted is enough to pay for the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you don't have enough for the drink. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    """Deduct the resources for each ingredient used."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Please enjoy {drink_name}. Have a nice day.")


is_on = True

while is_on:
    user = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if user == "off":
        is_on = False
    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_drink(user, drink["ingredients"])

