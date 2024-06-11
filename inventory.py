<<<<<<< HEAD
inventory = {}

def add_item(name, quantity):
  """Adds an item to the inventory or updates its quantity if it already exists."""
  if name in inventory:
    inventory[name] += quantity
  else:
    inventory[name] = quantity

def get_item_quantity(name):
  """Retrieves the quantity of a specific item in the inventory."""
  return inventory.get(name, 0)  # Return 0 if item is not found

def calculate_total_quantity():
  """Calculates and displays the total quantity of all items in the inventory."""
  total_quantity = sum(inventory.values())
  print(f"Total quantity: {total_quantity}")

def main():
  """Main loop for user interaction"""
  while True:
    print("\nInventory System")
    print("1. Add Item")
    print("2. Get Item Quantity")
    print("3. Calculate Total Quantity")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter item name: Pineapple")
      quantity = int(input("Enter quantity: 3000"))
      add_item(name, quantity)
      print(f"{name} added to inventory.")
    elif choice == '2':
      name = input("Enter item name: ")
      quantity = get_item_quantity(name)
      if quantity > 0:
        print(f"Quantity of {name}: {quantity}")
      else:
        print(f"Item {name} not found in inventory.")
    elif choice == '3':
      calculate_total_quantity()
    elif choice == '4':
      print("Exiting inventory system.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
=======
inventory = {}

def add_item(name, quantity):
  """Adds an item to the inventory or updates its quantity if it already exists."""
  if name in inventory:
    inventory[name] += quantity
  else:
    inventory[name] = quantity

def get_item_quantity(name):
  """Retrieves the quantity of a specific item in the inventory."""
  return inventory.get(name, 0)  # Return 0 if item is not found

def calculate_total_quantity():
  """Calculates and displays the total quantity of all items in the inventory."""
  total_quantity = sum(inventory.values())
  print(f"Total quantity: {total_quantity}")

def main():
  """Main loop for user interaction"""
  while True:
    print("\nInventory System")
    print("1. Add Item")
    print("2. Get Item Quantity")
    print("3. Calculate Total Quantity")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter item name: Pineapple")
      quantity = int(input("Enter quantity: 3000"))
      add_item(name, quantity)
      print(f"{name} added to inventory.")
    elif choice == '2':
      name = input("Enter item name: ")
      quantity = get_item_quantity(name)
      if quantity > 0:
        print(f"Quantity of {name}: {quantity}")
      else:
        print(f"Item {name} not found in inventory.")
    elif choice == '3':
      calculate_total_quantity()
    elif choice == '4':
      print("Exiting inventory system.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
>>>>>>> a838971ed257ecd7c0284abc69d99cd3f52561fa
  main()