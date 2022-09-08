def my_function_1():
    print('My function')

def my_function_2(k):
    return 5*k

def my_function_3(*args):
    print(args[2])

def my_function_4(**args):
    print(args['ok'])

def my_function_5(args='nice'):
    print('default')

def my_function_6():
    pass

def my_function_7(k):
    if(k>0):
        result = k + my_function_7(k-1)
    else:
        result = 0
    return result

my_function_1()
print(my_function_2(3))
my_function_3('A', 'B', 'C')
# my_function_3(a1='A1', a2='B3', a3='C2') dont work
my_function_4(nook='-',ok='+')
my_function_5()
my_function_6()
print(my_function_7(5))