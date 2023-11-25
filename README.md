<h1 align="center"> Проект Кошачий Благотворительный Фонд :smiley_cat:

<h3 align="center">API Позволяющий получать информацию о благотворительных проетах и автоматически распределять по ним пожертвования.</h3>


## Используемые технолологии:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy-%2300f.svg?style=for-the-badge)
![alembic](https://img.shields.io/badge/alembic-3ECF8E?style=for-the-badge&)
![uvicorn](https://img.shields.io/badge/uvicorn-%23DD0031.svg?style=for-the-badge&)
![pydantic](https://img.shields.io/badge/pydantic-39477F?style=for-the-badge&)

## Код Писал
<h3>Никита Ковалев</h3>
<a href="https://discordapp.com/users/432288531583598592/">
<img src="https://user-images.githubusercontent.com/74038190/235294015-47144047-25ab-417c-af1b-6746820a20ff.gif" width="60px"/>
</a>
<a href="https://t.me/gl_ready/">
<img src="https://user-images.githubusercontent.com/74038190/235294015-47144047-25ab-417c-af1b-6746820a20ff.gif" width="60px"/>
</a>
</a>
<a href="https://t.me/gl_ready/">
<img src="https://user-images.githubusercontent.com/74038190/235294015-47144047-25ab-417c-af1b-6746820a20ff.gif" width="60px"/>
</a>

<br />
<br />

- [Как запустить проект](#как--запустить--проект)
- [Запуск сервера](#запуск--сервера)
- [Настройка базы данных](#Настройка--базы--данных)

<br />
<br />

### Как запустить проект

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

## Запуск сервера

```
uvicorn app.main:app
```
