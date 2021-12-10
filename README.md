### Создание синтетических данных
Небольшой сервис для создания синтетических данных для дообучения моедли deeppavlov.

В процессе выполнения создаются файлы по 20 токенов в каждом, среди которых присутствует дата, указанная прописью.
Например: "двадцать пятого декабря одна тысяча девятьсот девяносто восьмого года"

Остальной текст берется случайным образом из заранее сохраненного текста - абзаца из википедии о значении слова статья с удаленной пунктуацией. Дополнительные слова не относятся к сущностям даты, поэтому не влияют на обучение, но дополняют своим шумом для натуральности.
Количество первых токенов перед датой так же берется случайно в промежутке от 1 до 5 штук.

В результате получаем файл вида:

имя файла: **file_numb0.txt** где цифра меняется по порядку
```
котором O 
вышел O 
ситуации O 
двадцать B-DATE 
восьмого I-DATE 
мая I-DATE
одна I-DATE
тысяча I-DATE
девятьсот I-DATE
девяносто I-DATE
седьмого I-DATE
года I-DATE
распространение O
направленность O
социальная O
своей O
является O
концепция O
относить O
статье O
```

Период дат для генерации используется по умолчанию с 1 января 1980 года по день запуска модуля.

Для генерации файлов с разметкой необходимо выполнить команду:
```
python main.py --cnt 30
```
Данная команда сгенерирует 30 файлов с датами и разметкой и разместит их в той директории, где выполняется скрипт.
Так же возможно указание следующих параметров:

* --path - путь для размещения готовых файлов
* --cnt' - необходимое количество файлов с разметкой
* --start - дата, с которой выбирается промежуток для генерации новых дат. Вводится в формате dd.mm.yyyy
* --end - дата, до которой выбирается промежуток для генерации новых дат. Вводится в формате dd.mm.yyyy


### Генератор дат

```
from dates_generator import dates_generator
```

Данным сервисом можно пользоваться для генерации списка случайных дат указанных текстом во временном промежутке от start_date до end_date
Даты указываются в родительном падеже: первого, второго и т.д.

```
dates_generator(cnt, start_date=None, end_date=None) -> list
```
Даты указываются в формате datetime.
В результате возвращается список дат текстом на русском языке.