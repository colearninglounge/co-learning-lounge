# Object detection + Image segmentation using mmdetection toolbox



![1](https://github.com/ash11sh/image-segmentation-mmdetection/raw/master/images/1.png)


### Comparison of different visual recognition tasks in computer vision.

(a) “Image Classification” only needs to assign categorical class labels to the image.

(b) “Object detection” not only predict categorical labels but also localise each object instance via bounding boxes.

 (c) “Semantic segmentation” aims to predict categorical labels for each pixel, without differentiating object
instances. 

(d) “Instance segmentation”, a special setting of object detection, differentiates different object instances by pixel-level segmentation masks.



### mmdetection toolbox installation



![demo image](https://github.com/open-mmlab/mmdetection/raw/master/demo/coco_test_12510.jpg)



- The toolbox directly supports popular and contemporary detection frameworks, *e.g.* Faster RCNN, Mask RCNN, RetinaNet, etc.
- Create a conda virtual environment and activate it.

```
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab
```



- Install PyTorch stable or nightly and torchvision following the [official instructions](https://pytorch.org/), e.g.,

```
conda install pytorch torchvision -c pytorch
```



- Clone the mmdetection repository.

```
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
```



- install required dependencies via  

```
pip install -r requirements.txt
```



- Install mmdetection (other dependencies will be installed automatically).

```
python setup.py develop
# or "pip install -v -e ."
```





### Dataset preparation

It is recommended to symlink the dataset root to `$MMDETECTION/data`. If your folder structure is different, you may need to change the corresponding paths in config files.

```
mmdetection
├── mmdet
├── tools
├── configs
├── data
│   ├── project_name
│   │   ├── trainval.json
│   │   ├── training_images


```



- For labelling you can use tools like CVAT, labelme , labelbox.
- Personally i have used CVAT & labelme. CVAT installation is bit tedious process.
- Annotation file should be in COCO format.
- For conversion of labelme annotation files to COCO format you  can use this python script - [link](https://github.com/wkentaro/labelme/blob/master/examples/instance_segmentation/labelme2coco.py) 



### Training the model

- For segmentation task select (mask-RCNN/cascade mask-RCNN) configuration files.

- You need to update the configuration file with paths of dataset and annotations, before proceeding to training.

- All outputs (log files and checkpoints) will be saved to the working directory, which is specified by `work_dir` in the config file.

- If you are using only one GPU, learning rate and batch-size should be set accordingly.

  

  ***Important\***: The default learning rate in config files is for 8 GPUs and 2 img/gpu (batch size = 8*2 = 16). According to the [Linear Scaling Rule](https://arxiv.org/abs/1706.02677), you need to set the learning rate proportional to the batch size if you use different GPUs or images per GPU, e.g., lr=0.01 for 4 GPUs * 2 img/gpu and lr=0.08 for 16 GPUs * 4 img/gpu.

  

##### Train with a single GPU

```
python tools/train.py ${CONFIG_FILE}
```

If you want to specify the working directory in the command, you can add an argument `--work_dir ${YOUR_WORK_DIR}`.



##### Train with multiple GPUs

```
./tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM} [optional arguments]
```

Optional arguments are:

- `--validate` (**strongly recommended**): Perform evaluation at every k (default value is 1, which can be modified like [this](https://github.com/open-mmlab/mmdetection/blob/master/configs/mask_rcnn_r50_fpn_1x.py#L174)) epochs during the training.
- `--work_dir ${WORK_DIR}`: Override the working directory specified in the config file.
- `--resume_from ${CHECKPOINT_FILE}`: Resume from a previous checkpoint file.

Difference between `resume_from` and `load_from`: `resume_from` loads both the model weights and optimizer status, and the epoch is also inherited from the specified checkpoint. It is usually used for resuming the training process that is interrupted accidentally. `load_from` only loads the model weights and the training epoch starts from 0. It is usually used for finetuning.



***NOTE\***:  for more information about training details go through this [link](https://github.com/open-mmlab/mmdetection/blob/master/docs/GETTING_STARTED.md).



### Inference demo 

For image:

```python
from mmdet.apis import init_detector, inference_detector, show_result
import mmcv

config_file = 'configs/faster_rcnn_r50_fpn_1x.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = 'test.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
# visualize the results in a new window
show_result(img, result, model.CLASSES)
# or save the visualization results to image files
show_result(img, result, model.CLASSES, out_file='result.jpg')
```



For video:

```python
from mmdet.apis import init_detector, inference_detector, show_result
import mmcv

config_file = 'configs/faster_rcnn_r50_fpn_1x.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a video and show the results
video = mmcv.VideoReader('video.mp4')
for frame in video:
    result = inference_detector(model, frame)
    show_result(frame, result, model.CLASSES, wait_time=1)
```



### Training and Inference using google colab

- If you want to train the model in google colab, go through this link and start training.
- Upload your data and trainval.json to google drive



colab link for training  : https://colab.research.google.com/drive/1A7hb3enCzuo0j8fTxLenIxaC6bCNJ5Qm
