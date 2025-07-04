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

Primero revisa si Docker ya está instalado, si Docker está instalado, este comando debería mostrar la versión
```bash
docker --version
```
## Si no lo tienes, sigue estos pasos para instalarlo limpio
### 1️⃣ Elimina versiones previas (opcional pero recomendado)
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
### 2️⃣ Actualiza los paquetes del sistema
```bash
sudo apt update -y
```

### 3️⃣ Agrega la clave GPG oficial de Docker
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```


 ### 4️⃣ Agrega el repositorio oficial de Docker
 ```
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

### 5️⃣ Instala Docker y sus herramientas
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 6️⃣ Verifica que funciona
```
sudo docker run hello-world
```

💥 **¿No funcionó?**  
Si algo salió mal, tu PC explotó, o simplemente quieres asegurarte de no romper nada más, revisa la **documentación oficial de Docker** 👉[Instalación de Docker](https://docs.docker.com/engine/install/)

## 🧪 Instalación y Ejecución

### 📥 Clonar el repositorio
```bash
git clone https://github.com/maxxee1/amqp-scapy-injection
cd RabbitMQ
```

### 🚀 Iniciar el tráfico
Construye e inicia los contenedores definidos en docker-compose.yml
```bash
sudo docker compose build
sudo docker compose up
```


## 📦 Comandos Disponibles

| Comando | Descripción |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|
| `sudo docker compose down -v --rmi all` | Detiene y elimina los contenedores, volúmenes y todas las imágenes construidas para limpiar todo el entorno. |
| `docker ps` | Muestra todos los contenedores que están corriendo actualmente. |
| `docker system prune` | Elimina contenedores, redes y volúmenes que no se estén usando para liberar espacio y evitar basura acumulada. |
















