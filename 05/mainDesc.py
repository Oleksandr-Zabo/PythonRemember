from Product import Product

samsung = Product("Galaxy S10", 500)

try:
    samsung.price=-100
except Exception as e:
    print(f"Error: {e}")

print(samsung)