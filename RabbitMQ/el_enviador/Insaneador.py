import pika
import time

print("🐇 Insaneador despertando...")

# Intentos infinitos para conectar al broker Rabbit
while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbit',
                port=5672,
                credentials=pika.PlainCredentials('MAXI', 'MAXI')
            )
        )
        print("🐇 Conejo encontrado, enviando 💌")
        break
    except pika.exceptions.AMQPConnectionError:
        print("🐇 Conejo dormido, retry en 5s 🫠")
        time.sleep(5)

channel = connection.channel()
channel.queue_declare(queue='insane_queue')

# Bucle infinito para SPAMEAR mensajes
contador = 1
while True:
    mensaje = f"Holi insaneado 🫶✨🐇 msg#{contador}"
    channel.basic_publish(exchange='',
                          routing_key='insane_queue',
                          body=mensaje)
    print(f" [x] Enviado: {mensaje}")
    contador += 1
    time.sleep(2)  # cada 2 segundos
