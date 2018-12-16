from car import Car


class Battery():
    """模拟电瓶"""
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

