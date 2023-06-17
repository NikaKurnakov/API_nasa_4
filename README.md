# Космический телеграмм

Этот проект поможет вам загрузить в телеграмм канал фото от NASA_APOD, spaceX и NASA_EPIC.

### Как получить API-ключ от NASA ID от spaceX, токен для телеграм бота и ID канала

Для того чтобы получить API-ключ от NASA_APOD, Вам нужно зарегистрироваться на [сайте](https://api.nasa.gov/#apod). API-ключ отправят Вам на почту.

После вам надо получить API-ключ от NASA_EPIC. Вам также надо зарегистрироваться [здесь](https://api.nasa.gov/#epic). API-ключ Вам так же отправят на почту. 

ID для spaceX можете использовать вот этот `5eb87d46ffd86e000604b388`. Тип данных ID `str`. 

Чтобы получить токен для телеграм бота, надо создать самого бота. Достаточно следовать инструкции бота `BotFather`. Он вам отправит ссылку на вашего бота и его токен.

Для получения ID канала, надо отправить боту `Get My ID` любое сообщение от канала, и в строке `Forwarded from chat` будет ID канала. 

### Переменные окружения

Когда вы получите свои ID, API-ключи и токен надо записать их в переменную окружения. Но у нас пользователи будут вводить свои данные в терминал, поэтому нам переменные окружения не нужны. 

### Как создать переменные окружения

Для появления переменных окружения вам надо импортировать библиотеку `os`.

```
import os
```

Далее вам надо создать переменные, в которых будут храниться ваши API-ключ, токен от бота и id канала, и присвоить им значение `os.environ`. Значение `os.environ` известно как объект мэппинга (сопоставления), который работает со словарем переменных пользовательской среды.

```
nasa_epic_token = os.environ['NASA_EPIC_TOKEN']
tg_token_bot = os.environ['TG_TOKEN_BOT']
tg_chanel_id = os.environ['TG_CHANEL_ID']
```

Когда вы создали переменные, надо присвоить им значение. Создайте файл `env.example`. В нем запишите названия переменных окружения и в кавычках напишите свой API-ключ, токен от бота и id канала. После создайте файл `.gitignore` и в него запишите `env.example`.

```
NASA_EPIC_TOKEN='ваш API-ключ'
TG_TOKEN_BOT='ваш токен от бота'
TG_CHANEL_ID='ваш id от канала'
```

Но для файла `send_photo_chanel.py` в переменной `delay_time` понадобится тоже переменная окружения, но со значением `os.getenv`. Переменная с этим значением позволяет установить значение по умолчанию. 

```
delay_time = args.delay if args.delay else os.getenv('DELAY', default=14400)
```

`'DELAY'` это название переменной в файле `env.example`. `default=14400` это значение по умолчанию. Вот так переменная будет выглядеть в файле `env.example`:

```
DELAY=14400
```

### Работа с библиотекой Argparse на примере файла get_epic_image.py

Для начала надо установить библиотеку.

```
import argparse
```

Далее есть синтаксис, который не меняется у этой библиотеки.

```
 parser = argparse.ArgumentParser()
```

В этой строчке мы говорим, что будем добавлять аргументы. После нам надо добавить сами аргументы. 

```
parser.add_argument("--epic_token", default=os.environ['NASA_EPIC_TOKEN'], help="epic_token")
```

Функция `add_argument` добавляет аргумент. Параметр, принимающий значение, будет `"--epic_token"`. Значение `default` означает, что если у вас будет написан токен в переменной окружения, то он будет брать от туда. Значение `help`, отвечает за пояснение аргумента. Чтобы добавить эти значения в код, надо использовать `args`.

```
args = parser.parse_args()
```

В коде будет это выглядеть вот так:

```
args.epic_token
```

### Запуск файла get_epic_image.py

Затем, когда разобрались с переменными, надо запустить код. Вы также можете выбрать количество картинок, которые хотите скачать. Если у вас Windows и есть API-ключ, то он запускается так:

```
py get_epic_image.py.py --epic_token ваш_токен --numb число_картинок
```

Если у вас Linux, то код будет запускаться почти так же, только вместо `py` будет `python`:

```
python get_epic_image.py.py --epic_token ваш_токен
```

### Запуск файла get_spaceX.py

Для этого запуска вам нужен id:

```
py get_spaceX.py --id ваш_id
```

На Linux то же самое:

```
python get_spaceX.py --id ваш_id
```

### Запуск файла tg_bot.py

Для запуска вам нужен будет токен вашего бота и ID канала. Если вы хотите скачать определенный файл, укажите его.
```
py tg_bot.py --bot_token токен_бота --chanel_id id_канала --file название_файла
```

На Linux то же самое:

```
python tg_bot.py --bot_token токен_бота --chanel_id id_канала --file название_файла
```

### Запуск файла send_photo_chanel.py

Для запуска вам нужен будет токен вашего бота и ID канала. Если вы хотите указать другое время загрузки, укажите его.

```
py send_photo_chanel.py --bot_token токен_бота --chanel_id id_канала --delay время_загрузки
```

На Linux то же самое:

```
python send_photo_chanel.py --bot_token токен_бота --chanel_id id_канала --delay время_загрузки
```


### Зависимости

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для 
установки зависимостей:

```
pip install -r requirements.txt
```
