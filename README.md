DooDooDash
==========

DooDooDash is a simple Raspberry Pi project that allows sending a text message using an Amazon Dash button. When the Amazon button is pressed, it sends an ARP request which the Raspberry Pi will intercept using Scapy. Once it sees this request, it uses pygooglevoice to send an SMS through google voice. Check out the youtube video for this: https://youtu.be/SA5eTOCDVJU

**UPDATE (7/15/17): This is currently broken. Currently I'm not able to get the ARP request from the Dash button which should look like it originates from an IP 0.0.0.0. Currently debugging and trying to figure this out. I've tried Scapy 2.3.1, 2.3.2, 2.3.3.**

Hardware Requirements
=====================
* [Amazon Dash Button](http://www.amazon.com/gp/product/B00WJ12MQ8/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00WJ12MQ8&linkCode=as2&tag=raka00-20&linkId=ZPBGTMJTND2IZGWB)
* [Rasperry Pi 3](http://www.amazon.com/gp/product/B01CD5VC92/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B01CD5VC92&linkCode=as2&tag=raka00-20&linkId=IMRGVIJJQ7YLWUSK)

Instructions
============
+ Create a [Google Voice account](https://www.google.com/voice)
+ Enable Less Secure Apps for your [Google Account](https://www.google.com/settings/security/lesssecureapps)
+ Startup your Raspberry Pi, connect it to your network
+ On your Raspberry Pi, install Scapy and tcpdump (Note instructions simplified from the original youtube post)

  ```
  sudo pip install scapy==2.3.1
  sudo apt-get install tcpdump
  ```
+ Download this repo to your Raspverry Pi

  ```
  git clone https://github.com/HackerDad/DooDooDash.git
  ```
+ Update DooDooDash.py with your phone number and google account settings

  ```
  sms_message = "Mom, I have a 💩!"  # SMS message
  sms_number = ""                    # Phone Number for SMS. Ex: "1234567890"
  google_account = ""                # Google Account. Ex: "user@gmail.com"
  google_password = ""               # Google Account password. Ex: "password"
  dash_mac_address = "*"             # filter on mac address. Ex: "74:75:48:19:79:1d"
  ```
+ Run the program

  ```
  sudo python dash.py
  ```
+ Dash away!
