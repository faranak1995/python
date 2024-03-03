#Definition of the superclass starts here
class Person:
    #Initializing the variables
    name = ""
    age = 0
    #Definding constractor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    
    #Defining class methods
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)
    #End of superclass definition
    
#Definintion of subclass starts here
class Student(Person):
    #Person is the superclass and Student is the subclass
    studentId = ""
        
    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName, studentAge)
        #Calling the superclass constractor and sending values of attributes.
        self.studentId = studentId
            
    def getId(self):
        return self.studentId
    #returns the value of student id
    #End of subclass definition
        
#Create an object of the superclass
person1 = Person("John", 23)
#Call member methods of the objects
person1.showAge()

#Create an object of the subclass
student1 = Student("Shaun", 22, "102")
print(student1.getId())
student1.showName()
