class Stock:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def update_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            print("Item not found")

    def get_item_quantity(self, item_name):
        return self.items.get(item_name, 0)