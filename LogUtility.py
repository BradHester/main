__author__ = 'Brad_PC'
import datetime

def writelog(message):
    f = open('Log.txt','a')
    y= datetime.datetime.now()
    #print(y.strftime('%d/%m/%Y'))
    #print(" - " + y.strftime('%H:%M:%S'))
    #print(' - ' + message)
    x= y.strftime('%d/%m/%Y') + ' - ' + y.strftime('%H:%M:%S') + ' - ' + message + "\n"
    print (x)
    f.write(x)
    f.close() # you can omit in most cases as the destructor will call it