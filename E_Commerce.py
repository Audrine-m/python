def add_product(product_name, price, quantity):

  product = {
    "name": product_name,
    "price": price,
    "quantity": quantity
  }
  return product

def update_price(product, new_price):

  product["price"] = new_price
  return product

def update_quantity(product, quantity_change):

  product["quantity"] = product["quantity"] + quantity_change
  
  if product["quantity"] < 0:
    print(f"Warning: Product {product['name']} cannot have negative stock.")
    product["quantity"] = 0
  return product

# Example
product1 = add_product("T-Shirt", 19.99, 20)
print(product1)

product1 = update_price(product1, 22.50)
print(product1)

product1 = update_quantity(product1, 5)
print(product1)

product1 = update_quantity(product1, -10)
print(product1)
