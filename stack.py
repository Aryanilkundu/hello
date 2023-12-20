stack=[]
def push():
    x=input('enter the element: ')
    stack.append(x)
    print(stack)

def pop():
    if len(stack)==0:
        print('stack is empty!')
    else:
        e=stack.pop()
        print(f'the popped element is {e}')
        print(stack)

while True:
    r=int(input("Select the opeartion: 1.push, 2.pop ,3.quit"))
    if r==1:
        push()
    elif r==2:
        pop()
    elif r==3:
        print('fuck off')
        break
    else:
        print('good bye')
    
    
    
    