from googlesearch import search
import time
import colorama
from colorama import Fore

print("""
   _,  
  / |                  __        
 / ___,  ____ ___     /' |
 /'   `\,--,/'   `\  /'   |
(       )  (       )'
 \_   _/'  `\_   _/         
                                          
      ~Dorket~
    """)

time.sleep(1)

print(Fore.GREEN + 'Made by BojamaV')

time.sleep(2)

username = input(Fore.RED + 'Enter Google Dork: ')

time.sleep(0.9)

print(Fore.BLUE + 'Processing request...')

time.sleep(1)

search_query=(username)
for i in search(search_query,
    tld='com',
    lang='en',
    num=10000,
    stop=10000,
    pause=2.0):
    print(i)
