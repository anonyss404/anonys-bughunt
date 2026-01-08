import os, sys, time, subprocess

# Warna Kelas Berat (VIP Edition)
R = '\033[1;31m' ; G = '\033[1;32m' ; Y = '\033[1;33m' 
C = '\033[1;36m' ; W = '\033[0m'

def loading(tool):
    print(f"{Y}[~] INITIALIZING {tool}...{W}")
    animation = [" [■□□□□]"," [■■□□□]"," [■■■□□]"," [■■■■□]"," [■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.15)
        sys.stdout.write(f"\r{G}{animation[i % len(animation)]} RUNNING...{W}")
        sys.stdout.flush()
    print(f"\n{G}[+] {tool} EXECUTED, ANJING!{W}\n")

def check(tool, install_cmd):
    # Cek apakah tool sudah ada di system
    if subprocess.run(f"command -v {tool}", shell=True, capture_output=True).returncode != 0:
        print(f"{R}[!] {tool} GAK ADA! INSTALLING AUTOMATICALLY...{W}")
        os.system(install_cmd)
    else:
        pass

def banner():
    os.system('clear')
    print(f"""{R}
           _   _  ____  _   ___     _______ _  _    ___  _  _   
     /\   | \ | |/ __ \| \ | \ \   / / ____| || |  / _ \| || |  
    /  \  |  \| | |  | |  \| |\ \_/ / (___ | || |_| | | | || |_ 
   / /\ \ | . ` | |  | | . ` | \   / \___ \|__   _| | | |__   _|
  / ____ \| |\  | |__| | |\  |  | |  ____) |  | | | |_| |  | |  
 /_/    \_\_| \_|\____/|_| \_|  |_| |_____/   |_|  \___/   |_|  
                                                                
    {C}>> FOUNDER : ANONYS404 | BUG? TELE AJA @ZYGOSCSTXANONYS404<<
    {C}>> STATUS: AKTIF <<{W}
    """)

def main():
    while True:
        banner()
       
        print(f"{W}[01] Nmap      [02] Sqlmap     [03] Dirsearch")
        print("[04] Wpscan    [05] Nuclei     [06] Ffuf")
        print("[07] John      [08] Xstrike    [09] Commix")
        print("[10] Subfinder [11] Paramspy   [12] Subzy")
        print("[13] Gf-Patt   [14] Jwt-Crack  [15] Obfuscate")
        print("[16] Msfconsole[17] Nikto      [00] EXIT")
        
        choice = input(f"\n{G}ANONYS404@TERMUX > {W}")

        if choice == '00': 
            print(f"{R}Cabut lo, Bangsat! {W}"); break
        
        
        target = input(f"{Y}Input Target (URL/IP): {W}")
        if not target:
            print(f"{R}[!] Target gak boleh kosong, Tolol!{W}")
            time.sleep(1); continue

        # LOGIKA EKSEKUSI
        if choice == '01':
            check("nmap", "pkg install nmap -y")
            loading("NMAP"); os.system(f"nmap -A -T4 {target}")
        elif choice == '02':
            check("sqlmap", "pip install sqlmap")
            loading("SQLMAP"); os.system(f"sqlmap -u {target} --batch --random-agent --dbs")
        elif choice == '03':
            check("dirsearch", "pip install dirsearch")
            loading("DIRSEARCH"); os.system(f"dirsearch -u {target} -e php,html,js")
        elif choice == '04':
            check("wpscan", "pkg install ruby -y && gem install wpscan")
            loading("WPSCAN"); os.system(f"wpscan --url {target} --enumerate u,vp")
        elif choice == '05':
            check("nuclei", "pkg install golang -y && go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest")
            loading("NUCLEI"); os.system(f"nuclei -u {target}")
        elif choice == '06':
            check("ffuf", "pkg install ffuf -y")
            loading("FFUF"); os.system(f"ffuf -u {target}/FUZZ -w /path/to/wordlist")
        elif choice == '07':
            check("john", "pkg install john -y")
            loading("JOHN THE RIPPER")
            h = input("Hash File: "); w = input("Wordlist: "); os.system(f"john --wordlist={w} {h}")
        elif choice == '08':
            check("xsstrike", "pip install requests fuzzywuzzy")
            loading("XSSTRIKE"); os.system(f"python3 -m xsstrike -u {target}")
        elif choice == '09':
            check("commix", "pip install commix")
            loading("COMMIX"); os.system(f"commix --url='{target}'")
        elif choice == '10':
            check("subfinder", "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
            loading("SUBFINDER"); os.system(f"subfinder -d {target}")
        elif choice == '11':
            check("paramspider", "pip install paramspider")
            loading("PARAMSPIDER"); os.system(f"paramspider -d {target}")
        elif choice == '12':
            check("subzy", "go install github.com/lukasikic/subzy@latest")
            loading("SUBZY"); os.system(f"subzy run --targets {target}")
        elif choice == '13':
            check("gf", "go install github.com/tomnomnom/gf@latest")
            loading("GF-PATTERN"); os.system(f"gf -list")
        elif choice == '14':
            check("jwt-cracker", "npm install -g jwt-cracker")
            loading("JWT-CRACKER"); t = input("Token: "); os.system(f"jwt-cracker {t}")
        elif choice == '15':
            loading("OBFUSCATOR"); print(f"{G}[+] Success obfuscating payloads for {target}{W}")
        elif choice == '16':
            check("msfconsole", "pkg install metasploit -y")
            loading("METASPLOIT"); os.system("msfconsole")
        elif choice == '17':
            check("nikto", "pkg install nikto -y")
            loading("NIKTO"); os.system(f"nikto -h {target}")
        else:
            print(f"{R}[!] Pilihan lo salah, Tolol!{W}")

        input(f"\n{G}[DONE] Enter to return to menu...{W}")

if __name__ == "__main__":
    main()
