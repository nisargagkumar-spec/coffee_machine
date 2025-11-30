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
    "money":0,

}

print("Welcome to the Coffee Cafe!")
while True:
    user_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_coffee=="off":
        print("System shut down")
        break
    elif user_coffee=="report":
        for items in resources:
            machine_resources=resources[items]
            print(items,machine_resources)

    elif user_coffee not in MENU:
        try:
            print("Check for the coffee flavors mentioned above again!")
        except KeyError:
            user_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    else:
        def check_ingredients():
            per_coffee = MENU[user_coffee]["ingredients"]
            # Step 1: check if all ingredients are sufficient
            can_make = True  # assume we can make the coffee
            for coffee_items in per_coffee:
                required_amount = per_coffee[coffee_items]
                available_amount = resources[coffee_items]
                if required_amount > available_amount:
                    can_make = False  # if any ingredient is insufficient
                    break  # no need to check further
            # Step 2: subtract resources if coffee can be made
            if can_make:
                for coffee_items in per_coffee:
                    required_amount = per_coffee[coffee_items]
                    resources[coffee_items] -= required_amount

                def process_coins(user_choice):
                    cost_per_coffee = MENU[user_coffee]["cost"]
                    print(f"Your cost for the {user_choice} is:{cost_per_coffee}")
                    quarters = float(input("How many quarters??"))
                    dimes = float(input("How many dimes?"))
                    nickles = float(input("How many nickles"))
                    pennies = float(input("How many pennies"))
                    total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                    if total_money == cost_per_coffee:
                        print(f"Here is your {user_coffee}")
                    elif total_money > cost_per_coffee:
                        refund_money = round(total_money - cost_per_coffee, 2)
                        print(f"Here is your {user_coffee}")
                        print(f"Here is your dollars in change $ {refund_money}")
                    else:
                        print(f"The money is not sufficent and the cost of {user_coffee} is {cost_per_coffee}")
                    resources["money"]=resources["money"]+cost_per_coffee
                process_coins(user_coffee)
            else:
                print(f"Your coffee cannot be made as {coffee_items} is insufficent")
        check_ingredients()