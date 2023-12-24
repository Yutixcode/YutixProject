import random
import argparse
import tldextract
import requests as req
req.urllib3.disable_warnings()
from colorama import Fore,Style
from bs4 import BeautifulSoup as bs

red	= Fore.RED
yellow = Fore.YELLOW
blue   = Fore.BLUE
bold   = Style.BRIGHT
green  = Fore.GREEN
white  = Fore.WHITE
dim	= Style.DIM
purple = Fore.MAGENTA
cyan   = Fore.CYAN
reset  = Style.RESET_ALL+white

def header(judul):
	print(fr"""{reset}{bold}
{cyan}      /\
{cyan} __  / /     __  _       {purple}______          __   
{cyan} \ \/ /__ __/ /_(_)  ___{purple}/ ____/_________/ /__/\
{cyan}  \  /  // / __/\  \/  {purple}/ /   / __  / __  / {red}_{purple}  /
{cyan}  / /  // / /_/ />   <{purple}/  \__/ /_/ / /_/ /  __/{red}_
{cyan} / /\__,_/\__/_/__/\__{purple}\____/_____/___,_/____/{red} /_
{cyan} \/                {red}/ _ \/ __/ _ \/ / -_) __/ __/
     {reset}just trash{bold}   {red}/ .__/_/  \___/ /\__/\__/\__/
   {reset}collections{bold}   {red}/_/         |___/              


 {reset}{judul}{dim}
   
   t.me/yutixverse | github.com/Yutixcode
   fb.me/njnk.xnxx | yutixcode@gmail.com
   {reset}""") # Banner version: 1.3

