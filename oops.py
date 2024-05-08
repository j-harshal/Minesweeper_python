import auth
class Car :
    Brand : "Audi"  #same for all improves space

    
    def __init__(self, fullname,marks):   #we can use name nstead of full name
        #print(self)
        self.name = fullname
        self.marks= marks
        print("Adding new cars in company")
    def rev(self):                          #cant miss self
        print("vroom vroom")
    def getmarks(self):
        return self.marks
    
    @staticmethod
    
    def say_go():                           #no need to pass self
        print("GO")


firstcar = Car("R8",10)
secondcar= Car('q3',20)


print(firstcar.name)
print(firstcar.marks)
print(secondcar.name, secondcar.marks)
firstcar.rev()
print(firstcar.getmarks())
firstcar.say_go()


auth.sayhello()