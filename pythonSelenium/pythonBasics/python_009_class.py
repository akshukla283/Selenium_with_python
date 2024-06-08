
class Employee:
    company = "ABC company" # class variable (always constant no matter how many objects created)

    def __init__(self, first_name, last_name):
        self.first_name = first_name # instance variable (differ by each object created)
        self.last_name = last_name
        print("I am called automatically when object is created!")

    def getData(self):
        print("I am now executing as method in class")
        print(f"First Name : {self.first_name}")
        print(f"last Name : {self.last_name}")


# syntax to create object in python
obj = Employee("Ankit", "Shukla")
obj.getData()
print(obj.company)

