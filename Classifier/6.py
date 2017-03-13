from scipy.ndimage import measurements
import os
from pylab import *
from PIL import Image
from scipy.misc import imread, imsave, imresize
from svmutil import *
import imtools
import cv2
import numpy as np


os.chdir("C:\Users\RubyLyu\libsvm-3.21\python")


def compute_feature(im):
    norm_im = imresize(im,(200,200))
    norm_im = norm_im[20:-20,20:-20]

    return norm_im.flatten()

def load_ocr_data(path):
    imlist = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

    labels = [int(imfile.split('\\')[-1][0:3])/50 for imfile in imlist]

    features = []
    for imname in imlist:
        im = array(Image.open(imname).convert('L'))
        #im = array(Image.open(imname).convert('L'))
        features.append(compute_feature(im))

    return array(features),labels



#features,labels = load_ocr_data()
# TRAINING DATA
features,labels = load_ocr_data("C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\data") # TESTING DATA
test_features,test_labels = load_ocr_data("C:\\Users\\RubyLyu\PycharmProjects\\PictureDB\\src\\data")
# train a linear SVM classifier
features = map(list,features)
#print features
#raw_input()
test_features = map(list,test_features)
prob = svm_problem(labels,features)
param = svm_parameter('-t 0')
m = svm_train(prob,param) # how did the training do?
svm_save_model("C:\\Users\\RubyLyu\\PycharmProjects\\untitled1\\svmNone.model",m)
res = svm_predict(labels,features,m)
# how does it perform on the test set?
res = svm_predict(test_labels,test_features,m)

print res[0][596]
#ACC, MSE, SCC = evaluations(test_features[0],test_labels[0])