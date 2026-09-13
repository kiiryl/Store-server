# Django Web Application (Educational Project)

Учебный веб-проект, разработанный для отработки навыков backend-разработки на Python и Django, интеграции с реляционными базами данных, а также настройки базового функционала веб-приложений (корзина, авторизация, обработка данных).

---

## Технологический стек

* **Language:** Python 3
* **Framework:** Django
* **Database:** PostgreSQL / SQLite
* **Frontend:** HTML5, CSS3, Bootstrap
* **VCS:** Git, GitHub

---

## Основной реализованный функционал

* Аутентификация и авторизация пользователей.
* Создание и управление корзиной товаров (Basket System).
* Взаимодействие с базой данных через Django ORM.
* Настройка маршрутизации и обработка HTTP-запросов (GET, POST).
* Валидация форм и работа со статическими файлами.

---

## Локальный запуск проекта
1. **Клонируйте репозиторий:**
    ``` bash
    git clone https://github.com/kiiryl/Store-server.git
    ```
2.  **Создайте и активируйте виртуальное окружение:**
    ```Bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    # venv\Scripts\activate   # Для Windows
    ```
3.  **Установите зависимости:**
    ``` Bash
    pip install -r requirements.txt
    ```
4.  **Примените миграции:**
    ``` Bash
    python manage.py migrate
    ```
5.  **Запустите сервер разработки:**
    ``` Bash
    python manage.py runserver
    ```
    Приложение будет доступно по адресу: http://127.0.0.1:8000/

👤 Автор

    Кирилл Полещук

    GitHub: @kiiryl
