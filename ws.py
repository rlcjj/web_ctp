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

def ws_ctpaccount(data):
    global account
    account = json.loads(data)
    for one in account:
        me.add(MainEngine(cs,one['userid'],one['password'],one['brokerid'],one['mdfront'],one['tdfront']))

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
    print(1)
    for one in me:
        one.set_ws(cs)
    print(2)
    for one in cs:
        one.send("new_guy_coming")
    print(3)
    while True:
        msg = ws.receive()
        if msg is not None:
            type_,data_ = msg.split('=')
            if type_ in funcs:funcs[type_](data_)
            print(msg,cs)
            ws.send("msg_received")
            for one in cs:
                one.send(msg)
        else: break
    print(4)
    cs.remove(ws)
    print(5)
    for one in me:
        one.set_ws(cs)

open_new_tab("ctp.html")
run(host='0.0.0.0', port=8080, server=GeventWebSocketServer)