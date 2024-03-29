### Список команд
В консоли выполнить `python manage.py --help`

Не входя в контейнер: 
```bash
docker-compose exec auth-api python manage.py --help
```


### Создание админа:
Из контейнера: `python manage.py create-admin admin@mail.ru 123123 Ivan Ivanov`

Не входя в контейнер: 
```bash
docker-compose exec auth-api python manage.py create-admin admin@mail.ru 123123 Ivan Ivanov
```

После этого можно логиниться им в http://localhost:8080/api/openapi#/

### Создание фейковых пользователей:
Из контейнера: `python manage.py create-fake-users 15`

Не входя в контейнер: 
```bash
docker-compose exec auth-api python manage.py create-fake-users 15
```

## gRPC

Достаточно подробно описано в https://grpc.io/docs/languages/python/quickstart/.

---
Файлы в `api_grpc_server/core/grpc` генерируются автоматически на основе файла `protos/users.proto`. Редактировать или пытаться анализировать их не нужно 😀

Если потребуется отредактировать `protos/users.proto`, то после этого нужно заново сгенерировать файлы в `core/grpc`


```bash
python -m grpc_tools.protoc --proto_path=./protos --python_out=./core/grpc --grpc_python_out=./core/grpc ./protos/users.proto --pyi_out=./core/grpc
```


##### Небольшая ручная доделка: в файле core/grpc/users_pb2_grpc.py отредактировать:
```bash
import users_pb2 as users__pb2` ---> `from . import users_pb2 as users__pb2
```

### Генерировать файлы нужно и в api_simple проекте ! 

---

### API сервис авторизации

http://localhost:8080/api/openapi#/

### API мелкое приложение для пробы gRPC клиента

http://localhost:8085/docs