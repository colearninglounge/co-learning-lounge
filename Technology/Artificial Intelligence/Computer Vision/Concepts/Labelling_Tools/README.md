# labelling tools (computer vision)

Image labelling is one of the tedious tasks to do after collecting data for Computer Vision tasks. To make the process faster and smooth select the labelling tool of your comfort.

Tools avaliable for labelling:

*   LabelME
*   CVAT
*   makesense.ai
*   VGG Image Annotator (VIA)

### labelme

Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation). 

you can install it by using pip:

`pip install labelme`

<p align="center"> 
    <img width="600" src="https://raw.githubusercontent.com/wkentaro/labelme/master/examples/instance_segmentation/.readme/annotation.jpg" alt="Logo">
</p>



[source code](https://github.com/wkentaro/labelme)

**Usage details**

```shell
Run labelme --help for detail.
The annotations are saved as a JSON file.

labelme  # just open gui

# tutorial (single image example)
cd examples/tutorial
labelme apc2016_obj3.jpg  # specify image file
labelme apc2016_obj3.jpg -O apc2016_obj3.json  # close window after the save
labelme apc2016_obj3.jpg --nodata  # not include image data but relative image path in JSON file
labelme apc2016_obj3.jpg \
  --labels highland_6539_self_stick_notes,mead_index_cards,kong_air_dog_squeakair_tennis_ball  # specify label list

# semantic segmentation example
cd examples/semantic_segmentation
labelme data_annotated/  # Open directory to annotate all images in it
labelme data_annotated/ --labels labels.txt  # specify label list with a file
```
---


### Computer Vision Annotation Tool (CVAT)

CVAT is free, online, interactive video and image annotation tool for  computer vision. It is being used by our team to annotate million of  objects with different properties. Many UI and UX decisions are based on feedbacks from professional data annotation team.

<p align="center"> 
    <img width="600" src="https://github.com/opencv/cvat/raw/develop/cvat/apps/documentation/static/documentation/images/cvat.jpg" alt="Logo">
</p>



For installation and usage details visit this page : [link](https://github.com/opencv/cvat)

---

### makesense.ai

<p align="center"> 
    <img width="600" src="https://github.com/SkalskiP/make-sense/raw/develop/public/img/main-image-dark_alter.png" alt="Logo">
</p>

[makesense.ai](https://www.makesense.ai/) is a free to use online tool for labelling photos. Thanks to the use of a browser it does not require any complicated installation - just visit the website and you are ready to go. It also doesn't matter which operating system you're running on - we do our best to be truly cross-platform. It is perfect for small computer vision deeplearning projects, making the process of preparing a dataset much easier and faster. Prepared labels can be downloaded  in one of multiple supported formats. The application was written in TypeScript and is based on React/Redux duo.

---

### VGG IMAGE ANNOTATOR 

VGG Image Annotator is a simple and standalone manual annotation software for image, audio and video. VIA runs in a web browser and does not require any installation or setup. The complete VIA software fits in a single self-contained  HTML page of size less than 400 Kilobyte that runs as an offline application in  most modern web browsers.

<p align="center"> 
    <img width="600" src="http://www.robots.ox.ac.uk/~vgg/software/via/images/via_demo_screenshot2_via-2.0.2.jpg" alt="Logo">
</p>



No Installation Needed just go through these below links

* [via_image_annotator.html](http://www.robots.ox.ac.uk/~vgg/software/via/app/via_image_annotator.html) : online copy (< 400KB)
* [via_video_annotator.html](http://www.robots.ox.ac.uk/~vgg/software/via/app/via_video_annotator.html) : online copy (< 400KB)
* [via_audio_annotator.html](http://www.robots.ox.ac.uk/~vgg/software/via/app/via_audio_annotator.html) : online copy (< 400KB)



For more details go through this [link](http://www.robots.ox.ac.uk/~vgg/software/via/)

