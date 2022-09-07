a, b = 123, 123.123
print(a + b)
print(type(a + b))
# c,d=123,"456" TypeError
# print(c+d)
# print(type(c+d))
c, d = 123, "456"
print(c + int(d))
print(type(c + int(d)))

try:
    c, d = 123, "456"
    print(c + d)
except:
    print("TypeError")
finally:
    print("Run programm")

try:
    c, d = 123, "456"
    print(c + d)
except Exception as e:
    print("Error:", e.__class__)
finally:
    print("Run programm")
