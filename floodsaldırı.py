from scapy.all import IP, ICMP, send
import time

target_ip = "192.168.1.1"  

for i in range(10):
    packet = IP(dst=target_ip) / ICMP()

    send(packet, verbose=False)

    print(f"{i+1}. ICMP saldırı paketi gönderildi")

    time.sleep(1)  
