class CustomerPanel:
    def __init__(self, customers, vehicles):
        self.vehicles = vehicles
        self.customers = customers

    def add_customer(self, Name, Card_number):
        self.customers[Card_number] = {
            "customer_name": Name,
            "rented_status": None
        }
        print(f"Customer: {Name} was added successfully")

    def view_vehicles(self):
        for key, value in self.vehicles.items():
            if value["status"] == "Available":
                print(f"ID: {key}, Details: {value['type']}, {value['model']}, Rent: {value['rent']}")

    def rent_vehicles(self, card_number, vehicle_id):

        if card_number not in self.customers:
            print("Customer does not exist, Please Register")
            return

        if vehicle_id not in self.vehicles:
            print("Vehicle does not exist")
            return

        if self.vehicles[vehicle_id]["status"] != "Available":
            print("Vehicle already rented")
            return

        self.customers[card_number]["rented_status"] = vehicle_id
        self.vehicles[vehicle_id]["status"] = "Rented"

        print(f"Customer: {self.customers[card_number]['customer_name']} has rented: {vehicle_id}")

    def return_vehicles(self, card_number):

        if card_number not in self.customers:
            print("Customer does not exist")
            return

        rented_vehicle = self.customers[card_number]["rented_status"]

        if rented_vehicle is None:
            print("Customer has not rented any vehicle")
            return

        self.vehicles[rented_vehicle]["status"] = "Available"
        self.customers[card_number]["rented_status"] = None

        print(f"Vehicle: {rented_vehicle} returned successfully by {self.customers[card_number]['customer_name']}")