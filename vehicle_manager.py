class VehicleManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_all_vehicles(self):
        return self.vehicles

    def get_vehicle(self, plate_number):
        for vehicle in self.vehicles:
            if vehicle.plate_number == plate_number:
                return vehicle
        return None
