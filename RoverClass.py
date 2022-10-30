import random
import math


class Rover:

    def __init__(self, battery=100.00, storage=10000):
        self.battery = battery
        self.storage = storage
        self.odometer = 0
        self.currentlocation = [0, 0]
        self.direction = 90
        self.compass = {
            "north": 0,
            "east": 90,
            "south": 180,
            "west": 270
        }

    def __ismovin__(self, roverstate=None):
        if roverstate:
            return self.battery - self.odometer
        else:
            return self.battery - 0.25

    def turnrover(self):
        onswitch = True
        print(f"The rover is facing{self.direction}")
        while onswitch:
            turn = input("Turn left or right? : R - Right | L - Left").lower()
            if turn == 'r':
                return self.direction + 90


# checks if rover is moving
# if yes, lower battery level by 1 per mile
# if no, lower battery level by 0.25


testRover = Rover()
testRover.odometer = 15
print(testRover.__ismovin__(True))
testRover.directionfacing(1, 1)
