# encoding: UTF-8
from bottle import get, run, template
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
from webbrowser import open_new_tab
from demoEngine import MainEngine
import json,time

cs = set()
me = set()
account = dict()

def ws_ctpaccount(data):
    global account
    account = json.loads(data)
    for one in account:
        me.add(MainEngine(cs,one))

timeskip = 0
def addTimer(data):
    global timeskip
    if time.time()-timeskip>=1:
        timeskip = time.time()
        print("add timer ok")

@get('/')
def index():
    return template('index')

@get('/test')
def sendit():
    for one in cs:
        one.send("123")
    return "ok"

funcs = {
"ws_timer":addTimer,

}

@get('/websocket', apply=[websocket])
def echo(ws):
    cs.add(ws)
    print(1)
    for one in me:
        one.set_ws(cs)
    print(2)
    for one in cs:
        one.send("连接服务器端成功")
    print(3)
    while True:
        msg = ws.receive()
        if msg is not None:
            type_,data_ = msg.split('=')
            if type_ in funcs:funcs[type_](data_)
            print(msg,cs)
            for one in cs:
                one.send(json.dumps({"message":msg}))
        else: break
    print(4)
    cs.remove(ws)
    print(5)
    for one in me:
        one.set_ws(cs)

open_new_tab("ctp.html")
run(host='0.0.0.0', port=8080, server=GeventWebSocketServer)