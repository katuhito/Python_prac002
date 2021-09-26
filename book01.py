class Book:
    def __init__(self, raw_price):
        if raw_price < 0:
            raise ValueError('price must be positive')
        self.raw_price = raw_price
        self._discounts = 0
        
        @property
        def discounts(self):
            return self._discounts
        
        @discounts.setter
        def discounts(self, value):
            if value < 0 or 100 < value:
                raise ValueError(
                    'discounts must be between 0 and 100'
                )
            self._discounts = value
        
        @property
        def price(self):
            multi = 100 - self._discounts
            return int(self.raw_price * multi / 100)










        