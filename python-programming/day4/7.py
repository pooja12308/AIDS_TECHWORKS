<<<<<<< HEAD

class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate  
        self.__owner_name = owner_name        

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print("Generic Vehicle")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def display(self):
        print(f"SUV - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def display(self):
        print(f"Truck - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 100 * hours


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size
        self.__is_occupied = False
        self.__vehicle = None

    def assign_vehicle(self, vehicle):
        if not self.__is_occupied:
            self.__vehicle = vehicle
            self.__is_occupied = True
            print(f"Parked {vehicle.get_license_plate()} at Spot {self.spot_id}")
        else:
            print(f"Spot {self.spot_id} already occupied.")

    def remove_vehicle(self, hours):
        if self.__is_occupied:
            fee = self.__vehicle.calculate_parking_fee(hours)
            print(f"Unparked {self.__vehicle.get_license_plate()} from Spot {self.spot_id}")
            self.__vehicle = None
            self.__is_occupied = False
            return fee
        return 0

    def show_status(self):
        status = "Occupied" if self.__is_occupied else "Empty"
        print(f"Spot {self.spot_id} ({self.__size}) → {status}")


class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            spot.show_status()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot._ParkingSpot__is_occupied:  # access private internally
                spot.assign_vehicle(vehicle)
                return spot
        print("No empty spots.")
        return None

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot._ParkingSpot__vehicle == vehicle:
                return spot.remove_vehicle(hours)
        print("Vehicle not found.")
        return 0


class Payment():

    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in Cash.")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} by Card.")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")


if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "M"))
    lot.add_spot(ParkingSpot(2, "L"))

    v1 = Bike("B123", "mahesh")
    v2 = Car("C456", "Babu")


    for v in [v1, v2]:
        v.display()

    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.show_spots()


    fee = lot.unpark_vehicle(v1, 2)
    if fee > 0:
        UPIPayment().process_payment(fee)

    fee = lot.unpark_vehicle(v2, 3) 
    if fee > 0:
        CardPayment().process_payment(fee)

    lot.show_spots()
=======

class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate  
        self.__owner_name = owner_name        

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print("Generic Vehicle")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def display(self):
        print(f"SUV - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def display(self):
        print(f"Truck - {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 100 * hours


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size
        self.__is_occupied = False
        self.__vehicle = None

    def assign_vehicle(self, vehicle):
        if not self.__is_occupied:
            self.__vehicle = vehicle
            self.__is_occupied = True
            print(f"Parked {vehicle.get_license_plate()} at Spot {self.spot_id}")
        else:
            print(f"Spot {self.spot_id} already occupied.")

    def remove_vehicle(self, hours):
        if self.__is_occupied:
            fee = self.__vehicle.calculate_parking_fee(hours)
            print(f"Unparked {self.__vehicle.get_license_plate()} from Spot {self.spot_id}")
            self.__vehicle = None
            self.__is_occupied = False
            return fee
        return 0

    def show_status(self):
        status = "Occupied" if self.__is_occupied else "Empty"
        print(f"Spot {self.spot_id} ({self.__size}) → {status}")


class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            spot.show_status()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot._ParkingSpot__is_occupied:  # access private internally
                spot.assign_vehicle(vehicle)
                return spot
        print("No empty spots.")
        return None

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot._ParkingSpot__vehicle == vehicle:
                return spot.remove_vehicle(hours)
        print("Vehicle not found.")
        return 0


class Payment():

    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in Cash.")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} by Card.")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")


if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "M"))
    lot.add_spot(ParkingSpot(2, "L"))

    v1 = Bike("B123", "mahesh")
    v2 = Car("C456", "Babu")


    for v in [v1, v2]:
        v.display()

    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.show_spots()


    fee = lot.unpark_vehicle(v1, 2)
    if fee > 0:
        UPIPayment().process_payment(fee)

    fee = lot.unpark_vehicle(v2, 3) 
    if fee > 0:
        CardPayment().process_payment(fee)

    lot.show_spots()
>>>>>>> d283d138443d18f417b8952a56da15ce85d46d2b
