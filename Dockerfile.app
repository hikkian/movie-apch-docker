FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Системные зависимости
RUN apt-get update && \
    apt-get install -y build-essential gcc wget curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем Python-код
COPY app/ /app/app/
COPY entrypoint.sh /app/entrypoint.sh

# Делаем скрипты исполняемыми
RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/app/*.py

CMD ["/app/entrypoint.sh"]
