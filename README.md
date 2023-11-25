### Проект Благотворительный фонд

## API Позволяющий получать информацию о благотворительных проетах и автоматически распределять по ним пожертвования.


## Используемые технолологии:

FastAPI
sqlalchemy


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:atar1boy/cat_charity_fund.git
```

```
cat_charity_fund
```

Создать .env файл внутри директории проекта:

Пример файла .env

```
APP_TITLE=TITLE
APP_DESCRIPTION=DESCRIPTION
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=SECRET
FIRST_SUPERUSER_EMAIL=admin@admin.ru
FIRST_SUPERUSER_PASSWORD=admin
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Запуск сервера:

```
uvicorn app.main:app
```
