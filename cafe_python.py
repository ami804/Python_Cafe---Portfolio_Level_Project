menu = {
    1: {"name": "Pizza", "price": 120},
    2: {"name": "Burger", "price": 80},
    3: {"name": "Pasta", "price": 100},
    4: {"name": "Coffee", "price": 50},
    5: {"name": "Sandwich", "price": 70}
}

cart = {}

def show_menu():
    print("\n------ PYTHON CAFE MENU ------")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ₹{item['price']}")

def take_order():
    while True:
        try:
            choice = int(input("\nEnter item number: "))
            
            if choice in menu:
                qty = int(input("Enter quantity: "))
                
                item_name = menu[choice]["name"]
                
                if item_name in cart:
                    cart[item_name] += qty
                else:
                    cart[item_name] = qty
                    
                print(f"{item_name} added to cart!")
            else:
                print("Invalid item number!")

        except:
            print("Please enter valid input!")

        more = input("Add more items? (yes/no): ")
        if more.lower() != "yes":
            break

def generate_bill():
    print("\n------ BILL RECEIPT ------")
    total = 0

    for item, qty in cart.items():
        price = next(v["price"] for v in menu.values() if v["name"] == item)
        item_total = price * qty
        total += item_total

        print(f"{item} x {qty} = ₹{item_total}")

    print("--------------------------")
    print("Total Bill = ₹", total)
    print("Thank you for visiting Python Cafe!")

def main():
    print("Welcome to Python Cafe ☕")
    show_menu()
    take_order()
    generate_bill()

main()