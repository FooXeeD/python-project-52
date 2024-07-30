### Hexlet tests and linter status:
[![Actions Status](https://github.com/FooXeeD/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/FooXeeD/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/cef0571f186ab1a5af6b/maintainability)](https://codeclimate.com/github/FooXeeD/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/cef0571f186ab1a5af6b/test_coverage)](https://codeclimate.com/github/FooXeeD/python-project-52/test_coverage)
![My TEST](https://github.com/FooXeeD/python-project-52/actions/workflows/My_TEST.yml/badge.svg)
h3>Менеджер задач</h3>
https://python-project-52-lay3.onrender.com
<p>Простое веб-приложения для управления задачами в компании или команде.
Реализовано на фреймворке <b>Django 5.0.7</b>.
<ul>
  <li>Регистрация и аутентификация пользователей.</li>
  <li>CRUD : пользователей, статусов, меток, задач.</li>
  <li>Доступ к статусам, меткам и задачам имеют только авторизированные пользователи.</li>
  <li>Пока задаче присвоен статус или метка, ее нельзя удалить.</li>
  <li>Присутсвует фильтрация задач.</li>
  <li>Локализация RU/EN. По умолачанию RU. Переведено с EN. Папка с переводами locale/ru/</li>
  <li>Покрытие тестами</li>
</ul>
<h3>Переменные окружения</h3>
<p>Необходимо в корне проекта создать файл .env и записать туда значения переменных.</p>
<pre>
SECRET_KEY =
DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
ROLLBAR_TOKEN = 
</pre>
<h3>Установка</h3>
<pre>
$ git clone https://github.com/FooXeeD/python-project-52.git
$ cd python-project-52.git
$ make setup
# Сайт станет доступен по адресу http://127.0.0.1:8000/
</pre>
