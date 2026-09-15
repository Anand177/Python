class Math:

    @staticmethod           # Static method, can't access any class attribute
    def add5(x: int) -> int:
        return x+5

    @staticmethod
    def add5(x: float) -> float:
        return x+5.0


print(Math.add5(10))
print(Math.add5(10.3))