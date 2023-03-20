def plus(x , y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):

    return x / y 

ops = {
    '+': plus,
    '-': minus,
    '/': division,
    '*': multiply
}

input_action = input("Write your operation: ")
num_1, operation, num_2 = input_action.split()
    
print(ops[operation](float(num_2), float(num_2)))