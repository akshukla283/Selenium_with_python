
class Calculator:
    num = 100
    # if here no constractor then default constructor execute
    def __init__(self):
        print("I am called automatically when object is created!")
    def getData(self):
        print("I am now executing as method in class")


# syntax to create object in python
obj = Calculator()
obj.getData()
print(obj.num)

