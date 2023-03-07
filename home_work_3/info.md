# Что и зачем?

![image](https://user-images.githubusercontent.com/103320407/223500406-750e1549-c24f-4267-a419-218c4506c86f.png)

Создал отдельный .py файл для генерации и работы с классом

![image](https://user-images.githubusercontent.com/103320407/223500532-c31b8f33-51b1-4451-8c6f-ec1fe5e828bd.png)

В urls прописал пути для сайта

hello отсылает на страницу от 2 дз.

![image](https://user-images.githubusercontent.com/103320407/223500717-9b2c4dff-beeb-42f6-8a0e-966404a51a8f.png)

'' отсылает на страницу выбора иначе говоря на навигационную

![image](https://user-images.githubusercontent.com/103320407/223500865-8642e10b-ed9a-462c-a5f2-c2e2a90ba273.png)

На ней можно открыть либо заданные заранее urls-ы 
либо перейти по генерированным

products - при get запросе отсылает на страницу со всеми товарами

![image](https://user-images.githubusercontent.com/103320407/223501237-2563a37b-7aea-4b8a-97a4-4008a7aa855b.png)


products - при post запросе принимает 5 строк разделлёных \n аргументов и добавляет в список всех обьектов новый
может обрабатывать пропуски

![image](https://user-images.githubusercontent.com/103320407/223501665-c8935d37-fcef-47fb-a698-49519702d07e.png)


products/product/<int:id> - при указании индекса отправляет на описание соответсвующего обьекта в списке
при его отсутствии направляет на страницу 404
если же по индексу идёт None отпраляет на products GET

![image](https://user-images.githubusercontent.com/103320407/223502167-2ecd66ba-f792-4fe3-81cd-cff48270b6a9.png)


На этом в принципе и усё...

