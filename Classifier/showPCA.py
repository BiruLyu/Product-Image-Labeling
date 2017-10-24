import os
from PIL import Image
from numpy import *
from pylab import *
import pickle
from scipy.cluster.vq import *
import pca




imlist = []
path = 'C:\\Users\\RubyLyu\\PycharmProjects\\untitled4\\selectedfontimages\\a_selected_thumbs\\'
imlist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]
imnbr = len(imlist)

immatrix = array([array(Image.open(im)).flatten()
                  for im in imlist],'f')

V,S,immean = pca.pca(immatrix)

with open('a_pca_modes.pkl','wb') as f:
    pickle.dump(immean,f)
    pickle.dump(V,f)

with open('a_pca_modes.pkl','rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)

immean = immean.flatten()
projected = array([dot(V[0,2],immatrix[i]-immean) for i in range(imnbr)])

projected = whiten(projected)
centroids, distortion = kmeans(projected,4)

code,distance = vq(projected, centroids)

for k in range(4):
    ind = where(code==k)[0]
    figure()
    gray()
    for i in range(minimum(len(ind),40)):
        subplot(4,10,i+1)
        imshow(immatrix[ind[i]].reshape((25,25)))
        axis('off')
show()







