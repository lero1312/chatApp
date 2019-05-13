from dataBase.dataBase import *
from time import sleep
send = 1
arrive = 2
read = 3

w = userCol.watch()
print(w.next())