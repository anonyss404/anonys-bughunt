#!/bin/bash
echo -e "\e[1;32m[+] SETTING UP ANONYS-BUGHUNT ENVIRONMENT...\e[0m"
pkg update && pkg upgrade -y
pkg install python ruby golang php git nmap -y
pip install -r requirements.txt
chmod +x anonys404.py
echo -e "\e[1;32m[+] SEMUA SIAP, BANGSAT! JALANKAN: python anonys404.py\e[0m"
