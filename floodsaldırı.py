from scapy.all import IP, ICMP, send
import time

target_ip = "192.168.1.100"  # Test makinenizin IP'si

for i in range(10):
    packet = IP(dst=target_ip) / ICMP()

    send(packet, verbose=False)

    print(f"{i+1}. ICMP paketi gönderildi")

    time.sleep(1)  # Saniyede 1 paket