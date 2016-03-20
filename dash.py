# coding=utf-8
from googlevoice import Voice
from googlevoice.util import input
from scapy.all import *
import httplib, urllib
import time
import datetime

sms_message = "Mom, I have a 💩!"  # SMS message
sms_number = ""                    # Phone Number for SMS. Ex: "1234567890"
google_account = ""                # Google Account. Ex: "user@gmail.com"
google_password = ""               # Google Account password. Ex: "password"
dash_mac_address = "*"             # filter on mac address. Ex: "74:75:48:19:79:1d"

def sms_gvoice(account, password, number, message):
	voice = Voice()
	voice.login(account, password)
	voice.send_sms(number, message)
	return;

def arp_display(pkt):
	if pkt[ARP].op == 1:
		if pkt[ARP].psrc == '0.0.0.0':
			if dash_mac_address == "*" or dash_mac_address == pkt[ARP].hwsrc:
				t = time.time()
				dt = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
				print dt + " sms sent to " + sms_number + " - " + pkt[ARP].hwsrc
				sms_gvoice(google_account, google_password, sms_number, sms_message)
	return;

print sniff(prn=arp_display, iface="wlan0",filter="arp",store=0)
