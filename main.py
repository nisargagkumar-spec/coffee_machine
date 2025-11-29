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

print("Welcome to the Coffee Cafe!")
while True:
    user_coffee = input("What would you like? (espresso/latte/cappuccino):")
    if user_coffee=="espresso":
        print(f"Here is your {user_coffee}")
    elif user_coffee=="latte":
        print(f"Here is your {user_coffee}")
    elif user_coffee=="cappucino":
        print(f"Here is your {user_coffee}")
    elif user_coffee=="report":
        print(f"Here is your {resources}")
    elif user_coffee=="off":
        print("Machine shut down")
    else:
        print("Select from the above 3 coffess only!")

    def make_coffee(user_choice):
        per_coffee = MENU[user_coffee]["ingredients"]
        for items in per_coffee:
            cost_per_coffee = MENU[user_coffee]["cost"]
            required_resources = per_coffee[items]
            print(items,"-",required_resources)
        print(f"Your cost for the {user_choice} is:{cost_per_coffee}")

    make_coffee(user_coffee)
