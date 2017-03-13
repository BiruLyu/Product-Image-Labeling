from numpy.random import randn
import pickle
from pylab import *

n = 200

class_1 = 0.6 * randn(n,2)
class_2 = 1.2 * randn(n,2) + array([5,1])
labels = hstack((ones(n),-ones(n)))


with open('points_normal_test.pkl','w') as f:
    pickle.dump(class_1,f)
    pickle.dump(class_2,f)
    pickle.dump(labels,f)

class_1 = 0.6 * randn(n,2)
r = 0.8 * randn(n,1) +5
angle = 2 * pi * randn(n,1)
class_2 = hstack((r*cos(angle),r*sin(angle)))
labels = hstack((ones(n),-ones(n)))


with open('points_ring_test.pkl','w') as f:
    pickle.dump(class_1,f)
    pickle.dump(class_2,f)
    pickle.dump(labels,f)


import knn
import imtools

with open('points_normal.pkl','r') as f:
    class_1 = pickle.load(f)
    class_2 = pickle.load(f)
    labels = pickle.load(f)

model = knn.KnnClassifier(labels,vstack((class_1,class_2)))

with open('points_normal_test.pkl','r') as f:
    class_1 = pickle.load(f)
    class_2 = pickle.load(f)
    labels = pickle.load(f)

print model.classify(class_2[0])