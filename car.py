class Car:
    def __init__(self, manufacture, model, year):
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def fill_gas(self):
        print("fill gas is needed")

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.manufacture + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has {} mile on it".format(self.odometer_reading))

    def update_odemeter(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you are not!")

    def increment_odometer(self, miles):
        self.odometer_reading = self.odometer_reading + miles







