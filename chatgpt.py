import random
import string

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, amount, price):
        self.items.append((product, amount, price))

    def remove_item(self, product):
        for i in range(len(self.items)):
            if self.items[i][0] == product:
                del self.items[i]
                break

    def get_total(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        return total

def generate_transaction_code(items):
    code = ""
    for item in items:
        code += random.choice(string.ascii_letters)
        code += str(item[1])
        code += str(item[2])
    return code

cart = ShoppingCart()

while True:
    print("Enter 'a' to add an item, or 'done' to finish:")
    choice = input()
    if choice == "done":
        break
    elif choice == "a":
        product = input("Enter product name: ")
        amount = 0
        while True:
            try:
                amount = int(input("Enter amount: "))
                break
            except:
                print("not integer")
        price = float(input("Enter price: "))
        cart.add_item(product, amount, price)

transaction_code = generate_transaction_code(cart.items)
print("Transaction code:", transaction_code)

print("List of items:")
for item in cart.items:
    print("Product:", item[0])
    print("Amount:", item[1])
    print("Price:", item[2])
    print("Total:", item[1] * item[2])
    print()

print("Total cost:", cart.get_total())

while True:
    print("Enter 'r' to remove an item, or 'done' to finish:")
    choice = input()
    if choice == "done":
        break
    elif choice == "r":
        product = input("Enter product name: ")
        cart.remove_item(product)

print("List of items:")
for item in cart.items:
    print("Product:", item[0])
    print("Amount:", item[1])
    print("Price:", item[2])
    print("Total:", item[1] * item[2])
    print()

print("Total cost:", cart.get_total())

while True:
    print("Enter 'b' to buy, or 'c' to cancel:")
    choice = input()
    if choice == "b":
        print("Thank you for your purchase!")
        break
    elif choice == "c":
        print("Transaction cancelled.")
        break
