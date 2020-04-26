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


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a {} kw battery.".format(self.battery_size))

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "this car can go approximately {} miles".format(range)
        print(message)


class ElectricCar(Car):
    def __init__(self, manufacture, model, year):
        super().__init__(manufacture, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model s", "2018")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

