## Это backend для будущего сервиса СЕРВАНТ (тг бот для помощи в быту)


## Напоминалка для работы с бд
1. Чтобы запустить дбивер нужна команда dbeaver-ce
ссылка на инфу про дбивер https://losst.pro/ustanovka-dbeaver-v-ubuntu-22-04
2. Чтобы проверить статус постгреса нужна команда sudo systemctl status postgresql.service
ссылка на инфу про постгрес https://firstvds.ru/technology/ustanovka-postgresql-na-ubuntu
3. создание миграции
uv run alembic revision --autogenerate -m "add rooms"
4. применение миграции 
uv run alembic upgrade head

## Напоминание по работе с проектом
### Запуск
- классический вариант: uv run python src/main.py
### UV
- инициализация проекта: uv init --app
- добавление нового пакета: uv add ruff или uv add --dev ruff 
- синхронизация: uv sync
### RUFF 
- исправление ошибок: uv run ruff check src/ --fix
- форматирование: uv run ruff format src/