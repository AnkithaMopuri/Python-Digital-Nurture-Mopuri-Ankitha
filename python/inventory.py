class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


class Perishable(Product):
    pass


class Electronics(Product):
    pass


class Inventory:
    def __init__(self):
        self.items = {}          # dictionary: name -> product
        self.low_stock = set()   # set for alerts

    def add_product(self, product):
        self.items[product.name] = product

    def update_stock(self, name, stock):
        if name in self.items:
            self.items[name].stock = stock

    def check_low_stock(self):
        self.low_stock.clear()
        for name, product in self.items.items():
            if product.stock < 5:
                self.low_stock.add(name)

    def print_summary(self):
        print("\n--- Inventory Summary ---")
        for name, product in self.items.items():
            print(name, "Stock:", product.stock)

        self.check_low_stock()

        print("\nLow Stock Alerts:")
        for item in self.low_stock:
            print(item)


inv = Inventory()

inv.add_product(Perishable("Milk", 3))
inv.add_product(Electronics("Laptop", 10))
inv.add_product(Perishable("Eggs", 2))

inv.print_summary()