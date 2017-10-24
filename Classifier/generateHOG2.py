import os
from PIL import Image
from numpy import *
from pylab import *
import pickle
from scipy.cluster.vq import *
import pca
import dsift
import knn
import random
from svmutil import *
import vocabularyHOG
import cv2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def read_features_labels(path):
    # create list of all files ending in .dsift
    featlist = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
    # read the features
    features = []
    for featfile in featlist:
        #l,d = sift.read_features_from_file(featfile)
        hog = cv2.HOGDescriptor()
        desc = hog.compute(cv2.imread(featfile))
        iw = voc.project(desc)
        d = array(iw)
        print d
        features.append(d.flatten())
    features = array(features)

    # create labels
    # labels = []
    # for i in range(150):
    #     labels.append(0)
    # for i in range(150,400):
    #     labels.append(1)
    # for i in range(400,600):
    #     labels.append(2)

    labels = [int(featfile.split('\\')[-1][0:3])/50 for featfile in featlist]

    print labels
    return features,array(labels)


imlist = []
path = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data1'
imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
print imlist


nbr_images = len(imlist)
featlist = [imlist[i][:-3]+'jpg' for i in range(nbr_images)]

#
voc = vocabularyHOG.Vocabulary('commodity')
voc.train(featlist,3000,10)
#

# for i in featlist:
#     locs,descr = sift.read_features_from_file(featlist[0])
#     iw = voc.project(descr)
#     print len(iw),iw

with open('TaobaovocabularyHOG3000.pkl','wb') as f:
     pickle.dump(voc,f)
print 'vocabulary is:',voc.name,voc.nbr_words


with open('TaobaovocabularyHOG3000.pkl','rb') as f:
    voc = pickle.load(f)



# for i in featlist:
#     locs,descr = sift.read_features_from_file(featlist[0])
#     iw = voc.project(descr)
#     print len(iw),iw

# locs,descr = sift.read_features_from_file(featlist[0])
# iw = voc.project(descr)
#print len(iw),iw


features,labels = read_features_labels('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data1')
test_features,test_labels = read_features_labels('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data1Test')

features = map(list,features)
test_features = map(list,test_features)
prob = svm_problem(labels,features)
param = svm_parameter('-t 0')
m = svm_train(prob,param)
svm_save_model("C:\\Users\\RubyLyu\\PycharmProjects\\untitled1\\Taobao-k-svm3000-00.model",m)
res = svm_predict(labels,features,m)
# #how does it perform on the test set?
res = svm_predict(test_labels ,test_features,m)
#
# model = svm_load_model("C:\\Users\\RubyLyu\\PycharmProjects\\untitled1\\Taobao-k-svm3000.model")
# res = svm_predict(test_labels,test_features,model)
