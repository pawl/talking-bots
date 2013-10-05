import os
import re
from chatterbotapi import ChatterBotFactory, ChatterBotType
from logmanager import LogManager

def htmlsil(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def soyle(who,text,langid):
    text=htmlsil(text)
    logManager.writeLog(who+"\t\t> "+text)
    print who+"> "+text
    seslendir(text,langList[langid])
    pass

def seslendir(text,lang):
    os.system('python tts_google.py "'+text+'" '+lang+' 2>/dev/null');

logManager=LogManager()

langList=["en","en-GB"]

factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.CLEVERBOT)
bot2session = bot2.create_session()

s = 'Hello dear.'
while (1):
    
    soyle('Cleverbot', s,0)

    s = bot2session.think(s);
    soyle('Chomsky', s,1)

    s = bot1session.think(s);