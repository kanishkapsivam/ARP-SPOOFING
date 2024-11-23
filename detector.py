# ARP Spoofing Detector
from scapy.all import sniff, ARP

# Mapping of legitimate IPs to their MAC addresses (for detection)
legitimate_macs = {
    "192.168.1.20": "00:11:22:33:44:55"  # User B's legitimate MAC
}

# ARP packet handler function
def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP reply
        ip_src = packet[ARP].psrc
        mac_src = packet[ARP].hwsrc

        # Check if the IP is in our known list of legitimate users
        if ip_src in legitimate_macs:
            real_mac = legitimate_macs[ip_src]
            
            if real_mac != mac_src:
                print(f"[!] ARP spoof detected! IP: {ip_src} has MAC: {mac_src}, but should be: {real_mac}")
            else:
                print(f"[+] Legitimate ARP response from {ip_src} with MAC: {mac_src}")

# Sniff ARP packets on the network
if __name__ == "__main__":
    print("Starting ARP spoof detection...")
    sniff(filter="arp", prn=detect_arp_spoof, store=0)
