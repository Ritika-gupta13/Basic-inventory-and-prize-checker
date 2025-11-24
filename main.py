import json
import os
import sys

INVENTORYFILE = 'inventory_data.json'
LOW_STOCKTHRESHOLD = 10

class Product:
    def __init__(self, name: str, price: float, stock: int, item_code: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.item_code = item_code

    def __str__(self):
        return f"Code: {self.item_code.ljust(6)} | Name: {self.name.ljust(20)} | Price: Rs{self.price:.2f} | Stock: {self.stock}"

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "item_code": self.item_code
        }

def load_inventory():
    if not os.path.exists(INVENTORYFILE):
        return []
    
    try:
        with open(INVENTORYFILE, 'r') as f:
            data = json.load(f)
            return [Product(
                name=item['name'], 
                price=item['price'], 
                stock=int(item['stock']), 
                item_code=item['item_code']
            ) for item in data]
    except (IOError, json.JSONDecodeError, KeyError, ValueError):
        print(f"Warning: Could not read {INVENTORYFILE} or file format is incorrect. Starting with an empty inventory.")
        return []

def save_inventory(inventory):
    data = [product.to_dict() for product in inventory]
    
    try:
        with open(INVENTORYFILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Inventory saved successfully.")
    except IOError:
        print("Error: Could not save inventory file.")

def generate_item_code(inventory):
    if not inventory:
        return "ITM001"
    
    codes = [int(p.item_code[3:]) for p in inventory if p.item_code.startswith("ITM")]
    new_num = max(codes) + 1 if codes else 1
    return f"ITM{new_num:03d}"

def add_product(inventory):
    print("\n--- Add New Product ---")
    name = input("Enter product name: ").strip()
    
    while True:
        try:
            price = float(input("Enter price (e.g., 19.99): Rs"))
            if price <= 0:
                print("Price must be positive.")
                continue
            break
        except ValueError:
            print("Invalid price format.")

    while True:
        try:
            stock = int(input("Enter initial stock level: "))
            if stock < 0:
                print("Stock cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid stock number.")

    item_code = generate_item_code(inventory)
    new_product = Product(name, price, stock, item_code) 
    inventory.append(new_product)
    
    print(f"\nProduct added: {new_product}")

def view_inventory(inventory):
    print("\n\n=============== Full Inventory Report ===============")
    if not inventory:
        print("The inventory is currently empty.")
        return

    sorted_inventory = sorted(inventory, key=lambda p: p.item_code)
    
    for product in sorted_inventory:
        print(f"| {product}")
        
    print("=====================================================\n")

def update_stock_and_price(inventory):
    code_to_update = input("\nEnter ItemCode of the product to update: ").upper().strip()
    
    product_found = None
    for product in inventory:
        if product.item_code == code_to_update: 
            product_found = product
            break

    if not product_found:
        print(f"Product with ItemCode '{code_to_update}' not found.")
        return

    print(f"\n--- Updating Product: {product_found.name} (Current Stock: {product_found.stock}, Price: Rs{product_found.price:.2f}) ---")

    while True:
        new_stock = input("Enter new stock level (leave blank to skip): ").strip()
        if not new_stock:
            break
        try:
            stock = int(new_stock)
            if stock < 0:
                print("Stock cannot be negative.")
                continue
            product_found.stock = stock
            break
        except ValueError:
            print("Invalid stock number.")

    while True:
        new_price = input("Enter new price (leave blank to skip): Rs").strip()
        if not new_price:
            break
        try:
            price = float(new_price)
            if price <= 0:
                print("Price must be positive.")
                continue
            product_found.price = price
            break
        except ValueError:
            print("Invalid price format.")

    print(f"\nProduct updated: {product_found}")

def view_low_stock(inventory):
    print(f"\n--- Low Stock Alert (Threshold: {LOW_STOCKTHRESHOLD}) ---")
    
    low_stock_items = [p for p in inventory if p.stock < LOW_STOCKTHRESHOLD] 
    
    if not low_stock_items:
        print("All products are above the low stock threshold.")
        return
        
    for product in low_stock_items:
        print(f"LOW STOCK: {product.name.ljust(20)} | Code: {product.item_code.ljust(6)} | Stock: {product.stock}")

def inventory_manager_app():
    inventory = load_inventory()
    print("=======================================================")
    print("  Basic Inventory & Price Checker (Retail E-commerce)")
    print(f"  Loaded {len(inventory)} products from {INVENTORYFILE}")
    print("=======================================================")
    
    while True:
        print("\n--- Menu ---")
        print("1. Add New Product (Create)")
        print("2. View All Inventory (Read)")
        print("3. Update Stock/Price (Update)")
        print("4. View Low Stock Items")
        print("5. Save & Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            update_stock_and_price(inventory)
        elif choice == '4':
            view_low_stock(inventory)
        elif choice == '5':
            save_inventory(inventory)
            print("Application closed.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    try:
        inventory_manager_app()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting without saving.")
        sys.exit(0)
