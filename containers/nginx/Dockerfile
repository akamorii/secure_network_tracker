# Dockerfile
FROM nginx:latest

# Устанавливаем tcpdump
RUN apt update && apt install -y tcpdump

# Создаем каталог для логов
RUN mkdir -p /var/log/tcpdump

# Копируем стартовый скрипт
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Устанавливаем скрипт как команду для запуска
CMD ["/usr/local/bin/start.sh"]

COPY nginx.conf /etc/nginx/nginx.conf