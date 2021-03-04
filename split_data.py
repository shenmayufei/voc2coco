import os
import random
import argparse

# usage:
# split_data.py --trainval_percent 0.85 --train_percent 0.85 --xml_file_path "/media/yzh/data/comma/tobo_2833_dataset/Annotations" --txt_save_path ""

def splitDataset(trainval_percent,train_percent,xmlfilepath,txtsavepath):
    # trainval_percent = 0.85
    # train_percent = 0.85
    # xmlfilepath = 'Annotations/'
    # txtsavepath = 'ImageSets/Main'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open(txtsavepath + '/trainval.txt', 'w')
    ftest = open(txtsavepath + '/test.txt', 'w')
    ftrain = open(txtsavepath + '/train.txt', 'w')
    fval = open(txtsavepath + '/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trainval_percent", type=float, default=0.85,
                        help="the trainval_percent number ,default is 0.85")
    parser.add_argument("--train_percent", type=float, default=0.85, help="the train_percent number ,default is 0.85")
    parser.add_argument("--xml_file_path", type=str, default="",
                        help="the training dataset xml file path ,default is "" ")
    parser.add_argument("--txt_save_path", type=str, default="",
                        help="the training dataset txt_save_path ,default is "" ")

    args = parser.parse_args()

    if(args.xml_file_path == "" or args.txt_save_path == "" ):
        print("the xml file path is null or the txt save path is null")
    else:
        splitDataset(args.trainval_percent, args.train_percent, args.xml_file_path, args.txt_save_path)


