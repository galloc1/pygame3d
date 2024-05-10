from dataclasses import dataclass
import pygame
import colours
import math

@dataclass
class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __sub__(self, y):   # Subtracting a vector from a vector returns a vector with x=x1-x2, y=..., z=...
        subtractedVector = Vector3()
        subtractedVector.x = self.x-y.x
        subtractedVector.y = self.y-y.y
        subtractedVector.z = self.z-y.z
        return subtractedVector
    
    def __mul__(self, y):   # Same as __sub__ but with multiplication instead
        multipliedVector = Vector3()
        multipliedVector.x = self.x*y.x
        multipliedVector.y = self.y*y.y
        multipliedVector.z = self.z*y.z
        return multipliedVector

    def magnitude(self):    # Returns the length of the vector
        magnitude = math.sqrt(pow(self.x, 2)+pow(self.y, 2)+pow(self.z, 2))
        return magnitude
    
    def normalise(self):    # Returns a vector with length 1
        normalisedVector = Vector3()
        magnitude = self.magnitude()
        normalisedVector.x = self.x/magnitude
        normalisedVector.y = self.y/magnitude
        normalisedVector.z = self.z/magnitude
        return normalisedVector

@dataclass
class Transform:
    position: Vector3 = Vector3()
    rotation: Vector3 = Vector3()

class Camera:
    def __init__(self, transform):
        self.transform = transform

class Line:
    def __init__(self, surface, length, transform):
        self.surface = surface
        self.length = length
        self.transform = transform
    
    def draw(self, camera):
        relativeRotation = self.transform.rotation - camera.transform.rotation  # The rotation of the line relative to the camera
        distance = (self.transform.position.z - camera.transform.position.z)
        fov = 90
        sizeOnScreen = (self.length*math.sin(relativeRotation.magnitude()))/(distance*(fov/45))
        startPoint = (self.transform.position.x, self.transform.position.y)
        dispx = (sizeOnScreen*math.sin(relativeRotation.x)/math.sin(math.radians(90)))
        dispy = (sizeOnScreen*math.sin(relativeRotation.y)/math.sin(math.radians(90)))
        endPoint = (startPoint[0]+dispx, startPoint[1]+dispy)
        pygame.draw.line(self.surface, colours.black, startPoint, endPoint, )
        

        