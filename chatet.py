import os
from chatterbotapi import ChatterBotFactory, ChatterBotType
import time

f = open('chatlog.txt','w')
f.write('')
f.close()

t=0.5
lang=["en-GB","en"]

def yaz(who,text,id):
    f = open('chatlog.txt','a')
    f.write(who+'> '+text+'\n')
    f.close()
    print who+'> '+text
    os.system('python tts_google.py "'+text+'" '+lang[id]+' 2>/dev/null');
    pass

factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()

s = 'What is purpose of life?'
while (1):
    
    yaz('Cleverbot', s,0)
    
    s = bot2session.think(s);
    #time.sleep(t)
    yaz('Chomsky', s,1)
    
    s = bot1session.think(s);
    #time.sleep(t)