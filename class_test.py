PI = 3.1415926535897 #all letters in global constant should be upper-case with _ for spaces
#names of variables and functions shoudl use lower-case with _ for spaces

class Circle(): #class names should use CapWords
    def __init__(self, radius: float): #parameter in function def should have type annotation (except self and cls)
        self.radius = radius

    def circumference(self) -> float: #every float should have return type annotation
        return 2 * PI * self.radius
    

