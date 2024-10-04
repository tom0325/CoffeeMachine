
class Menu:
    def __init__(self):
        self.menu =[
            MenuItem(name="latte",water=200,milk=150,coffee=24,cost=2.5),
            MenuItem(name="espresso",water=50,milk=0,coffee=18,cost=1.5),
            MenuItem(name="cappuccino",water=250,milk=50,coffee=24,cost=3),
        ]

    def get_items(self):
        options = ""
        for items in self.menu:
            options += f"{items.name}/"
        return options

    def find_drink(self, order_name):
        for items in self.menu:
            if items.name == order_name:
                return items
        print("Sorry that item is not available.")


class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
