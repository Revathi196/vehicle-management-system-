class Vehicle:
    def __init__(self, plate_number, brand, model, year):
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} (Plate: {self.plate_number})"
