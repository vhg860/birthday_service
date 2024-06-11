# Birthday Notification Service
```text
Тестовое задание:
Написать сервис для поздравлений с днем рождения.
o Цель удобное поздравление сотрудников
o Получения списка сотрудников любым способом(api/ad ldap/прямая регистрация)
o Авторизация
o Возможность подписаться на отписаться от оповещения о дне рождения
o Оповещение о ДР того на кого подписан
o Внешнее взаимодействие (json арi или фронт или тг бот)
o В случае взаимодействия через тг бот (создание группы и добавление в нее всех подписанных)
o В случае взаимодействие через фронт настройка времени оповещения до дня рождения на почту.
```
## Описание
Сервис для поздравлений с днем рождения сотрудников.

## Установка и запуск
1. Клонируйте репозиторий:
    ```sh
    git clone git@github.com:vhg860/birthday_service.git
    cd birthday_service
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

3. Установите необходимые зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Создайте и настройте файл `.env` на основе `.env.example` для настройки электронной почты и базы данных.

5. Выполните миграции для настройки базы данных:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Создайте суперпользователя для доступа к административному интерфейсу:
    ```sh
    python manage.py createsuperuser
    ```

7. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Использование

- Зарегистрируйтесь по адресу `/register/`
- Войдите в систему по адресу `/login/`
- Просмотрите и подпишитесь на дни рождения пользователей по адресу `/users/`
- Просмотрите ваши подписки по адресу `/subscriptions/`

## Уведомления по электронной почте

Убедитесь, что настройки электронной почты в `settings.py` правильно сконфигурированы для включения уведомлений по электронной почте. Пример конфигурации:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
```
