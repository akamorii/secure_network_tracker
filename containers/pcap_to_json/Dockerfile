FROM debian:latest

RUN apt update && apt install -y tshark

RUN tshark -r /app/data/traffic.pcap -T json > traffic.json
