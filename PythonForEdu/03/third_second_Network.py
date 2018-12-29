import numpy


def sigmoid(x):
    return 1 / (1+numpy.exp(-x))

#행렬 곱
#x = numpy.array([1,2])
#print(x)

#w= numpy.array([[1,3,5],[2,4,6]])

#print(w)

#y = numpy.dot(x,w)
#print(y)



x  =    numpy.array([1.0,0.5])
w1 =    numpy.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b1 =    numpy.array([0.1,0.2,0.3])

print(w1.shape)
print(x.shape)
print(b1.shape)
A1 = numpy.dot(x,w1) + b1

z1 = sigmoid(A1)#활성화

print(A1)
print(z1)

w2 = numpy.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
b2 = numpy.array([0.1,0.2])

print(z1.shape)
print(w2.shape)
print(b2.shape)

A2 = numpy.dot(z1,w2) + b2
z2 = sigmoid(A2)#활성화

w3 = numpy.array([[0.1,0.3],[0.2,0.4]])
b3 = numpy.array([0.1,0.2])

A3 = numpy.dot(z2,w3 ) + b3
Y = A3