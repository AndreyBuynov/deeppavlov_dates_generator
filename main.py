import random
import numpy as np
import os
from dates_generator import dates_generator
import argparse

sample_text = 'это жанр журналистики в котором автор ставит задачу проанализировать общественные ситуации процессы явления прежде всего с точки зрения закономерностей лежащих в их основе Такому жанру как статья присуща ширина практических обобщений глубокий анализ фактов и явлений четкая социальная направленность В статье автор рассматривает отдельные ситуации как часть более широкого явления Автор аргументированно пишет о своей точке зрения В статье выражается развернутая обстоятельная аргументированная концепция автора или редакции по поводу актуальной социологической проблемы Также в статье журналист обязательно должен интерпретировать факты это могут быть цифры дополнительная информация которая будет правильно расставлять акценты и ярко раскрывать суть вопроса Отличительным аспектом статьи является её готовность Если подготавливаемый материал так и не был опубликован не вышел в тираж не получил распространения то такой труд относить к статье некорректно Скорее всего данную работу можно назвать черновиком или заготовкой Поэтому целью любой статьи является распространение содержащейся в ней информации'

list_of_words = sample_text.split()


def write_file(file_name, text, dir_path=None):
    if not dir_path:
        dir_path=os.path.curdir
        
    file_name = dir_path + '/' + file_name
    
    with open(file_name, 'w') as f:
        f.write(text)

        
def make_file_name(num):
    return 'file_numb' + str(num) + '.txt'


def get_raw_text(date):
    start = random.randint(1,5)
    middle = len(date.split())
    sample_idx = np.arange(143)
    random.shuffle(sample_idx)
    ready_text = ''
    ready_text += create_entities(list(list_of_words[x] for x in sample_idx[:start]))
    ready_text += create_entities(list(date.split()), 'date')
    ready_text += create_entities(list(list_of_words[x] for x in sample_idx[middle+start:20]))
    return ready_text


def create_entities(raw_text, entities="O"):
    text = ''
    if entities == 'date':
        for i, item in enumerate(raw_text):
            if i == 0:
                text += item + ' B-DATE\n'
            else:
                text += item + ' I-DATE\n'
    else:
        for item in raw_text:
            text += item + ' O\n'
    return text


def create_dates_dataset(args):
    cnt = args.cnt
    if args.path:
        dir_path = args.path
    else:
        dir_path = None
        
    list_of_dates = dates_generator(cnt)
    for i in range(cnt):
        clear_text = get_raw_text(list_of_dates[i])
        file_name = make_file_name(i)
        write_file(file_name=file_name, text=clear_text, dir_path=dir_path)
    print(f'All {cnt} files are ready')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, required=False, help='path with txt files')
    parser.add_argument('--cnt', type=int, required=True, help='number of files')

    args = parser.parse_args()
    create_dates_dataset(args)
