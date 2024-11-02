#!/bin/bash

# Запускаем tcpdump в фоновом режиме
tcpdump -i eth0 -w /var/log/tcpdump/traffic.pcap &

# Запускаем основной процесс контейнера (nginx)
nginx -g "daemon off;"

