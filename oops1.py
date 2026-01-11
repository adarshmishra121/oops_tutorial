# initiate a class
class employee:
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        #print("Constructor called - Object is being created")
        self.id = 123
        self.salary = 10000
        self.designation = "sde"
        #print("Constructor called - Object has been created")

    def travel(self, destination):
        #print("this travel method is called manually")
        print(f"Employee is traveling to {destination}")    

# create an object/instance of the class
sam = employee()
#printing the attributes
print(sam.designation)
print(sam.id)
# calling the method
sam.travel("Bangalore")
