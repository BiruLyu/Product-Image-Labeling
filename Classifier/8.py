import os
from PIL import Image
from numpy import *
from pylab import *
import pickle
from scipy.cluster.vq import *
import pca
import dsift
import sift
import knn
from svmutil import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def read_features_labels(path):
    # create list of all files ending in .dsift
    featlist = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.dsift')]
    # read the features
    features = []
    for featfile in featlist:
        l,d = sift.read_features_from_file(featfile)
        features.append(d.flatten())
    features = array(features)

    # create labels
    labels = [int(featfile.split('\\')[-1][0:3])/50 for featfile in featlist]
    return features,array(labels)



imlist = []
path = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data'
imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
print imlist

for filename in imlist:
   featfile = filename[:-3]+'dsift'
   dsift.process_image_dsift(filename,featfile,10,5,resize=(150,200))

imlist = []
path = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\src\\data'
imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

for filename in imlist:
   featfile = filename[:-3]+'dsift'
   dsift.process_image_dsift(filename,featfile,10,5,resize=(150,200))

features,labels = read_features_labels('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data')

#print features
test_features,test_labels = read_features_labels('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\src\\data')

features = map(list,features)
test_features = map(list,test_features)
prob = svm_problem(labels,features)
param = svm_parameter('-t 2')
m = svm_train(prob,param)
svm_save_model("C:\\Users\\RubyLyu\\PycharmProjects\\untitled1\\svmDsift200.model",m)
res = svm_predict(labels,features,m)
res = svm_predict(test_labels,test_features,m)
#how does it perform on the test set?
# m = svm_load_model("C:\\Users\\RubyLyu\\PycharmProjects\\untitled1\\svmDsift.model")
#
# res = svm_predict(test_labels[:5],test_features[:5],m)