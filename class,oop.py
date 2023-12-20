class Person:
    def __init__(self):
        print('hey i am a person')
    name='aryanil'
    occupation='student'
    networth=5000
    def info(self):
        print(f'{self.name} is a {self.occupation}')
b=Person()
print(b)

class PythonProgrammer:
    def __init__(self, fullname, height, age):
        self.fa = fullname
        self.height = height
        self.age = age
    def show(self):
        print(self.fa)
PP = PythonProgrammer("Guido van Rossum", 5.6, 67)
PP.show()

class hello:
    def __init__(self,a,b,c):
        self.name=a
        self.occupation=b
        self.city=c
    def aryanil(self):
        print(f'{self.name} who is a {self.occupation} lives in {self.city}')
person1=hello('aryanil','student','howrah')
print(person1.aryanil())
print(hello(1, 2,3).aryanil())


class PythonProgrammer:
    def __init__(self, fullname):
        self.fullname = fullname
        print(fullname)
        # We cannot write return(self.fullname) here
    def include(self, height):
        self.height = height
        return(self.height)
    def send(self):
        return(self.fullname)
PP = PythonProgrammer("Guido van Rossum")
print(PP.send())
print(PP.include(5.6))

def greet(f):
    def mf(*args,**kwargs):
        print('good morning')
        f(*args,**kwargs)
        print('good bye')
    return mf
   
def helllo1():
    print('hello world')
helllo1()
greet(helllo1)()
@greet
def hello2(a,b):
    print(a+b)
hello2(2,3)
    



























