from pythonBasics.python_009_class import Employee


class ChildImp(Employee):
    child_cmp = "XYZ company"
    def get_complete_data(self):
        return f"Parent company : {self.company}\nChild company: {self.child_cmp}"
        # we can see that parent class company name accessible here



# need to pass parent class instance variable and
# child class if there is instance variable
# this is one method
obj = ChildImp(first_name="Ankit", last_name="Shukla")
print(obj.get_complete_data())