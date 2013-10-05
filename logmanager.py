import os
import time

class LogManager(object):
    __logfile=""
    __logdir=""
    __dateformat=""
    def __init__(self,logfile="",logdir="logs/",dateformat="%d.%m.%Y %H:%M:%S"):

        if logfile=="":
            logfile=time.strftime(dateformat, time.localtime())

        self.__logfile=logfile
        self.__dateformat=dateformat
        self.__logdir=logdir

        if not os.path.exists(self.__logdir):
            os.makedirs(self.__logdir)

        f = open(self.__logdir+logfile,'w')
        f.write('')
        f.close()

    def writeLog(self,text):
        f = open(self.__logdir+self.__logfile,'a')
        f.write(time.strftime(self.__dateformat, time.localtime())+" - "+text+"\n")
        f.close()