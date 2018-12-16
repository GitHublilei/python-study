class Restaurant():
    """ 定义一家餐馆"""

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print(self.restaurant_name + ' ' + self.restaurant_type)

    def open_restaurant(self):
        print("现在正在营业")

my_restaurant = Restaurant('viclilei', 'eating')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
