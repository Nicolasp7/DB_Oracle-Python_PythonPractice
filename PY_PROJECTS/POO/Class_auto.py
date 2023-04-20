class auto:
    def __init__(self):  # Class variable and attributes
        self.brand = "BMW"
        self.doors = 4
        self.color = 'red'
        self.weight = 800

    def functions(self):  # Method to define auto functions
        self.on = True
        self.start = True
        self.speedup = True
        self.brakes = True

    def data(self):
        print('Brand car: ', self.brand, '\nDoors: ', self.doors, '\nColor: ', self.color, '\nWeight: ', self.weight, 'kg')

my_auto = auto()
my_auto.data()
