class ShoppingCart:
    # write your code here
    import numpy as np

    def __init__(self, total=0, emp_discount=None,
                 items={'name': [], 'price': []}):
        self.total = total
        self.employee_discount = emp_discount
        self.items = items

    def add_item(self, name, price, quantity=1):
        self.total += price*quantity
        for item in range(quantity):
            self.items['name'].append(name)
            self.items['price'].append(price)
        return self.total

    def mean_item_price(self):
        return self.items['price'].np.mean()


    def median_item_price(self):
        return median(self.items['price'])

    def apply_discount(self):
        pass

    def void_last_item(self):
        pass
