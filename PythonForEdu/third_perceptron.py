import numpy



#def AND(x1,x2):
#    w1,w2,theta=0.5,0.5,0.7
#    tmp = x1 * w1 + x2 * w2
#    if tmp <= theta:
#        return 0
#    elif tmp > theta:
#        return 1

#print(AND(1,1))

def perceptron_basic_calc(x,w,b):

    tmp = numpy.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1


def AND_New(x1,x2):
    x = numpy.array([x1,x2])
    w = numpy.array([0.5,0.5])
    b = -0.7

    return perceptron_basic_calc(x,w,b)
    

def NAND(x1,x2):
    x = numpy.array([x1,x2])
    w = numpy.array([-0.5,-0.5])
    b = 0.7

    return perceptron_basic_calc(x,w,b)

def OR(x1,x2):
    x = numpy.array([x1,x2])
    w = numpy.array([0.5,0.5])
    b = -0.1

    return perceptron_basic_calc(x,w,b)

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)

    return AND_New(s1,s2)

a, b = input('input x1 and x2>').split()
a=int(a)
b=int(b)
print(AND_New(a,b))
print(NAND(a,b))
print(OR(a,b))