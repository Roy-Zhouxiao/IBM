import os
import xml.etree.ElementTree as ET
import pickle

train = 'D:/yolo data/train.txt'
test = 'D:/yolo data/test.txt'


def readTxt(txt):
    f = open(txt, 'r')
    ans = []
    lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
    for line in lines:
        line = line.strip('\n')
        ans.append(line)
    return ans


classes = ['drone', '1']  # 自己训练的类别


#                红灯           绿灯
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):  # 转换这一张图片的坐标表示方式（格式）,即读取xml文件的内容，计算后存放在txt文件中。
    in_file = open('D:/yolo data/xml/%s.xml' % image_id, encoding='UTF-8')
    out_file = open('D:/yolo data/txt/%s.txt' % image_id, 'w', encoding='UTF-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    # tree = open(in_file)
    # xml_text = f.read()
    # root = ET.fromstring(xml_text)
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            print("没有找到类")
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


lines = readTxt(train)
# print(lines)
for line in lines:
    convert_annotation(line)
    print("处理的", line)

lines = readTxt(test)
# print(lines)
for line in lines:
    convert_annotation(line)
    print("处理的", line)
