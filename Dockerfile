FROM python:3.10-slim

# Отключаем pyc-файлы и буферизацию
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория
WORKDIR /app

# Обновляем пакетный менеджер, ставим curl, сертификаты и т.д.
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Ставим Poetry через скрипт (рекомендуемый способ)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH (скрипт по умолчанию ставит бинарь в ~/.local/bin)
ENV PATH="/root/.local/bin:$PATH"

# (Опционально) Обновляем pip
RUN pip install --no-cache-dir --upgrade pip

# Копируем pyproject.toml / poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости (без установки самого проекта как пакета)
RUN poetry install --no-root --no-interaction --no-ansi

# Копируем исходники
COPY src/ ./src/

EXPOSE 8000

# Запуск FastAPI через poetry+uvicorn
CMD ["poetry", "run", "uvicorn", "src.digital_store.main:app", "--host", "0.0.0.0", "--port", "8000"]
