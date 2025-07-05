from scapy.all import *

IFACE = "eth0"
FILTER = "tcp port 5672"

def fuzz(packet):
    if packet.haslayer(Raw):
        print(f"👀 ORIGINAL: {packet.summary()}")
        # Mini fuzz: reemplaza texto, o corrompe bits, tu delirio
        if b"hello" in packet[Raw].load:
            packet[Raw].load = packet[Raw].load.replace(b"hello", b"VIRUS!!!")
        send(packet)
        print(f"💥 MODIFICADO: {packet.summary()}")

print(f"🔥 Sniffing en {IFACE} filtrando {FILTER}")
sniff(iface=IFACE, filter=FILTER, prn=fuzz)
