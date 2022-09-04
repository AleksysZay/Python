def print_value_and_type(variable): #funk for print value and datatype variables
    print("variable: {v:50} type: {t:10}".format(v=str(variable), t=str(type(variable))))

a = b = c = 100 #multiple assignment
print(a, b, c)

a, b, c = 1, 2, 'hello' #sequence assignment
print(a, b, c)

variable_str = 'string'
print_value_and_type(variable_str)

variable_int = 1
print_value_and_type(variable_int)

variable_float = 3.14
print_value_and_type(variable_float)

variable_complex = 1j
print_value_and_type(variable_complex)

variable_list = [1, 2, 3]
print_value_and_type(variable_list)

variable_tuple = (1, 2, 3)
print_value_and_type(variable_tuple)

variable_range = range(6)
print_value_and_type(variable_range)

variable_dict = {"name": "Aleksey", "age": 18}
print_value_and_type(variable_dict)

variable_set = {1, 2, 3}
print_value_and_type(variable_set)

variable_frozenset = frozenset({1, 2, 3})
print_value_and_type(variable_frozenset)

variable_bool = True
print_value_and_type(variable_bool)

variable_bytes = b"Hello"
print_value_and_type(variable_bytes)

variable_bytearray = bytearray(5)
print_value_and_type(variable_bytearray)

variable_mem = memoryview(bytes(5))
print_value_and_type(variable_mem)

variable_none = None
print_value_and_type(variable_none)
