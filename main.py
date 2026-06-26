from src.admin import AdminPanel
from src.customer import CustomerPanel


def main():
    print("___________________________________________________________")
    print("------------------Welcome to Car Rentals-------------------")
    print("___________________________________________________________")

    vehicles = {}
    customers = {}

    admin = AdminPanel(vehicles)
    customer_operations = CustomerPanel(customers, vehicles)

    while True:
        print("\n============= MAIN PANEL =============")
        print("1. Admin Panel")
        print("2. Customer Panel")
        print("3. Exit")

        user_choice = input("Please select an option: ")

        # ---------------- ADMIN PANEL ----------------
        if user_choice == "1":
            print("===== Welcome to ADMIN PANEL =====")

            while True:
                print("*********************** ")
                print("1. Add Vehicle")
                print("2. View Vehicles")
                print("3. Exit Admin Panel")

                admin_choice = input("Select option: ")

                if admin_choice == "1":
                    vehicle_id = input("Enter vehicle ID: ")
                    vehicle_Type = input("Enter vehicle type: ")
                    vehicle_model = input("Enter vehicle model: ")
                    vehicle_rent = int(input("Enter rent per day: "))

                    admin.add_vehicles(vehicle_id, vehicle_Type, vehicle_model, vehicle_rent)

                elif admin_choice == "2":
                    print("Viewing all Vehicle")
                    admin.view_vehicles()

                elif admin_choice == "3":
                    print("Exiting Admin Panel")
                    break

                else:
                    print("Invalid Option!")

        # ---------------- CUSTOMER PANEL ----------------
        elif user_choice == "2":
            print("===== Welcome to CUSTOMER PANEL =====")

            while True:
                print()
                print("1. Add Customer")
                print("2. View Vehicles")
                print("3. Rent Vehicle")
                print("4. Return Vehicle")
                print("5. Exit Customer Panel")

                customer_choice = input("Select option: ")

                if customer_choice == "1":
                    name = input("Enter customer name: ")
                    card_number = input("Enter card number: ")
                    customer_operations.add_customer(name, card_number)

                elif customer_choice == "2":
                    customer_operations.view_vehicles()

                elif customer_choice == "3":
                    card_number = input("Enter card number: ")
                    vehicle_id = input("Enter vehicle ID: ")
                    customer_operations.rent_vehicles(card_number, vehicle_id)

                elif customer_choice == "4":
                    card_number = input("Enter card number: ")
                    customer_operations.return_vehicles(card_number)

                elif customer_choice == "5":
                    print("Exiting Customer Panel")
                    break

                else:
                    print("Invalid option!")

        # ---------------- EXIT ----------------
        elif user_choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()