# Tarea 3 - Taller de Redes y Servicios

Este repositorio contiene todo lo necesario para **capturar, modificar e inyectar tráfico** entre un **servidor** y un **cliente** que se comunican usando el protocolo **AMQP**, usando **Scapy** como única arma de destrucción masiva 🕷️💥.

- Scripts para **interceptar paquetes**.
- Ejemplos de **inyección y modificación** en tiempo real.
- Dockerfile's para **replicar el entorno** desde cero.
- Un informe academico para entender qué pasó, por qué pasó y por qué probablemente todo salió mal igual.

## 📁 Estructura de carpetas

```plaintext
RabbitMQ/
├── docker-compose.yml        # Define y configura los servicios del cliente y servidor en contenedores
├── el_enviador/              # Contenedor que funciona como cliente/emisor
│   ├── Dockerfile
│   └── Insaneador.py         # Script para generar y enviar tráfico AMQP
├── el_espameado/             # Contenedor que funciona como servidor/receptor
│   ├── Dockerfile
│   └── Insaneado.py          # Script para recibir y procesar los mensajes
└── README.md                 # Documentación del proyecto
```
## 🚀 Cómo levantar los servicios en Ubuntu

Para correr este proyecto necesitas tener **Docker** instalado en tu máquina.

### ✅ Verificar instalación

Primero revisa si Docker ya está instalado:

```bash
docker --version
