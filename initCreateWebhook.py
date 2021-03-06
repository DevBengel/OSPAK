#Dieses Programm ist am Anfang eines Tages einmalig auszuführen- oder wenn sich die ngrok URL geändert hat
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import os 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
def createWebhook(roomId):
    access_token = os.getenv("ACCESSTOKEN")
    ngrokurl = os.getenv("NGROKURL")
    prefix = os.getenv("CLASSPREFIX")
    webhookname = "Teams API Kurs"
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    apiUrl = "https://api.ciscospark.com/v1/webhooks/"
    body = {"name" : str(prefix) +' '+ webhookname, "targetUrl" : ngrokurl, "resource" : "messages","filter":"roomId="+roomId,"event":"created"}

    response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

    data=json.loads(response.text)
    #print(response.status_code)
    #print(response.text)
    return (str(data['id']),str(data['name']))
