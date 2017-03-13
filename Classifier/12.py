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
import PreProcess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

imlist = []
path = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\Taobao\\'
result = 'C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\PreTaobao\\'
imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
#
for filename in imlist:
    print filename
    name = filename.split('\\')[-1]
    resultname = result + name
    PreProcess.pre_process_image(filename,resultname)
