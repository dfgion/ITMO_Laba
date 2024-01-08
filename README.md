# Лабораторная работа. Представление и работа с БД.
База данных — это упорядоченный набор структурированной информации или данных, которые обычно хранятся в электронном виде в компьютерной системе. База данных обычно управляется системой управления базами данных (СУБД).

Базы данных делят на 2 основных типа:
1. Реляционные
    * Это БД, в которых данные представлены в виде таблиц. (Строк и столбцов)
2. Нереляционные
    * Это БД, в которой в отличие от большинства традиционных систем баз данных не используется табличная схема строк и столбцов. В этих базах данных применяется модель хранения, оптимизированная под конкретные требования типа хранимых данных. Например, данные могут храниться как простые пары "ключ — значение", документы JSON или граф, состоящий из ребер и вершин.

Как ранее и говорилось для управления базой данных разработаны СУБД, например, PostgreSQL.

В данной лабораторной работе вам предстоит побыть в роли программиста, которому нужно дописать функционал к программе, которая взаимодействует с данными. 
> P.S. Это не СУБД!!1 Базы данных оптимизированы под хранение данных (например, имеют индексы для удобного взаимодействия)

Продолжаем! Данные хранятся в CSV файле. Фронтенд и некоторый функционал приложения уже готов, вам остается реализовать некоторые функции для того, чтобы закончить работу над приложением.

Главный файл, откуда производится запуск приложения это - manage.py

Файлы удобно распределены по каталогам, чтобы у вас не было нужны в гипнотизировании моего кода и попытках найти нужную функцую или класс.

## Немного о фронтенде
Фронтенд данного приложения написан на фреймворке flet. Flet — фреймворк, предоставляющий Flutter компоненты для разработки кроссплатформенных приложений на вашем любимом языке программирования Python. На этот фреймворк я наткнулся довольно случайно, когда разрабатывал эту лабораторную работу. Я решил не убивать вас каким-нибудь Tkinter и его "потрясающими" дизайнерскими решениями.
> Иногда я думаю, что у разработчика не было в планах делать библиотеку для пользователей винды выше, чем windows 95, но это так - моё личное мнение.

Так вот, flet позволяет писать фронтенд (и не только) для IOS, Android, Desktop и web приложений. Понимаю ваше удивление, касаемо последнего, но видимо фронтенд на питоне теперь не шутка.. 

Сам фронтенд написан с применением ООП, все объекты (или же controls((или же widgets))) представлены в виде классов, которые наследуются от класса UserControl с определенными методами. Если вы не до конца понимаете ООП или концепцию "Наследование", то советую перекреститься и зайти в интернет для поиска соответствующей информации, в самом конце предоставлю домены, где вы сможете найти инфу. 

Структура файлов:

>App - корень, древо, сердце и ху.. нашего приложения. Фронтенд в нём представлен в каталоге controls
>> Controls - каталог, включающий в себя python файлы, по которым распределен фронтенд. Я постарался ради вас с неймингом, поэтому позволю себе не объяснять полную структуру объектов фронтенда для приложения (Только если чуть-чуть). Если вам интересно, то поройтесь в этом дремучем лесу.\
>>Functions - каталог, включающий в себя python файл, в котором вы будете писать логику взаимодействия. Он включает в себя 1 основной файл: database_func.py

Для тех, кому приглянулся фреймворк - напишу информацию о том, как писать приложения в конце.

## Первый запуск
Для начала давайте убедимся, что вы готовы к запуску. 
1. Установите себе Git Bash на компьютер(хотя у всех уже должен быть) и создайте там пользователя
* git config --global user.name "John Doe"
* git config --global user.email johndoe@example.com
* Это пример, не все из нас Джон
2. Зайдите в какую-нибудь папку(или на рабочий стол) и щелкните е... правой кнопкой мыши и выберите git bash (Шаг указан для счастливых пользователей винды, так как на линуксе все и так умеют пользоваться гитом, а если нет, то мне очень жаль(там всё через терминал, но только git через apt установите)).
3. В git bash склонируйте себе удаленный репозиторий(тот, в котором вы сейчас читаете этот README).
4. Следующий шаг - открывайте ваш vs code (фанаты пайчарм извините) и заходите в проект.
5. Далее вам нужно настроить виртуальное окружение. Если вы на винде, то пропишите команду __python -m venv <название>__ я всегда пишу название venv. Если же Linux - __python3 -m venv env__
6. Далее самый ответственный момент - время установить зависимости. Стандарт для указания зависимостей это файл requirements.txt. Который вы можете увидеть и у себя в склонированном репозитории. Существует замечательная команда __pip install -r requirements.txt__, которую вы должны ввести у себя в консоли, __НО!__ Убедитесь, что вы в виртуальном окружении, чтобы не скачивать пакеты глобально. 
    * venv\Scripts\activate - Windows
    * source venv/bin/activate - Linux/MacOS

Теперь вы можете запустить у себя приложение и посмотреть на интерфейс. Я сделал некоторые фрагменты анимированными, так что наслаждайтесь. 

Думаю, что объяснять, как пройти проверку вам не нужно, лучше объяснить как и почему именно так работает это в коде. После того, как вы запускаете файл manage.py. Происходит инициализация eventloop, опять же, если вы не знаете, что такое eventloop, то welcome вниз README. Там указана статья об конкурентном или же асинхронном программировании. В eventloop изначально стартуют 2 задачи
* task_app
* task_telegram

Интуитивно понятно, что одна запускает бота в телеграм, а вторая приложение. В консоли будут соответствующие on_startup-уведомления. После запуска бот переходит в режим ожидания сообщения от пользователя, а приложение в режим ожидания запроса кода.
### Немного о системе с кодом
Код используется для аутентификации. Когда пользователь вводит код - идёт проверка является ли этот код кодом, который был отправлен ботом или нет. Если пользователь ничего не писал боту, то и соответствующего кода для проверки не будет, а значит и сверять не с чем, поэтому пользователю будет выведена соответствующая ошибка, указывающая на то, что нужно пройти в бота для получения кода доступа.

Собственно, мы и подошли к теме о том, что значит взаимодействие внутри localhost.
Данное приложение реализовано так, что компьютер является и сервером и клиентом в одном потоке(асинхронный код работает в одном потоке, в отличие от программы, где код выполняется в разных потоках threading или же в разных процессах(параллельно) multiprocessing). Архитектура такова, так как приложение создано не для выпуска в production, а в рамках лабораторной работы. Что я имею в виду - когда мы сканируем qr-код в приложении и переходим в бота, после чего пишем ему команду /start, то далее генерируется уникальный код функцией __secrets.token_hex(8)__, который шифруется вместе с никнеймом отправителя симметричным шифрованием из библиотеки cryptography (симметричное, так как для шифровки и расшифровки используется один и тот же ключ, в отличие от ассимметричного, где один ключ шифрует, а другой используется для расшифровки. Наглядный пример - RSA), затем запускается сервер(наше приложение) на локальном хосте с портом 9999, после чего инициализируется клиент, который будет отправлять зашифрованный код и никнейм, подключается к этому хосту, по тому же порту. Подход с помощью модуля asyncio с помощью создания tasks в уже существующем eventloop.
> В функции старта сервера (Расположение: app/utils/server) передается функция-обработчик или же хэндлер, которая реализована как class method класса Code(расположение: app/controls/registration). Простыми словами это обычный метод, который позволяет работать с атрибутами целого класса, а не определенного объекта. Реализуется с помощью декоратора @classmethod. Подробнее о classmethod укажу ниже :)

Далее наша клиентская программа отправляет зашифрованный код с никнеймом, а сервер в свою очередь получает update и отправляет входящие пакеты данных в обработчик(метод класса Code, как я написал ранее), после чего расшифровывает и записывает данные в атрибут класса cls.code и cls.nickname. Именно поэтому я и написал выше, что наш компьютер - и сервер, и клиент; код лишь переключается, благодаря асинхронному подходу, то на серверную программу, то на клиентскую.

Итак, извините меня за то, что я так жестоко обошёлся с вашей уставшей головой. Если вы что-то не поняли из того, что написано выше, то это не страшно, так как все материалы будут ниже, в любом случае всё познается на практике. Чем больше будете писать код, тем быстрее поймёте то, что было описано выше.

__Упрощенное объяснение того, что описывалось выше__ - Наш компьютер просто участвует и в роли сервера, и в роли клиента, чтобы получить код, записать его в нужный атрибут, с котором будут происходить дальнейшие действия. Вы можете задать резонный вопрос - зачем же работа с сокетами, если можно было просто в одном месте записать код в текстовый файл, а в другом прочитать для проверки? Делается это для того, чтобы показать вам примерную реализацию в реальных кейсах. Ведь пользователи же не скачивают, допустим, hidemevpn, в программе которого нужно ввести код(ключ) доступа, вместе с сервером себе на компьютер. Они скачивают клиентскую программу, которая подключается не к локальному, а внешнему хосту(серверу), который обрабатывает запросы пользователя. Пользователь вводит ключ, который есть у него - клиентская программа отправляет запрос на сервер, где идёт проверка ключа, после чего присылает ответ, в котором доступ либо разрешается, либо нет.

## Основное задание
Если вы прочитали информацию выше - я вас поздравляю, вы молодец (я бы не читал). Остальные пропустили много пэйлоада для мозга. Итак, приступим к описанию вашего задания. Как вы можете увидеть у себя на экране - вы прошли процесс аутентификации(я на это надеюсь..), попали на главный экран, где есть 2 основных страницы. Home и Database. Фото профиля на странице Home скачивается из тг, так что если у вас его нет, то будет анонимный профиль.(Скачивается, а не передается с помощью сокета, так как взаимодействие я вам показал на примере ника и кода, поэтому в рамках данной лр фотографию можно просто скачать:D ) Пройдя по ним, вы заметите, что информация имеется только на странице Home, а вот другая почему-то пустая. Как вы можете уже догадаться - вашей задачей будет написание некоторых функций для того, чтобы информация появилась на странице, а вместе с этим появилось и взаимодействие с этой информацией.
### Задание DatabasePage
В этом задании вам нужно реализовать функции форматирования и получения информации, а также взаимодействия с ней. В файле app/utils находится csv файл c данными о 20 людях, внимательно присмотревшись, вы можете заметить, что файл почему-то поврежден и в некоторых местах нет запятых, а в некоторых наоборот больше, чем одна.

Вашей первой задачей будет форматирование этого файла в читабельный csv-файл. Он содержит 7 именованных столбцов:\
__Имя__ 
__Последняя активность__ 
__Город__ 
__Права доступа__ 
__ID__ - всегда 3 цифры
__Паспорт__ - длина не важна
__ИНН__  - длина не важна

Если кому-то из вас это задание показалось сложным, то спешу вас обрадовать, это совсем не так. Как же это сделать? Существует такая замечательная вещь, как регулярки(Регулярные выражения). Именно это вы и должны использовать в рамках этого задания. В Python есть встроенная библиотека для работы с регулярными выражениями (модуль re)\
импортируйте его строкой __import re__; чтобы немного упростить вам задачу - расскажу алгоритм действий, который поможет вам с легкостью решить это задание:
1. Напишите регулярное выражение, которое будет валидировать и распределять на так называемые группы ваши элементы(7 столбцов)
2. Далее вам нужно пройти по каждой строке в цикле и отдать её в функцию форматирования, в которой с помощью команды re.sub разбить её на 7 элементов, которые объединить в новой строке в формате Имя,Последняя активность,Город,Права доступа,ID,Паспорт,ИНН __БЕЗ ПРОБЕЛОВ МЕЖДУ ЭЛЕМЕНТАМИ__.
* > re.sub(pattern, repl, string), в котором pattern это ваше регулярное выражение, repl будет r'\1,\2,\3,\4,\5,\6,\7', так как repl представляет собой то, на что в итоге заменяется элемент вхожения, а он должен замениться на строку вида "Имя,Последняя активность,Город,Права доступа,ID,Паспорт,ИНН", через обратный слэш указаны группы по которым будут распределены элементы строки (элемент это, например, имя, последняя активность и тд.), а string, соответственно, строка, с которой будут провереды операции
1. Cтроку отдавать в функцию форматирования, результат которой возвращать в генераторе 
* > yield formatting(строка)

Алгоритм, описанный сверху, должен быть разбит на 2 функиции: генератор и функцию форматирования
* Генератор читает поврежденный csv-файл, далее каждый раз отдает поврежденную строку в функцию форматирования, после чего получаенный результат возвращает с помощью ключевого слова yield
* Функция форматирования получает строку и с помощью re.sub форматирует её и возвращает. Результатом функции должна являться строка вида "Имя,Последняя активность,Город,Права доступа,ID,Паспорт,ИНН" __БЕЗ ПРОБЕЛОВ МЕЖДУ ЭЛЕМЕНТАМИ__

Функция генератор - get_entries, которая принимает путь к файлу и аргумент disable_rewrite, установленный в False по умолчанию. Первую строку из кривого файла csv Имя, Последняя активность и тд брать не нужно. Её вы пропускаете и берете только те строки, которые хранят информацию о человеке.\
Функция форматирования - formatting принимает 2 аргумента - строку(row) и disable rewrite. Данная функция в зависимости от disable_rewrite должна либо отправлять строку на форматирование и последующую запись в csv файл с помощью функции get_correct_csv, либо нет(Читайте полное задание, чтобы понять, что делает get_correct_csv и что делать, если disable_rewrite установлен в True)

Естественно, без полезных материалов я вас не оставлю. 
1. [Сайт для помощи в написании регулярных выражений](https://regex101.com/).
2. [Документация модуля re python](https://docs-python.ru/standart-library/modul-re-python/)
3. [Генераторы](https://pythonist.ru/generatory-v-python/)

### Немного о регулярных выражениях
Как я описал ранее регулярные выражение могут использоваться для форматирования и проверки строк, вот результат того, что у вас должно получиться с помощью регулярного выражения
![](screenshots\2024-01-05_19-15-24.png)

Описание:
![](screenshots\2024-01-05_19-18-16.png)
С помощью определенных паттернов вы можете находить в тексте соответствия.\
Пример: 
1. [А-я] позволяет найти все русские буквы(большие и маленькие)
2. [а-я] позволяет найти все маленькие русские буквы
3. [0-9] позволяет найти все цифры от 0 до 9(включительно)
4. [ ]* позволяет включить алгоритм поиска, в котором либо встречается такой шаблон, либо нет, то есть от 0 до +∞
5. [ ]+ позволяет включить алгоритм поиска, в котором такой шаблон точно встречается, то количество неограниченно, то есть от 1 от +∞

![](screenshots\2024-01-05_19-23-16.png)
![](screenshots\2024-01-05_19-23-46.png)

Так же в регулярках вы можете создавать группы и делить строки с помощью ().

Пример:\
![](screenshots\2024-01-05_19-33-31.png)


Уважаемые студенты, просьба не писать с вопросами о правильности задания, данное регулярное выражение можно написать и для этого даже не нужно прилагать огромных усилий. Ошибок в задании нет :D 
Но человек, проживающий по данному адресу может помочь inst: @dfgion __НЕ РЕКЛАМА__

Приступим к описанию вашей второй задачи.\
В файле database_func.py вы можете увидеть функцию generate_correct_csv, в ней вам нужно написать код для написания корректного csv-файла, который в дальнейшем будет использоваться программой для того, чтобы брать данные. После реализации функции для формирования строк (formatting), вы должны записывать данные в файл csv, так как при дальнейшем взаимодействии с программой данные не требуется форматировать опять и лишний раз нагружать систему. Самое сложное в этом задании открыть документацию по работе с модулем csv :(\
Важно! Чтобы первая строка в файле correct_users.csv была "Имя, Последняя активность, Город, Права доступа, ID, Паспорт, ИНН". __Она там и так есть, но в процессе вы можете её стереть, так что рекомендую её куда-нибудь сохранить.__ ну или нажимать ctrl+z :D

### Итог того, что должно получиться
Функция, которая записывает в файл correct_users.csv корректные, отформатированные строки. В дальнейшем именно этот файл будет использоваться программой, так что если вам не нравится моё название :0, то посмотрите где он используется аргументом и замените на свой с новым названием. Аргумент disable_rewrite используется для того, чтобы дать понять программе, нужно ли переписывать csv(будет ли использоваться generate_correct_csv) или же нет. То есть в статусе False он должен быть только в начале работы программы, потом же в функцию будет передаваться True(не требует переписывания). В общем, посмотрите код и поймёте о чём я пишу.

Ещё одно задание! Вам нужно реализовать асинхронный генератор - get_entries_async, который выполняет те же самые действия, что и get_entries, но в асинхронном режиме. Итогом будет асинхронный генератор, который возвращает строку из уже корректного csv(по умолчанию correct_users.csv) в функцию форматирования с аргументом disable_rewrite установленным в True
> yield formatting(строка, disable_rewrite = True)

Следующее задание!\
В файле database_func.py вы можете увидеть функцию flutter_formatting. Тут максимально просто. Отформатированная строка в функции formatting должна подгоняться под flet object. Функция просто принимает name, last_login, city, status, user_id, passport, tin, которые вы должны получить из отформатированной строки и передать в функцию. (ес че TIN - это ИНН)

### Итог того, что должно получиться
Как вы поняли, функцию не нужно писать. В неё просто нужно передать элементы отформатированной строки (что такое элементы я уже объяснял). Это делается, так как фронтенд должен получить flet object (Control), а именно DataRow, который формируется этой функцией. После того, как функционал для запуска был написан - должен быть функционал для дальнейшей работы - функция get_entries_async, которая используется после форматирования csv файла, а значит форматировать и заново записывать данные в файл не нужно, нужно просто прогнать функцию через formatting, откуда она попадёт в flutter_formatting

Также я предоставляю вам возможность поменять шрифты или цвета, если вам вдруг что-то не нравится. DataRow хранит в себе 7 controls (flet objects) - DataCell, хранящие Text, которые, в свою очередь, хранят в себе цвет. Изначально он установлен как black, но вы можете воспользоваться своей памятью, которая хранит названия цветов на английском, и изменить цвет на тот, который вам больше нравится, если с этим туго, то вот вам [документация](https://flet.dev/docs/guides/python/colors/), где вы можете найти нужный вам цвет, ещё есть вариант просто написать ft.colors. и великолепный vs code выдаст вам варианты доступных цветов (любители pycharm извиняюсь ещё раз). Шрифты можно поменять в атрибуте font_family, просто скачиваете нужный шрифт(поддерживающий русский язык), переносите его в assets\fonts и указываете путь.

Следующим заданием будет реализация функции удаления записи о пользователе по его ID. После запуска программы данные в csv форматируются и записываются в корректный csv-файл, откуда потом с ним будут происходить операции, например, операция удаления пользователя с помощью функции delete_user_async. В данной функции вы должны написать код, который заключается в том, чтобы брать данные из csv файла, фильтровать их, чтобы там не было записи о человеке с ID, по которому происходит удаление, после чего записыть в тот же файл. Как вы уже могли понять из названия, функция должна быть [асинхронной](https://habr.com/ru/companies/wunderfund/articles/700474/). Если записи по такому ID нет, то ничего не нужно делать

Полностью делать всю работу асинхронным кодом я вас не заставляю, но простые функции для понимая асинхронности в python всё же придётся сделать. Главная идея в том, чтобы вы поняли хотя бы примерно, как работает асинхронное программирование, что такое IO-bound и CPU-bound нагрузки.

Удачи в выполнении работы!

## Инфа как писать на Flet

Я объясню вам ключевые моменты, а дальше вы сможете найти материал в документации. Как я уже говорил, flet представляет собой фреймворк для написания графического интерфейса(и не только), если вы раньше не работали с фреймворками для написания gui, то возможно инфа вам покажется сложной, но это лишь временно. 
### Расположение объектов

У каждого виджета(control) есть свои атрибуты для расположения на странице. Например, если вы используете контейнер, то его свойство alignment может задаваться с помощью указания aligment.Aligment(0, 0) в качестве значения для того, чтобы расположить объект поцентру(Не путайте расположение самого контейнера и объекта внутри него, alignment отвечает на расположение внутри контейнера). Если же вы хотите расположить контейнер, то вы должны ссылаться на свойства объекта, в котором он находится(Page это тоже объект, у которого тоже есть свойства для расположения объектов внутри него). Для расположения объектов в вертикальном направлении вам может пригодиться Column, для того, чтобы расположить объекты горизонтально, вы можете использовать Row. Для наложения объектов друг на друга подойдёт Stack, это может пригодиться в случае, когда вы хотите задать задний фон изображения. Тогда вы можете использовать Stack, в который передается Image(control) и ваши другие объекты. В документации находится большая часть того, что вам может пригодиться, описание всех свойств и объектов.

### Использование ООП для декомпозиции и структурированности

Используйте парадигму ООП в фреймворке для того, чтобы ваш код стал более читабельным. Flet позволяет создавать пользовательствие contols в виде классов, позволяя разбивать код на модули. Для того, чтобы создать пользовательский виджет, вам нужно создать класс, который наследуется от класса UserControl и переопределить у него метод build, который должен возвращать control или их список. Как и у других классов, вы можете задать __init__, который позволит передать данные конкретному объекту. 

### Анимации

Почти каждый виджет может быть анимированным, для того, чтобы создать анимацию, вам нужно указать определенный свойства у объекта, например:

__opacity__ - Анимация прозрачности
__offset__ - Анимация перемещения по линии
__rotation__ - Анимация поворота
__scale__ - Анимация масштабирования
__position__ - Комбинированные перемещения по нескольким сторонам
__и другие__

### Асинхронный подход

Используйте асинхронное программирование для создания асинхронных приложений, способных выполнять несколько действий пользователя с помощью переключения контекста. Методы у классов в таком случае должны быть асинхронными, а при указаниии уже существующих методов объектов вы должны вызывать методы с _async на конце(если такие методы есть), ну и естественно через await внутри асинхронной функции, так как это корутина. Сам запуск приложения app() должен не асинхронным (не app_async), если не является частью другого асинхронного кода, иначе такое же действие, как и с методами.

## Полезные материалы




