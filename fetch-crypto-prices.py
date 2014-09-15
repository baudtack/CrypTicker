#!/usr/bin/python

import requests
import json
from gi.repository import Notify, GLib
import webbrowser

currency = "DOGE"
market = "BTC"

url = "https://api.mintpal.com/v1/market/stats/" + currency + "/" + market

r = requests.get(url)

data = json.loads(r.text)[0]

color = "blue";

if data["change"][0] == "+":
    color = "green"
elif data["change"][0] == "-":
    color = "red"
    

msg = data["code"] + " last at <span  color=\"" + color + "\">" + data["last_price"] + "</span> " + market
    
Notify.init("CrypTicker")
Notify.Notification.new('CrypTicker', msg, 'dialog-information').show()
