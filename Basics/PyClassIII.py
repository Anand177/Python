from dataclasses import dataclass
from typing import ClassVar

@dataclass      # Creates Boiler plate class methods automatically
class Point:
    x : int = 0 # Default parm in dataclass
    y : int = 0
    num_of_points : ClassVar[int] = 0   # Class variable

p = Point(x = 3, y =3) # __init__ automatically created
print(p)                # __repr__ invoked  . Both these methods are auto generated 
print(p == Point(1,2))  # __eq__ invoked
print(p == Point(3,3))