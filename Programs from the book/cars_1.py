
'''Present a car Class''' 
class Car():
    '''Smple car model'''
    
    def __init__(self, make, model, year):
        '''initialize attributes description of a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        '''Return formated discription'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_ododmeter(self):
        ''' Show the car mileage in miels '''
        print("This car has " + str(self.odometer_reading) + " milf on it.")
    
    def update_odometer(self, mileafe):
        '''Setup set value on odometer.
        if someon try to do value less, skript reject it '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant`t roll back an odometer!")
    
    
    def increament_odometer(self, miles):
        ''' '''
        self.odometer_reading += miles

class Battery():
    
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximatly " + str(range)
        message += " miles on a full charge."
        print(message)
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    
    def fill_gas_tank():
        print("This car doesn`t need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


