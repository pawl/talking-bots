#-*- coding: utf-8 -*-

import os
import re
from chatterbotapi import ChatterBotFactory, ChatterBotType
from logmanager import LogManager


class Bot():
    def __init__(self, name, bottype, lang="en", pandoraid=""):
        self.bottypestr=bottype
        if bottype=="cleverbot":
            self.bottype=ChatterBotType.CLEVERBOT
        elif bottype=="jabberwacky":
            self.bottype=ChatterBotType.JABBERWACKY
        elif bottype=="pandorabots":
            self.bottype=ChatterBotType.PANDORABOTS

        factory = ChatterBotFactory()

        self.pandoraid=pandoraid
        self.name=name
        self.session=factory.create(self.bottype,self.pandoraid).create_session()
        self.lang=lang

    def think(self, text):
        return self.session.think(text)

def htmlsil(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def soyle(who,text,lang):
    text=htmlsil(text)
    logManager.writeLog(who+"\t\t> "+text)
    print who+"> "+text
    seslendir(text,lang)
    pass

def seslendir(text,lang):
    os.system('python tts_google.py "'+text+'" '+lang+' 2>/dev/null');

logManager=LogManager()

factory = ChatterBotFactory()

bot=[]

os.system("clear");

for x in range(2):
    pandoraid="b0dafd24ee35a477"
    name = raw_input(str(x+1)+". botun adı: ")

    bottypeno = raw_input(name+" isimli botun tipi [1:cleverbot/2:pandorabots/3:jabberwacky]: ")
    if bottypeno=="1":
        bottype="cleverbot"
    elif bottypeno=="2":
        bottype="pandorabots"
    elif bottypeno=="3":
        bottype="jabberwacky"

    if bottype=="pandorabots":
        pandoraidraw = raw_input(name+" isimli botun pandora no'su (varsayılan:b0dafd24ee35a477): ")
        if pandoraidraw.strip()!="": pandoraid=pandoraidraw

    langno = raw_input(name+" isimli botun dili [1:en-US(kadın)/2:en-GB(erkek)]: ")
    if langno=="1":
        lang="en-US"
    elif langno=="2":
        lang="en-GB"

    bot.append(Bot(name,bottype,lang,pandoraid))

os.system("clear")
for x in range(2):
    pandoraidraw=""
    if bot[x].bottypestr=="pandorabots":pandoraidraw="("+bot[x].pandoraid+")"
    print(bot[x].name+" isimli bot "+bot[x].bottypestr+pandoraidraw+" tipi bottur.")

print("------------------------")

print("Şimdi iki bot arasında bir konuşma başlatılacak. Botların birbirleriyle konuşabilmeleri için diyalog'u "+bot[0].name+" ağızından sizin başlatmanız gerekmetedir.")
s = raw_input(bot[1].name+" diyaloga nasıl başlasın?: ")

soyle(bot[1].name, s,bot[1].lang)

while (1):
    
    for x in range(2):
        s = bot[x].think(s);
        soyle(bot[x].name, s,bot[x].lang)