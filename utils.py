import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(3)

def moveForwardNorth(distance):
    print("Steve: I'm moving north!")
    
    t.setheading(90)
    t.forward(distance)

def moveForwardEast(distance):
    print("Steve: I'm moving east!")
    
    t.setheading(0)
    t.forward(distance)

def moveForwardSouth(distance):
    print("Steve: I'm moving south!")
    
    t.setheading(270)
    t.forward(distance)

def moveForwardWest(distance):
    print("Steve: I'm moving west!")
    
    t.setheading(180)
    t.forward(distance)

def moveForwardNorthEast(distance):
    print("Steve: I'm moving north-east!")
    
    t.setheading(45)
    t.forward(distance)

def moveForwardSouthEast(distance):
    print("Steve: I'm moving south-east!")
    
    t.setheading(315)
    t.forward(distance)

def moveForwardSouthWest(distance):
    print("Steve: I'm moving south-west!")
    
    t.setheading(225)
    t.forward(distance)

def moveForwardNorthWest(distance):
    print("Steve: I'm moving north-west!")
    
    t.setheading(135)
    t.forward(distance)    

def moveRandomDirection(distance):
    randomNumber = random.randint(1, 8)

    if randomNumber == 1:
        moveForwardNorth(distance)

    elif randomNumber == 2:
        moveForwardEast(distance)

    elif randomNumber == 3:
        moveForwardSouth(distance)

    elif randomNumber == 4:
        moveForwardWest(distance)

    elif randomNumber == 5:
        moveForwardNorthEast(distance)

    elif randomNumber == 6:
        moveForwardSouthEast(distance)

    elif randomNumber == 7:
        moveForwardSouthWest(distance)

    elif randomNumber == 8:
        moveForwardNorthWest(distance)

def setSteveColour(colour):
    t.color(colour)

def setSteveColourRandom():
    colours = ["red", "green", "blue", "black"]
    randomColour = random.choice(colours)

    t.color(randomColour)

def setSteveSpeed(speed):
    t.speed(speed)
