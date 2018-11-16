# TFannotations2TC
Convert a TensorFlow annotations csv file into a Turi Create annotations csv file

## Overview 

If you are using the [TensorFlow Framework](https://www.tensorflow.org) for `Object Detection`, you must be familiar with an annotiations csv file that looks like:

```
filename,width,height,class,xmin,ymin,xmax,ymax
1.jpg,2048,1251,waldo,706,513,743,562
2.jpg,1600,980,waldo,715,157,733,181
3.jpg,2828,1828,waldo,460,1530,482,1557
4.jpg,1276,1754,waldo,846,517,878,563
5.jpg,1280,864,waldo,932,274,942,288
```

Howerver, if you are using the [Turi Create Framework](https://github.com/apple/turicreate) for `Object Detection`, this file looks like:

```
path,annotations
1.jpg,[{"coordinates": {"height": 49, "width": 37, "x": 724, "y": 537}, "label": "waldo"}]
2.jpg,[{"coordinates": {"height": 24, "width": 18, "x": 724, "y": 169}, "label": "waldo"}]
3.jpg,[{"coordinates": {"height": 27, "width": 22, "x": 471, "y": 1543}, "label": "waldo"}]
4.jpg,[{"coordinates": {"height": 46, "width": 32, "x": 862, "y": 540}, "label": "waldo"}]
5.jpg,[{"coordinates": {"height": 14, "width": 10, "x": 937, "y": 281}, "label": "waldo"}]
```

The purpose of this Python script is to convert the TensorFlow cvs file into a Turi Create one.

## Usage

As simple as the script is, just run the following command:

```shell
$ python TFAnnotation2TC.py TensorFlow_annotations_file.csv TuriCreate_annotations_file.csv
```

When the convertion is complete, you must get the following message prompted in the console:
``` 
    Processed 43 lines.
```
    
## Contact
If you have a question or any comment, feel free to open an issue or to DM me on [@florianldt](https://twitter.com/florianldt).
