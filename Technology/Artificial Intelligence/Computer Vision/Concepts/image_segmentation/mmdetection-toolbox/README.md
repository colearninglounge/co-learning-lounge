# mmdetection toolbox

If you are already into object detection/segmentation, may know about *mmdetection*. This is built on top of Pytorch by [Multimedia Laboratory, CUHK](http://mmlab.ie.cuhk.edu.hk/). The toolbox started from a codebase of MMDet team who won the detection track of COCO Challenge 2018. . It gradually evolves into a unified platform that covers many popular detection methods and contemporary modules. It not only includes training and inference codes, but also provides weights for more than 200 network models. As per now, this toolbox is by far the most complete detection toolbox (SOTA).

##  Supported Frameworks

-   Single-stage detector  
    SSD, RetinaNet, FCOS, FSAF  
    
-   Two-stage detectors  
    Faster R-CNN, R-FCN, Mask R-CNN, Mask Scoring R-CNN, Grid R-CNN  
    
-   Multi-stage detector  
    Cascade R-CNN, Hybrid Task Cascade  
    
-   General modules and methods  
    soft-NMS, DCN, OHEN, Train from Scratch, M2Det, GN, HRNet, Libra R-CNN  
    

  github address : [https://github.com/open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection)
  paper link : [https://arxiv.org/pdf/1906.07155.pdf](https://arxiv.org/pdf/1906.07155.pdf)
  
## Quick demo

Before that, you need to setup the mmdetection environment for running the scripts. 

for insallation go through this [link](https://github.com/colearninglounge/co-learning-lounge/blob/master/Technology/Artificial%20Intelligence/Computer%20Vision/Concepts/image_segmentation/mmdetection-toolbox/blob/master/installation.md)

* go through demo/inference_demo.ipynb file.
* set the configuration file as your requirement.
* download the checkpoint from [model zoo](https://github.com/open-mmlab/mmdetection/blob/master/docs/MODEL_ZOO.md) and put it in `checkpoints/`


  

```python
from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
```


```python
config_file = '../configs/faster_rcnn_r50_fpn_1x.py'
# download the checkpoint from model zoo and put it in `checkpoints/`
checkpoint_file = '../checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'
```


```python
# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')
```


```python
# test a single image
img = 'demo.jpg'
result = inference_detector(model, img)
```


```python
# show the results
show_result_pyplot(img, result, model.CLASSES)
```


![png](https://i.ibb.co/LCfxvkQ/output-4-0.png)



#### For details of training on your own dataset, go through this [link](https://github.com/colearninglounge/co-learning-lounge/blob/master/Technology/Artificial%20Intelligence/Computer%20Vision/Concepts/image_segmentation/mmdetection-toolbox/blob/master/training_details.md)
