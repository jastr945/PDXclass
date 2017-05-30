class Car:
    number_of_wheels = 4
    def __init__(self, color, number_of_doors):
        self.color = color
        self.number_of_doors = number_of_doors

    def print_characteristics(self):
        print(self.color, self.number_of_doors)

    def honk(self):
        print('Honk!')
#
# mazda = Car('red', 4)
# #
# subaru = Car('blue', 2)
