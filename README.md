<!DOCTYPE html>
<html>
<head>

</head>
<body>

<h1>ARPGuard</h1>

<h2>Purpose</h2>

<p>ARPGuard is a Python tool that demonstrates ARP spoofing, a technique used to intercept and redirect network traffic between a target device and a gateway. By sending forged ARP (Address Resolution Protocol) messages, ARPGuard impersonates the IP addresses of the target device and the gateway, tricking them into updating their ARP tables with false mappings between IP addresses and MAC addresses. The primary objective of ARPGuard is to raise awareness about ARP spoofing attacks and their implications for network security. By simulating a real-world attack scenario, ARPGuard helps users understand the vulnerabilities of the ARP protocol and the risks associated with unauthorized access to network traffic. ARPGuard is designed using the Scapy library, a powerful packet manipulation tool, and implements object-oriented programming principles to structure the code efficiently. The tool's architecture includes an ARP Spoofer class that encapsulates the functionalities for ARP spoofing, including sending spoofed ARP responses, restoring the original ARP mappings, and running the attack. This tool is intended for educational and legitimate purposes only, as ARP spoofing is illegal in most countries. Users should ensure they have proper authorization and follow responsible disclosure practices when testing networks with ARPGuard.</p>

<h2>Usage</h2>

<ol>
  <li>Ensure you have Python installed on your system.</li>
  <li>Install the required dependencies by running <code>pip install scapy</code>.</li>
  <li>Run the script with the target IP and gateway IP specified using the <code>--target</code> and <code>--gateway</code> flags respectively.</li>
</ol>

<p><strong>Example:</strong></p>

<pre><code>python arp_guard.py --target TARGET_IP --gateway GATEWAY_IP</code></pre>

<h2>Prerequisites</h2>

<p>To use this script, you must have the IP addresses of the target device and the gateway. Additionally, IP forwarding must be enabled on your system. You can enable IP forwarding by running the following command:</p>

<pre><code>echo 1 > /proc/sys/net/ipv4/ip_forward</code></pre>

<h2>Disclaimer</h2>

<p>This script is provided for educational purposes only. ARP spoofing is a malicious activity and may be illegal in certain jurisdictions. Do not use this script for unauthorized access to networks or for any illegal activities. Always ensure you have proper authorization before using ARPGuard.</p>


</body>
</html>
