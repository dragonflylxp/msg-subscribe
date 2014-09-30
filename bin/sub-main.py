#coding:utf-8
#File: sub-main.py
#Auth: lixp(@500wan.com)
#Date: 2014-09-30 15:40:32
#Desc: 


import os
import sys
import time
import getopt
import redis
import ujson

APP_PATH    = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(os.path.join(APP_PATH,'biz'))
sys.path.append(os.path.join(APP_PATH,'lib'))
import configer
from logger import Log

"""常量:业务channels
"""
PRIZE       = "ESUNMSG.ESUN_PRIZE.BONPRIZE"              #派奖
CHASE       = "ESUNMSG.ESUN_PROJECT_V2.FINISH_CHASE"     #追号到期
DRAWMONEY   = "ESUNMSG.ESUN_ACCOUNT_V2.DRAW_MONEY"       #提款
DRAWDONE    = "ESUNMSG.ESUN_ACCOUNT_V2.DRAWMONEY_DONE"   #提款完成
MATCHRESULT = "ESUNMSG.ESUN_LOTTERY.SEND_MATCHRESULT"    #开赛结果
ACTIVATE    = "ACTIVATE"                                 #激活
REG         = "REGISTER"                                 #注册
CHARGE      = "REGCHARGE"                                #充值
channels = [PRIZE, CHASE, DRAWMONEY, DRAWDONE, MATCHRESULT, ACTIVATE, REG, CHARGE]

"""初始化application: conf/log
"""
def init_app(cfgfile):
    confs = configer.JsonConfiger.get_instance()
    try:
        confs.load_file(cfgfile)
    except:
        print "Open config file error! [cfgfile : %s]" % cfgfile  
        sys.exit(0)

    #Log初始化
    Log.set_up(os.path.join(APP_PATH,confs.get("log/logfile")),\
               confs.get("log/logger"))
    global logger
    logger = Log().getLog()

    return confs.get()


def usage():
    print u'''使用参数启动:
    usage: [-c]
    -c <file> ******加载配置文件
    ''' 
    sys.exit(0)

"""消息处理函数
"""
def do_handler(msg):
    if msg['channel'] == PRIZE: 
    elif msg['channel'] == CHASE: 
    elif msg['channel'] == DRAWMONEY: 
    elif msg['channel'] == DRAWDONE: 
    elif msg['channel'] == MATCHRESULT: 
    elif msg['channel'] == ACTIVATE: 
    elif msg['channel'] == REG: 
    elif msg['channel'] == CHARGE: 
    else:
        logger.warning("Unknown channel![ CHANNEL=%s msg=%s ]" % (msg['channel'], msg['data']))


"""总入口
"""
def main():
    #初始化
    cfgfile  = None
    try:
        opts, argvs = getopt.getopt(sys.argv[1:], "c:h") 
        for op, value in opts:
            if   op == '-c':
                cfgfile = value
            elif op == '-h':
                usage()
    except getopt.GetoptError:
        usage()
    confs = init_app(cfgfile)
            
    #订阅redis
    c = confs['servers']['redis']
    r = redis.StrictRedis(host=c['host'], port=c['port'], db=c['db'])
    p = r.pubsub()
    p.subscribe(channels)

    #处理消息
    for msg in p.listen():
        do_handler(msg)

    logger.info("Msg-subscribe stopped!")
    
if __name__ == '__main__':
    main()
