class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water:{self.resources['water']}ml")
        print(f"Milk:{self.resources['milk']}ml")
        print(f"Coffee:{self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for items in drink.ingredients:
            if drink.ingredients[items] > self.resources[items]:
                print(f"Sorry there is not enough {items}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for items in order.ingredients:
            self.resources[items] -= order.ingredients[items]
        print(f"Here is your {order.name}. Enjoy!")