# encoding: UTF-8
from ws import *
open_new_tab("ctp.html")
run(host='0.0.0.0', port=8080, server=GeventWebSocketServer)