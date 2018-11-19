from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET
import mxnet as mx
import numpy as np
import pandas as pd
import math
def toxml(filepath,id,x,y,w,h,label):

    root = Element('annotation')

    folder = SubElement(root, "folder")
    folder.text = filepath[:-12]

    filename=SubElement(root, "filename")
    filename.text=id

    path = SubElement(root, "path")
    path.text = folder.text +"/anno_folder"+ "/{}.xml".format(id)

    size=SubElement(root, "size")
    width = SubElement(size, "width")
    width.text="512"
    height = SubElement(size, "height")
    height.text="512"

    object=SubElement(root, "object")
    name = SubElement(object, "name")
    name.text = label

    difficult=SubElement(object, "difficult")
    difficult.text="0"
    position=x+w/2

    bndbox = SubElement(object, "bndbox")
    xmin = SubElement(bndbox, "xmin")
    xmax = SubElement(bndbox, "xmax")
    ymin = SubElement(bndbox, "ymin")
    ymax = SubElement(bndbox, "ymax")
    pos = SubElement(bndbox, "pos")
    if position<=512:
        pos.text='left'
        xmin.text=str(x)
        xmax.text=str(min(510,(x+w)))
        ymin.text=str(max(5,y-256))
        ymax.text=str(min(y+h-256,510))
    else:
        pos.text='right'
        xmin.text=str(max(5,x-512))
        xmax.text=str((x+w)-512)
        ymin.text=str(max(5,y-256))
        ymax.text=str(min(y+h-256,510))
    # xmin = SubElement(bndbox, "xmin")
    # xmin.text=str(x/2)
    # xmax = SubElement(bndbox, "xmax")
    # xmax.text=str((x+w)/2)
    # ymin = SubElement(bndbox, "ymin")
    # ymin.text=str(y/2)
    # ymax = SubElement(bndbox, "ymax")
    # ymax.text=str((y+h)/2)

    tree = ET.ElementTree(root)
    tree.write(filepath+"/"+id+".xml")



if __name__=="__main__":

    path="/Users/yanxinzhou/course/kaggle/agriculture/data/rsna/data/train/anno_folder"
    df=pd.DataFrame.from_csv(path+"/train.csv",header=0)
    df=df.fillna(0)
    for idx,row in df.iterrows():
        toxml(path, idx, row[0], row[1], row[2],row[3],"ill")# str(int(row[4])))