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
    "money": 0,
}

coins_in_machine = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

money_inserted = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

coins_map = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def request_payment():
    print("Please insert coins.")
    for coin_type in money_inserted:
        money_inserted[coin_type] = int(input(f"how many {coin_type}?: "))


def calculate_inserted_money():
    total_money_inserted = 0

    for coin in money_inserted:
        total_money_inserted += coins_map[coin] * money_inserted[coin]

    return total_money_inserted


def check_payment(beverage):
    beverage_cost = MENU[beverage]["cost"]

    if beverage_cost > calculate_inserted_money():
        return False
    else:
        return True


def check_resources(beverage):
    for resource in resources:
        if resource in MENU[beverage]["ingredients"] and resources[resource] < MENU[beverage]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            return False

    return True


def prepare_beverage(beverage):
    for ingredient in MENU[beverage]["ingredients"]:
        resources[ingredient] -= MENU[beverage]["ingredients"][ingredient]
    print(f"Here is your {beverage} ☕️. Enjoy!")


def update_money(beverage):
    resources["money"] += MENU[beverage]["cost"]
    change = round(calculate_inserted_money() - MENU[beverage]["cost"], 2)
    print(f"Here is ${change} in change.")

    for coin in coins_in_machine:
        coins_in_machine[coin] += money_inserted[coin]
        money_inserted[coin] = 0
    return


def process_order(ordered_beverage):

    if ordered_beverage == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        request_payment()

        if check_payment(ordered_beverage):
            if check_resources(ordered_beverage):
                update_money(ordered_beverage)
                prepare_beverage(ordered_beverage)
            else:
                return
        else:
            print("Sorry that's not enough money. Money refunded.")


client_order = ""

while client_order != "off":

    client_order = input("What would you like? (espresso / latte / cappuccino): ")
    if client_order != "off":
        process_order(client_order)

# TODO: 1. Comment code appropriately.
# TODO: 2. Clean up if needed.
# TODO: 3. Expand the machine to work with coins, instead of only total amounts.

