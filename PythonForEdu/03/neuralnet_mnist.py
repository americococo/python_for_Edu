import sys, os
import numpy as np
import pickle
from mnist import load_mnist

#시그모이드 함수
def sigmoid(x):
    return 1 / (1+np.exp(-x))

#소프트 맥스
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/ sum_exp_a
    
    return y


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    dataset_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(dataset_dir + "/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()

batch_size=1000 #배치 (묶음) 크기
accuracy_cnt = 0

for i in range(0,len(x),batch_size):
    x_batch = x[i:i+batch_size]#100장씩 묶어서 커냄

    y_batch = predict(network,x_batch)
    p= np.argmax(y_batch,axis=1) # 가장 첫번째 차원에서 최대값의 인덱스값을 찾도록함

    accuracy_cnt += np.sum(p==t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
