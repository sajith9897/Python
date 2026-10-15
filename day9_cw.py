class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: ₹{self._base_rate:.2f}"

    def rental_charge(self):
        return 0.0

class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self.num_seats

class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5

def calculate_rental(vehicle):
    return vehicle.rental_charge()


v1 = Vehicle("VEH001", 100.00)
car1 = Car("CAR001", 100.00, 4)
bike1 = Bike("BIKE001", 100.00, "Motorcycle")


print("Vehicle Details")
print(v1.display_details())
print("Rental Charge: ₹", calculate_rental(v1))

print("\nCar Details")
print(car1.display_details())
print("Number of Seats:", car1.num_seats)
print("Rental Charge: ₹", calculate_rental(car1))

print("\nBike Details")
print(bike1.display_details())
print("Bike Type:", bike1.bike_type)
print("Rental Charge: ₹", calculate_rental(bike1))