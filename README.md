## Тестовое задание, краткая аннотация

В данном репозитории находятся решения трех задач из тестового задания

### task_1

Папка содержит Jupyter-notebook с решением и комментариями. Кроме того, сам Jupyter notebook также экспортирован в HTML, для удобства просмотра на некоторых устройствах. 

### task_2

Папка содержит исходный код решения второй задачи. <br>
В ходе решения создано веб-приложение, которое содержит две точки входа: <br>
http://<ip:port>/db/ - страница, при входе на которую (запросом GET) идёт обращение к БД (postgres) и пользователю выдаются данные, полученные в ходе выполнения задачи 1 <br> 
Пример вывода: <br> 

```
('(37.212384,56.001591)', 'atm')
('(37.215998,55.996413)', 'atm')
('(37.21567,55.995869)', 'atm')
('(37.210458,55.997989)', 'supermarket')
('(37.209,56.000198)', 'supermarket')
('(37.216219,55.996584)', 'supermarket')
('(37.218563,55.996989)', 'supermarket')
('(37.213194,55.993363)', 'supermarket')
```

http://<ip:port>/online/ - страница, при входе на которую пользователю предлагается ввести координаты, диапазон и интересующую категорию. При отправке введенных значений осуществляется POST-запрос к серверу и задействуется код из задания 1, чтобы найти POI. Данные POI рисуются на карте и карта показывается пользователю <br>
Пример вывода: <br>

![Screenshot](https://i.ibb.co/7CMx8Pn/screen.png)
<br>
Кроме того, вживую можно ознакомиться с решением, если скачать и запустить docker-контейнеры следующим образом: <br>
```
docker pull vvorotnikov/geopython:webapp
docker pull vvorotnikov/geopython:postgresv0.3

docker network create gnet --driver bridge --subnet 10.1.37.0/24

docker run -ti --network gnet --ip 10.1.37.2 -d vvorotnikov/geopython:postgresv0.3
docker run -ti --network gnet --ip 10.1.37.3 -p 5555:5555 -d vvorotnikov/geopython:webapp
```
После чего можно зайти браузером на адрес 10.1.37.3:5555/db/ (или 10.1.37.3:5555/online/) или адрес устройства где запущен контейнер и посмотреть работу вживую. <br>

vue.js на решение не натягивал, вместо этого сделал дополнительную часть не предусмотренную заданием (страница online). Представление о vue.js имею, но уже вылез за временные лимиты, которые могу потратить на 1 тестовое задание, поэтому решил сфокусироваться на бекэнде. <br>

Просьба воспринимать код веб-приложения как скетч: есть ряд точек, которые нужно обкладывать try-ями, по другому нужно строить работу и запросы к базе, в работе по сути отсутствует весь фронтэнд, естественно возникает и вопрос тестов, документации. Все это в объем тестового задания у меня не вошло (общее время выполнения данного тестового задания составило ~16 чистых часов, т.е. 2 рабочих дня), что кажется адекватным. <br>

### task_3 

Т.к. код требовал некоторых экспериментов и комментариев, собрал не в виде скрипта, а в виде jupyter-notebook'a, для удобочитаемости. Все комментарии по заданию внутри <br>

Буду рад пообщаться и ответить на любые возникшие вопросы

