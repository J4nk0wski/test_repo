import pygame

class Drone:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

def main():
	print("It works!")
	drone_1 = Drone(10, 20)
	print("Drone 1: \n" + "weight: " + str(drone_1.weight) + "\nheight: " + str(drone_1.height))

if __name__ == "__main__":
	main()