class Book:
    def __init__(self, name, author, year, price, isbn):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
        self.isbn = isbn


class Invoice:
    def cal_total(self):
        price = (self._book.price - self._book.price * self._disc_rate) * self._quant
        price_with_tax = price * (1 + self._tax_rate)
        return price_with_tax

    def __init__(self, book, quantity, discount_rate, tax_rate):
        self._book = book
        self._quant = quantity
        self._disc_rate = discount_rate
        self._tax_rate = tax_rate
        self._total = self.cal_total()

    def price(self):
        print(f"{self._quant}x {self._book.name} {self.book.price}$")
        print(f"Discount rate: {self._disc_rate}")
        print(f"Tax rate: {self._tax_rate}")
        print(f"Total: {self._total}")

    def save(self, filename):
        pass
