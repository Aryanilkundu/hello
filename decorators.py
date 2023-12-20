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
