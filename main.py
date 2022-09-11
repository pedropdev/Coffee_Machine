from menu import MENU
from menu import resources
not_OFF = True
CASH = 0


while not_OFF:
    # checks for milk in drink
    GOT_MILK = 0
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    coffee = input('"What would you like?"(espresso/latte/cappuccino):').lower()
    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if coffee == "off":
        not_OFF = False
    # TODO: 3. Print report.
    elif coffee == "report":
        print(f"Water: {resources['water']} ml \n"
              f"Milk: {resources['milk']} ml \n"
              f"Coffee: {resources['coffee']} ml \n"
              f"Money: {CASH} $")


    def coffee_selection(drink):
        """Selects 1 of 3 options: (Espresso/Latte/Cappuccino)"""
        global GOT_MILK
        if coffee == "latte" or coffee == "cappuccino":
            GOT_MILK = 1
        if coffee != "off" and coffee != "report":
            selected_drink = MENU[drink]
            return selected_drink


    # TODO: 4. Check resources sufficient?


    def resource_checker(drink, contents):
        """Checks inventory for available ingredients and returns 0 if not enough and 1 if enough for selected drink."""

        if drink["ingredients"]["water"] >= contents["water"]:
            return 1
        elif GOT_MILK and drink["ingredients"]["milk"] >= contents["milk"]:
            return 2
        elif drink["ingredients"]["coffee"] >= contents["coffee"]:
            return 3
        else:
            return 4


    # TODO: 5. Process coins.


    def coin_processor():
        """Processes coins for payment."""

        print("Please insert coins.\n")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        payment = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
        return payment


    # TODO: 6. Check transaction successful?


    def transaction_check(amount):
        """Checks whether if a transaction was successful or not. Provides change if needed."""
        global CASH
        if amount == drink_of_choice["cost"]:
            CASH += amount
            print(f"Here is your {coffee}. ☕ Enjoy!")
        elif amount > drink_of_choice["cost"]:
            # Overpayment scenario
            CASH += amount
            difference = amount - drink_of_choice["cost"]
            print(f"Here is your change: {round(difference,2)} $")
            print(f"Here is your {coffee}. ☕ Enjoy!")
        else:
            print(f"Sorry not enough coins. Here is your {amount} $")


    if coffee != "off" and coffee != "report":
        drink_of_choice = coffee_selection(coffee)
        check = resource_checker(drink_of_choice, resources)
        if check == 4:
            transaction_check(coin_processor())
            # TODO: 7. Make Coffee.
            resources["water"] -= drink_of_choice["ingredients"]["water"]
            if GOT_MILK:
                resources["milk"] -= drink_of_choice["ingredients"]["milk"]
            resources["coffee"] -= drink_of_choice["ingredients"]["coffee"]
        elif check == 3:
            print("Sorry,there is not enough  coffee")
        elif check == 2:
            print("Sorry,there is not enough  milk")
        elif check == 1:
            print("Sorry,there is not enough water")
