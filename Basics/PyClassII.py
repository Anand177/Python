class Circle:

    def __init__(self, radius : int):
        """Initializa Radius of Circle"""
        if radius >= 0:
            self._radius = radius
            self.__diameter = 2 * radius
        else:
            ValueError("Radius should be >= 0")

    @property
    def radius(self) -> int:          # getter method. Should have same name as variable
        """Returns radius"""
        print("""Returns radius""")
        return self._radius

    @property                         # getter method. Should have same name as variable
    def diameter(self) -> int:
        """Returns Diameter"""
        """Returns Diameter"""
        return self.__diameter

    @radius.setter                    # setter method for radius variable
    def radius(self, radius):         # Same name as variable
        """Sets Radius"""
        print("Sets Radius")
        if radius >= 0:
            self._radius = radius
            self.__diameter = 2 * radius
        else:
            ValueError("Radius should be >= 1")

    @radius.setter                    # setter method for diameter variable
    def diameter(self, diameter):         # Same name as variable
        """Sets Diamater"""
        print("Sets Radius")
        if diameter >= 0:
            self._radius = diameter // 2
            self.__diameter = diameter
        else:
            ValueError("Radius should be >= 1")

    @radius.deleter
    def radius(self):
        del self._radius

c = Circle(5)
print(c.radius)
c.radius = 10

c.diameter = 20

print(c.diameter)

del c.radius

print(c.radius)