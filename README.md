1. Необходимо разработать REST API, предоставляющее возможность ведения блога.

2. API должен иметь минимум 2 сущности:

Пользователь
Пост

3. Пользователь должен иметь возможность:

создать
прочитать
изменить
удалить пост

4. Задание должно быть выполнено с помощью фреймворка Flask.

5. Задание необходимо предоставить в виде архива с исходными кодом или ссылки на репозиторий в github/gitlab

помимо кода, должна быть краткая инструкция по запуску задания
в инструкции необходимо указать примеры тела запросов, HTTP метод и соответствующие URL для осуществления операций

create twit
metthod POST:
http://127.0.0.1:5000/create/ >> send twit in this format: {"id": int, "body": "text", "author": "username"}

read list of twits:
method GET:
http://127.0.0.1:5000/read/

read one twit
method GET:
http://127.0.0.1:5000/read/<int:id>/

update twit
method PUT:
http://127.0.0.1:5000/update/<int:_id>/
send updated_twit in this format: {"id": int, "body": "updated_text", "author": "updated_username"}

delete twit
method DELETE:
http://127.0.0.1:5000/delete/<_id>/
