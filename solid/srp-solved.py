class Book:
    def __init__(self, name, author, year, price, isbn):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
        self.isbn = isbn


class Invoice:
    def cal_total(self):
        price = (self._book.price - self._book.price * self._disc_rate) * self.quant
        price_with_tax = price * (1 + self._tax_rate)
        return price_with_tax

    def __init__(self, book, quantity, discount_rate, tax_rate):
        self._book = book
        self.quant = quantity
        self._disc_rate = discount_rate
        self.tax_rate = tax_rate
        self.total = self.cal_total()


class InvoicePrinter:
    def __init__(self, invoice):
        self.invoice = invoice

    def print(self):
        invoice = self.invoice
        print(f"{invoice.quant}x {invoice.book.name} {invoice.book.price}$")
        print(f"Discount rate: {invoice._disc_rate}")
        print(f"Tax rate: {invoice._tax_rate}")
        print(f"Total: {invoice._total}")


class InvoicePersistence:
    def __init__(self, invoice):
        self.invoice = invoice

    def save(self, filename):
        pass
