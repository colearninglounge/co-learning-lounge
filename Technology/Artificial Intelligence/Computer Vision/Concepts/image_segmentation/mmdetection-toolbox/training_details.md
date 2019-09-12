## training your own data

* You can use lableme/CVAT tool for labelling the data to get annotations as  COCO format.
* For conversion of labelme annotations to COCO format, use [labelme2coco.py](https://github.com/Tony607/labelme2coco/blob/master/labelme2coco.py) script.
use command `python labelme2coco.py images_folder`
* for CVAT tool you can directly dump COCO format.

Place your dataset under  `$MMDETECTION/data`. If your folder structure is different, you may need to change the corresponding paths in config files.

```
mmdetection
├── mmdet
├── tools
├── configs
├── data  
│   ├── annotations
│   ├── train2017
│   ├── val2017
│   ├── test2017
```

* you need to put the annotation file obtained by labelling the dataset inside the "annotations" folder.
* place train data under train2017, test under test2017, and validation data under val2017 folders.


### Training Modifications:
The configuration that needs to be modified for training is:

`tools/train.py`
Modify the configuration file; change the config and other required arg --to optional configuration, avoid typing long commands every time.

`configs/xxx.py`
`#dataset settings` The code segment part, including: `dataset_type`, `data_root`, and the training set, test set , verification set , under the data dictionary `ann_file`, `img_prefix`;

`checkpoint_config` the interval is the number of rounds saved by the model;
`log_config` setting the number of iterations of the training log record and the recording mode;
`total_epochs`recording the total number of training rounds
mmdet/datasets/my_dataset/py(op)
Select configuration based on the data set, see the section on training your own data set later.

```python
data = dict(
    imgs_per_gpu=4,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/instances_train2017.json',
        img_prefix=data_root + 'train2017/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/instances_val2017.json',
        img_prefix=data_root + 'val2017/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/instances_val2017.json',
        img_prefix=data_root + 'val2017/',
        pipeline=test_pipeline))
# optimizer
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=1.0 / 3,
    step=[8, 11])
checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
evaluation = dict(interval=1)
# runtime settings
total_epochs = 120
```


Also change lr=0.005, if you use only single gpu.

* I have used config `mask_rcnn_r101_fpn_1x.py` for training ,
![enter image description here](https://i.ibb.co/HBhPVBz/1-2.png)

* result i got after training for 120 epochs :

![enter image description here](https://i.ibb.co/kQV6zgw/photo6327646245295859993.jpg)
