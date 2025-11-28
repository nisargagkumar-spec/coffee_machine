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
        print("espresso")
    elif user_coffee=="latte":
        print("latte")
    elif user_coffee=="cappuccino":
        print("cappuccino")
    elif user_coffee=="report":
        for keys in resources:
            print(keys,resources[keys])
    elif user_coffee=="off":
        break
    else:
        print("Choose from the above 3 options only.")


