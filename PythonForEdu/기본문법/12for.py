patterns = ['가위','바위','보']
for pattern in patterns: #patterns 반복할 개체 #pattern 대입
    print(pattern)

#for i in [0,1,2,3,4]:
for i in range(10):
    print(i,end=' ')

print()

a = ['a','b','c','d']

for i in range(len(a)):
    character = a[i]
    print('No.{} : {}'.format(i+1,a[i]))
print()
for i,name in enumerate(a):
    print('No.{} : {}'.format(i+1,a[i]))

for i in range(11172):
    print(chr(44032+i),end=' ')