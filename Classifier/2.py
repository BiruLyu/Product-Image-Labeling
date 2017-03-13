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



# imlist = []
# path = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data'
# imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
# print imlist
#
# for filename in imlist:
#     featfile = filename[:-3]+'dsift'
#     dsift. process_image_dsift(filename,featfile,10,5,resize=(200,200))
#
imlist = []
path = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\PreTaobao'
#featfile = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\TaobaoTest\\495.sift'
imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
#
for filename in imlist:
    featfile = filename[:-3]+'sift'
    sift. process_image(filename,featfile)

# features,labels = read_features_labels('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data')
#
# test_features,test_labels = read_features_labels('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\src\\data')
#
#
# k = 1
# knn_classifier = knn.KnnClassifier(labels,features)
# res = array([knn_classifier.classify(test_features[i],k) for i in range(len(test_labels))])
#
# acc = sum(1.0*(res==test_labels))/len(test_labels)
# print 'Accuracy:',acc
