'''
Name: Grace Yao
Date: August 27, 2025
Name of Program: Lab 1, "Name"
'''

PI = 3.1415926535897 #all letters in global constant are upper-case w/ _ for spaces
#names of variables and functions should use lower-case with _ for spaces
#all lines must be <80 chars

class Circle(): #class names should use CapWords
    def __init__(self, radius: float = 0):
        #parameter in function def should have type annotation (except self and cls)
        self.radius = radius

    def __str__(self) -> str:
        return f"Circle object with radius {self.radius}"

    def circumference(self) -> float: #every float should have return type annotation
        #each method should have a docstring (1 line with triple quotes) except Dunder methods
        '''Calculate the circumference of circle based on radius attribute.
        
        Skip line to add more details.'''
        return 2 * PI * self.radius

def main():
    circle = Circle(3)
    print(circle)
    help(circle)

if __name__ == "__main__":
    main()
    

