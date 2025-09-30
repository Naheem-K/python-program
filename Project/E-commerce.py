class User:
    def __init__(self,Name,Password):
        self.Name = Name
        self.__Password = Password
    
    def check_password(self,Password):
        return self.__Password == Password

   

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category


class Cart:
    def __init__(self):
        self.Product = []
    def add_Product(self,Product):
        self.Product.append(Product)
    def Remove_product(self,Product_name):
        self.Product = [p for p in self.Product if p.name != Product_name]
    def calculate_total_value(self):
        return sum(p.price for p in self.Product)
    

class order:
    def __init__(self,User,cart):
        self.User = User
        self.cart = cart
        self.item = cart.Product.copy()
        self.status = "NEW"
    def set_status(self,status):
        self.status = status

    def set_status(self,status):
        allowed = ['Ordered','Pending','Confirmed','Canceled']
        if status in allowed:
            self.status = status
        else:
            print('Invalid Status')



    
class Payment:
    def __init__(self,UPI_Payment,Cash,Swipe):
        self.UPI_Payment = UPI_Payment
        self.Cash = Cash
        self.Swipe = Swipe



# Create a user
user1 = User("Shibila", "1234")

# Authenticate
print(user1.check_password("1234"))  # ✅ True

# Create products
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Phone", 25000, "Electronics")
p3 = Product("Shoes", 2000, "Fashion")

# Add to cart
cart1 = Cart()
cart1.add_Product(p1)
cart1.add_Product(p3)
print("Cart total:", cart1.calculate_total_value())  # 52000

# Place order
order1 = order(user1, cart1)
order1.set_status("Ordered")
print("Order status:", order1.status)

# Make payment
payment1 = Payment(UPI_Payment=True, Cash=False, Swipe=False)
if payment1.UPI_Payment:
    print("Payment successful via UPI ✅")
    order1.set_status("Confirmed")

# Final Order Summary
print("Final Status:", order1.status)
for item in order1.item:
    print(item.name, "-", item.price)
