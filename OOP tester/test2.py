class ToyRobot:
    def __init__(self, name, battery_level):
        self.name = name                # Public attribute
        self.__battery_level = battery_level  # Private attribute (using double underscore)

    def walk(self):
        if self.__battery_level > 0:
            print(f"{self.name} is walking!")
            self.__battery_level -= 1
        else:
            print(f"{self.name} has no battery left!")

    def charge(self):
        print(f"Charging {self.name}...")
        self.__battery_level = 5

# Create an object
robot = ToyRobot("Robo", 3)

robot.walk()  # Robo is walking!
robot.__battery_level = 0  # Won't change the actual battery level because it's private
robot.walk()  # Robo is walking!
robot.charge()  # Charging Robo...
