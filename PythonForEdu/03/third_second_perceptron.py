import numpy
import matplotlib.pyplot as plt


#활성화 함수
def step_function(x):
    #y = x > 0
    #return y.astype(numpy.int)
    return numpy.array(x>0, dtype= numpy.int)

#시그모이드 함수
def sigmoid(x):
    return 1 / (1+numpy.exp(-x))


x = numpy.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)

print(sigmoid(x))

y = sigmoid(x)
plt.plot(x,y,linestyle="--")
plt.ylim(-0.1,1.1)

plt.show()



#ReLu함수
def Relu(x):
    return numpy.maximum(0,x)


