# REST API ON FLASK

задание:<br/>
1. Необходимо разработать REST API, предоставляющее возможность ведения блога.<br/>
2. API должен иметь минимум 2 сущности:<br/>
   - Пользователь
   - Пост
4. Пользователь должен иметь возможность:<br/>
   - создать
   - прочитать
   - изменить
   - удалить пост
5. Задание должно быть выполнено с помощью фреймворка Flask<br/>
6. Задание необходимо предоставить в виде архива с исходными кодом или ссылки на репозиторий в github/gitlab<br/>


Помимо кода, должна быть краткая инструкция по запуску задания.<br/>
В инструкции необходимо указать примеры тела запросов, HTTP метод и соответствующие URL для осуществления операций.<br/>


# инструкция к API
В коммандной строке перемещаемся в папки с проектом с помощью команды cd, например: "cd try_to_do_API_FLASK"<br/>
1. Сreate twit:<br/>
   - curl http://127.0.0.1:5000/create/ -Metod POST -ContentType 'application/json' -Body '{"body": "text", "author": "username"}'


2. Read list of twits:<br/>
   - curl http://127.0.0.1:5000/read/ 


3. Read one twit:<br/>
   - http://127.0.0.1:5000/read/<int:id>/


4. Update twit:<br/>
   - curl http://127.0.0.1:5000/update/1/ -Method PUT -ContentType 'application/json' -Body '{"body": "text", "author": "username"}'


5. Delete twit:<br/>
   - curl http://127.0.0.1:5000/delete/1/ -Method DELETE
