import random

def genIntArray(size : int, maxValue) -> list[int]:

    arr = [random.randint(1, maxValue),]

    for i in range(size-1):
        arr.append(random.randint(1, maxValue))
    return arr


if __name__ == "__main__":
    print(genIntArray(5, 100))