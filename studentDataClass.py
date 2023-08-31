from dataclasses import dataclass

@dataclass
class Student: # dataclass version doesn't need to use __init__ or self at all
    name: str # variable types are declared instead of being left blank.
    collegeId: int
    gpa: float

def main():

    alice = Student('Alice', 12345, 3.71) # example Student objects created
    bob = Student('Bob', 98765, 3.13)
    john = Student('John', 32456, 2.00)
    victoria = Student('Victoria', 20512, 2.42314234)

    print(alice) # prints each example to check if the variables are there and correct.
    print(bob)
    print(john)
    print(victoria)

main()