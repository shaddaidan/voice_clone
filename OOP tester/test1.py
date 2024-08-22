# This is our class (the blueprint)
class ToyCar:
    def __init__(self, color, size):  # This is the constructor method
        self.color = color  # Attribute
        self.size = size    # Attribute

    def move(self):  # This is a method (an action the toy car can do)
        print("The car is moving!")

    def stop(self):  # Another method
        print("The car has stopped.")

# Create a red, small toy car
my_car = ToyCar(color="red", size="small")

# Use the methods to make the car move and stop
my_car.move()
my_car.stop()
