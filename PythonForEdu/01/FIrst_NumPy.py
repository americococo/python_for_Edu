import numpy as np

x= np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])

#원소별 계산
print('x:{} y:{}'.format(x,y))

print('x+y')
print(x+y)

print('x-y')
print(x-y)

print('x*y')
print(x*y)

print('x/y')
print(x/y)

type(x)

#2차원 배열
print()
print('##########')
A = np.array([[1,2],[3,4]])
B = np.array([[3,0],[0,6]])

print(A)
print(B)
#배열에 형태를 출력
print(A.shape)

#행렬에 담긴 원소의 자료형을 확인
print(A.dtype)

print('A+b')
print(A+B)

print('A*b')
print(A*B)
print('##########')
print()
#브로드캐스트
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)
#[1 2] # * [10 20] = [1 2] * [10 20] = [10 40]
#[3 4]             = [3 4] * [10 20] = [30 80]

#원소접근
print()
print('##########')
x = np.array([[51,55],[14,19],[0,4]])
print(x)
print(x[0])#[51,55]
print(x[0][1])#[55]

for value in x:
    print(value)

x = x.flatten() #평탄화
print(x)

print('##########')
print()
print(x>15)
print(x[x>15]) #값이 15이상인 원소들

