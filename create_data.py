import argparse
import glob
import os
import numpy as np


def create_file(idx_list, file_list, mode, work_dir):
    new_text = ''
    ent_list =['B-GPE', 'B-CARDINAL', 'B-NORP', 'I-MONEY', 'I-GPE', 'I-PERCENT', 'B-MONEY', 'I-WORK_OF_ART',
               'I-CARDINAL', 'B-PERCENT', 'B-ORDINAL', 'I-EVENT', 'B-LOC', 'I-TIME', 'I-FAC', 'I-LOC', 
               'I-QUANTITY', 'B-TIME', 'B-WORK_OF_ART', 'B-FAC', 'I-LAW', 'B-EVENT', 'B-QUANTITY', 'B-PRODUCT',
               'I-PRODUCT', 'I-NORP', 'B-LANGUAGE', 'B-LAW', 'I-LANGUAGE', 'I-ORDINAL']
    tags = ['B-DATE', 'I-DATE', 'B-ORG', 'I-ORG', 'B-PERSON', 'I-PERSON', 'O']
    for idx in idx_list:
        with open(file_list[idx], 'r') as f:
            temp_text = ''
            need_line = False
            for i, line in enumerate(f):
                text = line.replace('\t', ' ')
                if i % 20 == 0:
                    need_line = True
                if len(text.split()) == 2:
                    if need_line and text.split()[1] == 'O':
                        temp_text += text + '\n'
                        need_line = False
                    else:
                        if text.split()[1] == 'O' and len(ent_list) > 0:
                            temp_text += text.split()[0] + ' ' + ent_list[0] + '\n'
                            ent_list.pop(0)
                        elif text.split()[1] == 'B-ORGANIZATION':
                            temp_text += text.split()[0] + ' B-ORG' + '\n'
                        elif text.split()[1] == 'I-ORGANIZATION':
                            temp_text += text.split()[0] + ' I-ORG' + '\n'
                        elif text.split()[1] == 'B-PER':
                            temp_text += text.split()[0] + ' B-PERSON' + '\n'
                        elif text.split()[1] == 'I-PER':
                            temp_text += text.split()[0] + ' I-PERSON' + '\n'
                        elif text.split()[1] in tags:
                            temp_text += text

        new_text += temp_text + '\n'

    new_file_name = mode + '.txt'
    with open(work_dir + '/' + new_file_name, 'w') as f:
        f.writelines(new_text)

def main(args):
    """
    Скрипт считывает из папки все txt файлы и собирает из них случайным образом три
    файла для обучения модели deeppavlov.
    Размер выборок указывается в аргументах через -
    """
    WORK_DIR = args.path
    
    file_list = glob.glob(WORK_DIR + "/*.txt")
    
    x = np.arange(len(file_list))
    np.random.shuffle(x)
    l_tr, l_ts, l_v = args.size.split('-')
    
    len_train = round(len(file_list)*int(l_tr)/100)
    len_test = round(len(file_list)*int(l_ts)/100)
    len_val = round(len(file_list)*int(l_v)/100)

    train_idx = x[:len_train]
    test_idx = x[len_train:len_train+len_test]
    val_idx = x[len_train+len_test:len_train+len_test+len_val]

    create_file(train_idx, file_list, 'train', WORK_DIR)
    create_file(test_idx, file_list, 'test', WORK_DIR)
    create_file(val_idx, file_list, 'valid', WORK_DIR)
    print(f'All files are ready in {WORK_DIR}')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, required=True, help='path with txt files')
    parser.add_argument('--size', type=str, required=True, help='train/test/valid size like 80-10-10')

    args = parser.parse_args()
    main(args)