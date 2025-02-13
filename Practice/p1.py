# n = 5
# k=5
# for i in range(n):
#     p=k
#     for j in range(i+1):
#         print(" ",end ="")
#     for j in range(i,n):
#         print(p,end="")
#         p -= 1
#     k -=1
#     print()



# def rev(n):
#     reve= ''
#     for i in n:
#         reve = i + reve
#     print(reve)

# n = input()
# rev(n)



def r(n):
    reverse_num =0
    while n>0:
        digit = n %10
        reverse_num = reverse_num*10+digit
        n = n//10
    return reverse_num

n = int(input())
result = r(n)
print(result)

class Order:
    def __init__(self):
        self.total = 0  # Initialize total order value to 0

    def place_order(self, amount):
        if amount <= 0:
            raise ValueError("Order amount must be positive.")  # Raise error for negative order
        self.total += amount  # Add amount to total
        print(f"Order of {amount} placed successfully. Current total: {self.total}")

    def apply_discount(self, discount):
        if discount < 0:
            raise ValueError("Discount cannot be negative.")  # Raise error for negative discount
        if discount > self.total:
            raise ValueError("Discount cannot be greater than total order value.")  # Prevent excessive discount
        self.total -= discount  # Subtract discount from total
        print(f"Discount of {discount} applied successfully. Current total: {self.total}")

# Main program
order = Order()

try:
    order_amount = int(input())  # Get order amount
    order.place_order(order_amount)  # Place order
except ValueError as e:
    print(f"Order failed. {e}")

try:
    discount_amount = int(input())  # Get discount amount
    order.apply_discount(discount_amount)  # Apply discount
except ValueError as e:
    print(f"Discount failed. {e}")