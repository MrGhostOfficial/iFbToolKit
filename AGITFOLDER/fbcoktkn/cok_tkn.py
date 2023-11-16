#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Decompile by MrGhostOfficial:)
# uncompyle6 version 3.7.4
# Decompiler: mardis
# Python version 3.11.4
# Python2 version 2.7.18 (default, 2023-06-14 13:42:04.103358
import requests, re, os, sys
print('\n\x1b[0m** \x1b[1;31m< \x1b[1;37mGET FB ACCESS TOKEN FROM COOKIE \x1b[1;31m> \x1b[1;37m**\n\x1b[0m')
cookie = input('Input Cookie?\x1b[1;31m: \x1b[1;33m')
try:
    data = requests.get('https://business.facebook.com/business_locations', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # don't change this user agent.
        'referer'                   : 'https://www.facebook.com/',
        'host'                      : 'business.facebook.com',
        'origin'                    : 'https://business.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
    }, cookies = {
        'cookie'                    : cookie
    })
    find_token = re.search('(EAAG\w+)', data.text)
    results    = '\n\x1b[0m* \x1b[1;37mFail \x1b[1;30m: \x1b[1;31mMaybe your cookie invalid\x1b[1;37m!\x1b[0m' if (find_token is None) else '\n\x1b[0mFb access token\x1b[1;31m: \x1b[1;32m' + find_token.group(1)
except requests.exceptions.ConnectionError:
    results    = '\n\x1b[0m* \x1b[1;37mFail \x1b[1;30m: \x1b[1;31mNo connection error\x1b[1;37m!\x1b[0m'
except:
    results    = '\n\x1b[0m* \x1b[1;37mFail \x1b[1;30m: \x1b[1;31mUnknown errors, please try again\x1b[1;37m!\x1b[0m'

print(results)
