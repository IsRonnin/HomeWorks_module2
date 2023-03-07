# Почему не стартует джанго?

.

.

Предисловие. По прмеру одного человека узнал что вы забывваете сохранять 
файл - помните что то изменили -> Контрол + S

![image](https://user-images.githubusercontent.com/103320407/223197600-e6e4febf-513f-417f-a09b-3ae5102fed17.png)

*Конец предисловия*

.

.


Ну что-ж по жалобам многих опишу подробно 
"КАК ЧЁРТ ПОБЕРИ ЗАСТАВИТЬ
ДЖАНГУ РАБОТАТЬ" - цитата


Ну для начала создаём в папке проекта file.py и открываем его

после чего запускаем его что бы появился терминал (знаю что можно просто открыть терминал отдельно)

![image](https://user-images.githubusercontent.com/103320407/222906062-4af8137b-e0cd-4400-a8b1-4dde08ed284f.png)

После чего идём и лапками в терминал пишем такие комманды ->


py -m venv env

env\scripts\activate

pip install django


![image](https://user-images.githubusercontent.com/103320407/222906170-30512e34-6bb4-40cf-8747-1f0c21a3b55d.png)

После этого если есть ошибка идём и читаем статью выше по репу а если всё ок - дальше
Прямо в терминал печатаем 


django-admin startproject shop

cd shop

django-admin startapp kittyshop


![image](https://user-images.githubusercontent.com/103320407/222906467-66b3fbb5-a1a8-40c7-9e93-15fd3138d833.png)

Если всё ок идём дальше если нет то читаем статью по новой и повторяем

Теперь открываем файл settings.py по пути <Путь к проекту>/shop/shop/settings.py

![image](https://user-images.githubusercontent.com/103320407/222906565-254479a9-02d6-4cf4-ba83-acccec60908d.png)

в нём мы ищем список называемый INSTALLED_APPS
в него добавляем новою строку 'kittyshop'

![image](https://user-images.githubusercontent.com/103320407/222906686-cedf6556-d592-48c9-99b5-a46dc0122df6.png)

после чего мы готовы к работе!

что-бы запустить наше приложение нам нужно прописать комманду


py manage.py runserver


(Может выдать ошибку no such file in directory
не пугайтесь это лишь значит что у вас не выбрана директория проекта и нужно с помощью
комманды cd перейти в неё 

![image](https://user-images.githubusercontent.com/103320407/222906971-58cbd2f3-3da8-4f82-a8a8-1e3b2ff050ce.png)

Пишите в терминал следующие 


cd shop

и повторяем комманду запуска сервера)

Второй возможный вариант - что срдеа потеряла django 

если такое случилось

мы берём и заново её создаём и вписываем туда (по статье выше)

pip install django


если-же всё хорошо то - 
В терминале появится 

![image](https://user-images.githubusercontent.com/103320407/222906798-5956b1b9-bd36-477f-aa43-89cc9afc8cf7.png)

и ссылка на ваш сайт (локальная друзьям можете не кидать ;3)

![image](https://user-images.githubusercontent.com/103320407/222906853-832de109-5119-48ea-ab8d-d8c1122e7edd.png)

можно перейти нажав на неё с зажатым контролом

![image](https://user-images.githubusercontent.com/103320407/222906883-6fd64191-caf7-4ca3-ac6b-9e100851e0cd.png)

Если вы видите эту страничку вы молодец! и у вас всё настроенно верно!




