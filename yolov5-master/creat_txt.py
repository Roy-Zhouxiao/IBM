import os
import random

trainval_percent = 0.2  # 可自行进行调节
train_percent = 1
xmlfilepath = 'E:/科研电脑数据/Notebook/5989/train/XML'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('D:/yolo data/test.txt', 'w')
ftrain = open('D:/yolo data/train.txt', 'w')
# fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        # ftrainval.write(name)
        if i in train:
            ftest.write(name)
        # else:
        # fval.write(name)
    else:
        ftrain.write(name)

# ftrainval.close()
ftrain.close()
# fval.close()
ftest.close()