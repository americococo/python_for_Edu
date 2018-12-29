import numpy as np
def sigmoid(x):
    return 1 / (1+np.exp(-x))

def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b1'] = np.array([0.1,0.2,0.3])
    network['b2'] = np.array([0.1,0.2])
    network['b3'] = np.array([0.1,0.2])

    return network

def forward(netwrok, x):
    a1 = np.dot(x,netwrok['W1']) + netwrok['b1']
    z1 = sigmoid(a1)
    a2 = np.dot(z1,netwrok['W2']) + netwrok['b2']
    z2 = sigmoid(a2)
    a3 = np.dot(z2,netwrok['W3']) + netwrok['b3']
    y = identity_function(a3)

    return y

network = init_network()
x= np.array([1.0,0.5])
y = forward(network,x)
print(y)
