class Product(object):
    """description of class"""
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

    # Getter
    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            current_value = float(value.replace('R$', ''))
        self._price = value

    @name.setter
    def name(self, value):
        self._name = value.title()
