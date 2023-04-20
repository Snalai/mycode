"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

for wor in ['разработка', 'сокет', 'декоратор']:
    print(f"Тип: {type(wor)}, содержание: {wor}")

for t_b in [b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
          b'\u0441\u043e\u043a\u0435\u0442',
          b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']:
    print(f"Тип: {type(t_b)}, содержание: {t_b}")

"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

for wor in [b'class', b'function', b'method']:
    print(f"Тип {type(wor)}, содержимое {wor}, длинна строки: {len(wor)}")

"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

for wor in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(f"{wor.encode('ascii')}, слово '{wor}' - исключение ")
    except:
        print(f"слово '{wor}' - невозможно записать в байтовом типе")

"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

wor = ["разработка", "администрирование", "protocol", "standard"]
for c_de in wor:
    print(f"Строковое представление: {c_de}")
    a = c_de.encode('utf-8')
    print(f"Байтовое представление: {a}")
    print(f"обратное преобразование: {a.decode('utf-8')}\n")

"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess, chardet

for si in ['yandex.ru', 'youtube.com']:
    ix = ['ping', si]
    rawdata = subprocess.Popen(ix, stdout=subprocess.PIPE)
    for line in rawdata.stdout:
        a = chardet.detect(line)
        print(line.decode(encoding=a['encoding']))

