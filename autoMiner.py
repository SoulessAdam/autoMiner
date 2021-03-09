import requests
import time
import random
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("AutoMiner - Running // By Adam 774")


def updateTitle(job):
    ctypes.windll.kernel32.SetConsoleTitleW("AutoMiner - Running // "+job+" // By Adam 774")


def mine():
    updateTitle("Running Commands (\"s.mine\")")
    jsonMsg["content"] = "s.mine"
    return requests.post(url=url1, json=jsonMsg, headers=auth)


def announceDelay(d):
    jsonMsg["content"] = "```fix\n[-] Sleeping for "+str(d)+"s at "+time.strftime("%H:%M:%S", time.localtime())+"...\n```"
    requests.post(url=url1, json=jsonMsg, headers=auth)


def checkPost(request1):
    if request1.status_code == 200:
        print("["+time.strftime("%H:%M:%S", time.localtime())+"] Success on sending", jsonMsg["content"])
    else:
        print("Failed:")
        print(f"Headers Sent: {request1.headers}")
        print(f"Content Returned: {request1.content}")


jsonMsg = {"content": "```ini\n[Starting "+time.strftime("%H:%M:%S", time.localtime())+"]\n```"}
url1 = "https://discord.com/api/v8/channels/{Channel Num/ID Here}/messages"
auth = {"Authorization": "{AUTH TOKEN HERE}"}
# requests.post(url=url1, json=jsonMsg, headers=auth)  # Uncomment me for an message on start.


while True:
    checkPost(mine())
    delay = random.randint(30, 45)
    updateTitle("Waiting for " + str(delay) + " seconds")
    print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] Waiting " + str(delay) + "s")
    # announceDelay(delay)  # Uncomment me for announcement of delays.
    print("-" * 119)
    time.sleep(delay)
