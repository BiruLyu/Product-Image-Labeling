# Product-Image-Labeling-Using-Image-Classification
This is a repository for Biru Lyu's Undergraduate Capstone Project ***Product Image Labeling*** at East China Normal University(ECNU).

This project is come from the ***Research on Domain Ontology-Based Semi-Automatic Image Annotation Prject***. This Project is focus on the partial task that to mapping products to the classification tree and checking the project images' labeling information.

I tried to get the descriptions from images to assisting products mapping and label verification by  training for the classification model, doing some tests on it and analyzing the test results. I mainly completed the following work: 

+ Experiments
  + [Data Collection](#data-collection)
  + [Extract HoG features](#extract-hog-features)
  + [Extract SIFT features](#extract-sift-features)
  + [Extract Dense SIFT features](#extract-dsift-features)
  + [Training Classfier](#training-classifer)
  + [Fusion of multiple features](#fusion-of-mutiple-features)
+ Demo interface
  + [Flow Chart](#flow-chart)
  + [Snapshot](#snapshot)

# Experiments

In this project, I design comparative experiments by extracting different dimensions of HoG feature, SIFT feature and DSIFT feature. Then I contrast respective impacts on different data sets along with added the dimension numbers of the same feature. I also contrast the respective performance of classification on the same data set by using different kinds of features. The experimental result shows that the performance of classification on Tmall data set achieves optimization when using the DSIFT feature. The average classification accuracy is 96.1667% and the system classification accuracy is 88.4317%.	

## <a name = "data-collection"></a>Data Collection
+ Using Python's third part library **BeautifulSoup** to parse HTML only gaining some static information
+ Using **Selenium** technique to crawl 2,400 product images from [Tmall](www.tmall.com) and [Taobao](www.taobao.com). The average picture resolution is 800x800 pixels.

Built a two-layer Image Library as shown in following figure:

![](https://ws3.sinaimg.cn/large/006tNc79gy1fk28u9iypoj31kw15owsl.jpg)

## <a name = "extract-hog-features"></a>Extract HoG features



![](https://ws4.sinaimg.cn/large/006tNc79gy1fk28w8ufuij317u09qjt7.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79gy1fk28x213wxj315i0eaq7g.jpg)



## <a name = "extract-sift-features"></a>Extract SIFT features

![](https://ws4.sinaimg.cn/large/006tNc79gy1fk28zg0zp6j318609wgnl.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79gy1fk28z50whgj319s0egwic.jpg)

## <a name = "extract-dsift-features"></a>Extract Dense SIFT features

![](https://ws2.sinaimg.cn/large/006tNc79gy1fk290ia53aj317a0a8q4p.jpg)



![](https://ws2.sinaimg.cn/large/006tNc79gy1fk290nqzgnj31880ey101.jpg)

## <a name = "training-classifer"></a>Training Classifer

Using **K-Means Clustering** and **SVM** to training classifier, run the test data and compare the result.

![](https://ws3.sinaimg.cn/large/006tNc79gy1fk295d60b2j31220o80y5.jpg)

## <a name = "fusion-of-mutiple-features"></a>Fusion of multiple features

Obtain new feature to represent images by fusing HoG feature, SIFT feature and DSIFT feature. Then I contrast the respective performance of classification on the same data set by using single and multi-feature fusion feature in order to figure out  whether the system classification performance can be improved or not. The experimental result

It shows that the performance of classification on Taobao data set achieves 6% improvement when
using multi-feature fusion feature. This illustrates that multi-feature fusion feature can improve the
discrimination of different kinds of product images.


​			
​		
​	

![](https://ws4.sinaimg.cn/large/006tNc79gy1fk29chgcl6j318w0iygov.jpg)



# User Interface Design 

## <a name = "flow-chart"></a>Flow Chart

![](https://ws1.sinaimg.cn/large/006tNc79gy1fk29i6ger5j30sk0zwwhc.jpg)

## <a name = "snapshot"></a>Snapshot

### Initial Screen

![](https://ws3.sinaimg.cn/large/006tNc79gy1fk29ipqpz5j30k80gcq3m.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79gy1fk29iw08hkj30kg078mxz.jpg)

### Parameter Selection



![](https://ws3.sinaimg.cn/large/006tNc79gy1fk29jc4kclj30kk0euq4v.jpg)

### Results

![](https://ws2.sinaimg.cn/large/006tNc79gy1fk29jjwt2hj30n40da0ug.jpg)



# Conclusion

Though the research work above, the classification model with optimal performance is

selected for building Product Image Annotation System and the labels combined the information

obtained from other sources in this project are used to assist products mapping, which improves

the mapping rate of products. The labels are also used to check the product images’ annotation,

which provides greater credibility.