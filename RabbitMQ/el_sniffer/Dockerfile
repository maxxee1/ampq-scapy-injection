FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y tcpdump libpcap-dev iproute2 iputils-ping && \
    pip install scapy

COPY modificador.py .

CMD ["python", "modificador.py"]

