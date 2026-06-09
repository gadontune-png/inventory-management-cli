from utils.storage import load_json, save_json, load_state, save_state
from rich.console import Console
from rich.table import Table

console = Console()

state = load_state()

SUPPLIERS = "data/suppliers.json"
PRODUCTS = "data/products.json"
WAREHOUSES = "data/warehouses.json"
TRANSACTIONS = "data/transactions.json"


def next_id(key):
    state[key] += 1
    save_state(state)
    return state[key]


# ---------------- SUPPLIER ----------------
def add_supplier():
    name = input("Name: ")
    email = input("Email: ")

    data = load_json(SUPPLIERS)
    data.append({
        "supplier_id": next_id("supplier_id"),
        "name": name,
        "email": email
    })
    save_json(SUPPLIERS, data)
    console.print("[green]Supplier added[/green]")


def list_suppliers():
    table = Table(title="Suppliers")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")

    for s in load_json(SUPPLIERS):
        table.add_row(str(s["supplier_id"]), s["name"], s["email"])

    console.print(table)


# ---------------- WAREHOUSE ----------------
def add_warehouse():
    name = input("Name: ")
    location = input("Location: ")

    data = load_json(WAREHOUSES)
    data.append({
        "warehouse_id": next_id("warehouse_id"),
        "name": name,
        "location": location
    })

    save_json(WAREHOUSES, data)
    console.print("[green]Warehouse added[/green]")


# ---------------- PRODUCT ----------------
def add_product():
    sku = input("SKU: ")
    name = input("Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    supplier_id = int(input("Supplier ID: "))
    warehouse_id = int(input("Warehouse ID: "))

    data = load_json(PRODUCTS)
    data.append({
        "product_id": next_id("product_id"),
        "sku": sku,
        "name": name,
        "price": price,
        "quantity": qty,
        "supplier_id": supplier_id,
        "warehouse_id": warehouse_id
    })

    save_json(PRODUCTS, data)
    console.print("[green]Product added[/green]")


def list_products():
    table = Table(title="Products")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Stock")
    table.add_column("Price")

    for p in load_json(PRODUCTS):
        table.add_row(
            str(p["product_id"]),
            p["name"],
            str(p["quantity"]),
            str(p["price"])
        )

    console.print(table)


def search_product():
    name = input("Search: ").lower()

    results = [
        p for p in load_json(PRODUCTS)
        if name in p["name"].lower()
    ]

    table = Table(title="Search Results")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Stock")

    for p in results:
        table.add_row(str(p["product_id"]), p["name"], str(p["quantity"]))

    console.print(table)


# ---------------- STOCK ----------------
def stock_in():
    pid = int(input("Product ID: "))
    qty = int(input("Qty: "))

    data = load_json(PRODUCTS)

    for p in data:
        if p["product_id"] == pid:
            p["quantity"] += qty

    save_json(PRODUCTS, data)
    console.print("[green]Stock updated[/green]")


def stock_out():
    pid = int(input("Product ID: "))
    qty = int(input("Qty: "))

    data = load_json(PRODUCTS)

    for p in data:
        if p["product_id"] == pid:
            if p["quantity"] < qty:
                console.print("[red]Not enough stock[/red]")
                return
            p["quantity"] -= qty

    save_json(PRODUCTS, data)
    console.print("[green]Stock updated[/green]")


# ---------------- DASHBOARD ----------------
def dashboard():
    products = load_json(PRODUCTS)

    total_stock = sum(p["quantity"] for p in products)

    console.print("\n[bold cyan]INVENTORY DASHBOARD[/bold cyan]")
    console.print(f"Products: {len(products)}")
    console.print(f"Total Stock: {total_stock}\n")


# ---------------- MENU ----------------
def menu():
    while True:
        console.print("\n[bold yellow]INVENTORY SYSTEM[/bold yellow]")
        print("1. Add Supplier")
        print("2. List Suppliers")
        print("3. Add Warehouse")
        print("4. Add Product")
        print("5. List Products")
        print("6. Stock In")
        print("7. Stock Out")
        print("8. Search Product")
        print("9. Dashboard")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_supplier()
        elif choice == "2":
            list_suppliers()
        elif choice == "3":
            add_warehouse()
        elif choice == "4":
            add_product()
        elif choice == "5":
            list_products()
        elif choice == "6":
            stock_in()
        elif choice == "7":
            stock_out()
        elif choice == "8":
            search_product()
        elif choice == "9":
            dashboard()
        elif choice == "0":
            break
        else:
            console.print("[red]Invalid choice[/red]")


if __name__ == "__main__":
    menu()