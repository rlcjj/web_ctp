# encoding: UTF-8

'''
本文件仅用于存放对于事件类型常量的定义。

由于python中不存在真正的常量概念，因此选择使用全大写的变量名来代替常量。
这里设计的命名规则以EVENT_前缀开头。

常量的内容通常选择一个能够代表真实意义的字符串（便于理解）。

建议将所有的常量定义放在该文件中，便于检查是否存在重复的现象。
'''


EVENT_TIMER = 'eTimer_'                  # 计时器事件，每隔1秒发送一次
EVENT_LOG = 'eLog'                      # 日志事件，通常使用某个监听函数直接显示

EVENT_TDLOGIN = 'eTdLogin'                  # 交易服务器登录成功事件

EVENT_TICK = 'eTick'                        # 行情推送事件
EVENT_TICK_JUST = 'eTick.'                        # 行情推送事件

EVENT_TRADE = 'eTrade'                      # 成交推送事件
EVENT_TRADE_JUST = 'eTrade.'                      # 成交推送事件

EVENT_ERROR = 'eError'                      # Error推送事件

EVENT_ORDER = 'eOrder'                      # 报单推送事件
EVENT_ORDER_JUST = 'eOrder.'                      # 报单推送事件

EVENT_POSITION = 'ePosition'                # 持仓查询回报事件

EVENT_INSTRUMENT = 'eInstrument_'            # 合约查询回报事件
EVENT_PRODUCT = 'eProduct'                      # 合约品类更新
EVENT_INSTRUMENT_DETAIL = 'eInstrumentDetail'  # 合约查询
EVENT_INVESTOR = 'eInvestor'                # 投资者查询回报事件
EVENT_ACCOUNT = 'eAccount'                  # 账户查询回报事件
