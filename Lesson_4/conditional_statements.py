a=0
if a==0:
    print('+')
if a==True:
    print('true')
else:
    print('false')
b=10 if a>1 else -1
print(b)
if b==a:
    print('=')
elif b>a:
    print('>')
else:
    print('<')
while a<10:
    a+=1
print(a)
while b<5:
    b+=1
    if b==3:
        continue
    elif b>4:
        break
    print(b)
for i in range(3):
    print("hi")