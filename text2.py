class Vehicle:
    """Base class representing a general vehicle."""

    def __init__(self, vehicle_id, brand, price):
        """Initialize vehicle attributes."""
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.price = price

    def display_vehicle(self):
        """Display the basic details of the vehicle."""
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Price:", self.price)


class Car(Vehicle):
    """Derived class representing a car that inherits from Vehicle."""

    def __init__(self, vehicle_id, brand, price, num_doors, fuel_type):
        """Initialize car attributes including vehicle properties."""
        super().__init__(vehicle_id, brand, price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_car_details(self):
        """Display vehicle details along with car specific information."""
        self.display_vehicle()
        print("Number of Doors:", self.num_doors)
        print("Fuel Type:", self.fuel_type)
        print()


# Creating objects
car1 = Car(101, "Toyota", 800000, 4, "Petrol")
car2 = Car(102, "Honda", 900000, 4, "Diesel")

# Displaying details
car1.display_car_details()
car2.display_car_details()