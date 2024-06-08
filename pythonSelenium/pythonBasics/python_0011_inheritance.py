from pythonBasics.python_009_class import Employee
class ChildImp(Employee):
    child_cmp = "XYZ company"
    # note check if there is constructor in your parent class then create constructor here as well
    # and pass the instance variable
    def __init__(self, est_year):
        Employee.__init__(self, first_name="Ankit", last_name="Shukla")
        self.esr_year = est_year

    def get_complete_data(self):
        return f"Parent company : {self.company}\nChild company: {self.child_cmp}\nEstablished in year: {self.esr_year}"
        # we can see that parent class company name accessible here



# if you have already passed instance variable of you parent class then
# while creating child class obj just pass child class instance variable
obj = ChildImp(est_year=2010)
print(obj.get_complete_data())