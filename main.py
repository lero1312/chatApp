from dataBase.dataBase import *
from time import *
from var import *


def register(name, age, phone):
    x = userCol.find_one({"phone": phone})
    if not x:
        return userCol.insert_one({"name": name, "age": age, "phone": phone}).inserted_id
    else:
        print("the Phone number is already existed")


def login(phone):
    x = userCol.find_one({"phone": phone})
    if x:
        print("welcome ;) " + x["name"])
        return x["_id"]
    else:
        print("not founded")


def sendMessage(sender, to, text):
    x = messageCol.insert_one({"from": sender, "to": to, "body": text, "time": time(), "stat": send})
    if not x.inserted_id:
        print("not sent")


def getIdByName(name):
    x = userCol.find_one({"name": name})
    if x:
        return x["_id"]
    else:
        print("not founded")


curid = 0


def printAllFriends():
    r = userCol.find({"_id": {"$ne": curid}}, {"name": 1})
    indx = 0
    for i in r:
        print('' + str(indx) + ' ' + i['name'])
        indx += 1


def printChat(to):
    chat = messageCol.find({"$or": [{"from": curid}, {"from": to}]})
    for i in chat:
        if i["from"] == curid:
            print('\t\t\t' + i['body'])
        else:
            print(i['body'])


print("HI Welcome to my chat app >> its beta :(")
x = int(input("press 1 for register \npress 2 for login\n"))
if x == 2:
    curid = login(input("phone : "))
else:
    curid = register(input("inter your name : "), int(input("inter your age : ")), input("your phone : "))
while 1:
    printAllFriends()
    list = userCol.find({"_id": {"$ne": curid}})
    to = list[int(input("chose one : "))]['_id']
    printChat(to)
    x = int(input("press 1 for send message, 2 for back\n"))
    while x == 1:
        text = input()
        sendMessage(curid, to, text)
        printChat(to)
        x = int(input("press 1 for send message, 2 for back\n"))
