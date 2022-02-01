class Teacher:
    def __init__(self,name,age):
        self.firstname = name
        self.age1 = age

    def stud1(self):
        pass
    def stud2(self):
        print("The firstname is:" + self.firstname)
        #print("The age is {}" . format(self.age1))
    def stud3(self):
        print("The age is {}".format(self.age1))

#obj1 = Teacher("Amma",16)
#obj1.firstname = "Archana"
#obj1.age1 = 38
#obj1.stud2()

class Student(Teacher):
    def __init__(self, name ,age, dob):
        #Teacher.__init__(self,name,age)
        super().__init__(name,age) #Self is not required
        self.dob = dob

    def stud4(self):
        print(self.dob)
        print("my dob is " + self.dob)

obj_child = Student("Shau", 6, "2/12/983")
obj_child.stud2()
obj_child.stud3()
obj_child.stud4()








#Check attributes are present or no..returns : T/F
#print(hasattr(obj1, 'age1'))







class fruits:
    pass