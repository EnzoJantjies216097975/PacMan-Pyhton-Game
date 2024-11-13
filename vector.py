import math

# Class to represent a 2D vector with basic vector operations
class Vector2(object):
    # function that sets initial x and y values
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    # Function that adds two vectors and returns a new vector
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # Function that subtracts another vector from the current one and returns a new vector
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    # Function returns a new vector pointing in the opposite direction
    def __neg__(self):
        return Vector2(-self.x, -self.y)

    # Function scales the vector by multiplying it by a given number
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    # Function scalees the vector down by dividing it by a giving number
    def __div__(self, scalar):
        if scalar != 0:
            return Vector2(self.x / float(scalar), self.y/float(scalar))
        return None

    # This Function handles division in Python, using true division
    def __truediv__(self, scalar):
        return self.__div__(scalar) # Calls the __div__ method for division

    # This function checks if the current vector is equal to another vector
    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
            return False

    # This function calculates and returns the square of the vector's length (magnitude)
    def magnitudeSquared(self):
        return self.x ** 2 + self.y ** 2

    # This function calculates and returns the actual length (magnitude) of the vector
    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    # This function returns a copy of the vector
    def copy(self):
        return Vector2(self.x, self.y)

    # This function returns the vector as a tuple
    def asTuple(self):
        return self.x, self.y

    # This function returns the vectors as a tuple of integers (rounded down)
    def asInt(self):
        return int(self.x), int(self.y)

    # This function returns a string representation of the vector for printing
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"