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
    if user_coffee=="report":
        for items in resources:
            res=resources[items]
            print(f"{items}-{res}")
    elif user_coffee=="off":
        print("Machine shut down")
        break
    else:
        per_coffee = MENU[user_coffee]["ingredients"]
        for items in per_coffee:
            required_resources = per_coffee[items]
            print(items, "-", required_resources)

        def makecoffee(user_choice):
            cost_per_coffee = MENU[user_coffee]["cost"]
            print(f"Your cost for the {user_choice} is:{cost_per_coffee}")
            quarters=float(input("How many quaters??"))
            dimes=float(input("How many dimes?"))
            nickles=float(input("How many nickles"))
            pennies=float(input("How many pennies"))
            total_money=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
            if total_money==cost_per_coffee:
                print(f"Here is your {user_coffee}")
            elif total_money>cost_per_coffee:
                refund_money=round(total_money-cost_per_coffee,2)
                print((f"Here is your {user_coffee} and the change of {refund_money}"))
            else:
                print(f"The money is not sufficent and the cost of {user_coffee} is {cost_per_coffee}")

        makecoffee(user_coffee)
