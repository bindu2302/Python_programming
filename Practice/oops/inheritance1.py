class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_car_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")

class Insurance:
    def __init__(self, insurance_provider, insurance_expiry):
        self.insurance_provider = insurance_provider
        self.insurance_expiry = insurance_expiry

    def insurance_info(self):
        print(f"Insurance provider: {self.insurance_provider}")
        print(f"Insurance Expiry: {self.insurance_expiry}")

class Car(Vehicle, Insurance):
    def __init__(self, make, model, car_id, insurance_provider, insurance_expiry):
        Vehicle.__init__(self, make, model)
        Insurance.__init__(self, insurance_provider, insurance_expiry)
        self.car_id = car_id

    def display_car(self):
        self.display_car_info()
        print(f"Car ID: {self.car_id}")
        self.insurance_info()

make = input()
model = input()
car_id = input()
Insurance_provider = input()
Insurance_expiry = input()

car = Car(make, model, car_id, Insurance_provider, Insurance_expiry)
car.display_car()
