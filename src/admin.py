class AdminPanel:
    def __init__(self,vehicles):
        self.vehicles = vehicles

    def add_vehicles(self,vehicle_id,vehicle_Type,vehicle_model,vehicle_rent):
        self.vehicles[vehicle_id] = {
            "type": vehicle_Type,
            "model": vehicle_model,
            "rent": vehicle_rent,
            "status": "Available"
            }
        


        print(f"Vehicle : {vehicle_id}, {vehicle_Type} - {vehicle_model} was added succesfully") 
    

    def view_vehicles(self):
        for key, value in self.vehicles.items():
             print(f"ID: {key} , Details : {value["type"]}, {value["model"]}, for rupees : {value["rent"]} is {value["status"]}")