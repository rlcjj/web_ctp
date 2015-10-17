# encoding: UTF-8
from bottle import get, run, template
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
from webbrowser import open_new_tab
from demoEngine import MainEngine
import json,time,shelve,os
from string import lowercase as _chars

cs = set()
me = {}
STORE = "local_store"

def make_plus(accountid):
    o = ''
    for one in accountid:
        o = o+_chars[int(one)]
    return o

def ws_ctpaccount(data):
    global account
    account = json.loads(data)
    _store = shelve.open(STORE)
    _store['ctp_account'] = account
    _store.close()
    for k,v in account.items():
        if k not in me:
            _plus = make_plus(v['userid'])
            me[k] = MainEngine(cs,v,_plus)
            print("account "+k+" started")

def ws_getinstrument(data):
    for one in me.values():
        one.sub_instrument(data)

timeskip = 0
def addTimer(data):
    global timeskip
    if time.time()-timeskip>=1:
        timeskip = time.time()
        for one in me.values():
            one.addEventTimer()

@get('/')
def index():
    return template('index')

@get('/test')
def sendit():
    for one in cs:
        import shelve,json
        f = shelve.open("debug_event_types")
        for _ee in f.values():
            one.send(json.dumps(_ee))
        f.close()
    return "ok"

funcs = {
"ws_ctpaccount":ws_ctpaccount,
"ws_getinstrument":ws_getinstrument,
}

@get('/websocket', apply=[websocket])
def echo(ws):
    cs.add(ws)
    for one in me.values():
        one.set_ws(cs)
    while True:
        msg = ws.receive()
        if msg is not None:
            type_,data_ = msg.split('=')
            if type_ in funcs:
                funcs[type_](data_)
            else:
                print(msg,cs)
        else: break
    cs.remove(ws)
    for one in me.values():
        one.set_ws(cs)

open_new_tab("ctp.html")
run(host='0.0.0.0', port=8080, server=GeventWebSocketServer)