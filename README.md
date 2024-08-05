# Perfect Chord
Приложения для лёгкого и удобного чтения текста и аккордов во время игры на любимом инструменте.

### Настройка venv:
```
poetry install --no-root
```
### Настройка pre-commit:
```
pre-commit install
```
### Создание .env:
```
cp .env-ex .env
```
### Создание миграций:
```
docker compose exec -it pc_api  poetry run alembic revision --autogenerate -m '<название миграции>'
```
### Генерация JWT RS256 ключей:
```
ssh-keygen -t rsa -b 4096 -m PEM -f auth.key
```
```
openssl rsa -in auth.key -pubout -outform PEM -out auth.key.pub
```
Создайте папку `keys` и переместите в неё 2 созданных файла.

### Запуск приложения:
```
docker compose up --build -d
```
