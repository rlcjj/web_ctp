from bottle import get, run, template
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
from webbrowser import open_new_tab
from demoEngine import MainEngine
import json

cs = set()
me = set()
account = dict()
funcs = dict()

@get('/')
def index():
    return template('index')

@get('/test')
def sendit():
    for one in cs:
        one.send("123")
    return "ok"

@get('/websocket', apply=[websocket])
def echo(ws):
    cs.add(ws)
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else: break

open_new_tab("ctp.html")
run(host='0.0.0.0', port=8080, server=GeventWebSocketServer)