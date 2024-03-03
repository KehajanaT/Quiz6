class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items
class Calculate:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_total(self, cart):
        subtotal = sum(item.price for item in cart.items)
        tax = subtotal * self.tax_rate
        return subtotal + tax

class Customerinfo:
    def __init__(self, info):
        self.info = info

    def info(self, address, email):
        print("Customer info")

class Email:
    def __init__(self, email_service):
        self.email_service = email_service

    def send_confirmation(self, cart, email):
        self.email_service.send_email(email, "Order Confirmation")

class Order:
    def __init__(self, tax_rate, information , email_service):
        self.cart = Cart()
        self.calculate = Calculate(tax_rate)
        self.customerinfo = Customerinfo(information)
        self.confirmation = Email(email_service)

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def get_cart_items(self):
        return self.cart.get_items()

    def checkout(self, payment_method):
        total = self.calculate.calculate_total(self.cart)
        self.payment_processor.checkout(self.cart, payment_method)
        self.order_confirmation.send_confirmation(self.cart, self.email)
        self.cart.clear()

