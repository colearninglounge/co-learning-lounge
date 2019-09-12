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

Before that, you need to setup the installed environment for running the scripts. 

### Installation

#### Requirements

- Linux (Windows is not officially supported)
- Python 3.5+ (Python 2 is not supported)
- PyTorch 1.1 or higher
- CUDA 9.0 or higher
- NCCL 2
- GCC(G++) 4.9 or higher
- [mmcv](https://github.com/open-mmlab/mmcv)

We have tested the following versions of OS and softwares:

- OS: Ubuntu 16.04/18.04 and CentOS 7.2
- CUDA: 9.0/9.2/10.0
- NCCL: 2.1.15/2.2.13/2.3.7/2.4.2
- GCC(G++): 4.9/5.3/5.4/7.3

#### Install mmdetection

a. Create a conda virtual environment and activate it.

```shell
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab
```

b. Install PyTorch stable or nightly and torchvision following the [official instructions](https://pytorch.org/), e.g.,

```shell
conda install pytorch torchvision -c pytorch
```

c. Clone the mmdetection repository.

```shell
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
```

d. Install mmdetection (other dependencies will be installed automatically).

```shell
python setup.py develop
# or "pip install -v -e ."
```

#### for demo: 
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



#### For training on your own dataset, go through this link
