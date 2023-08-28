#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import logging
import traceback
import configparser
import socket
import time
import requests

Py_version = sys.version_info
if Py_version < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    import importlib
    importlib.reload(sys)

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

node_name = 'AutoRestartMySQL'
logger=logging.getLogger('autorestartmysql') 

def exprint(x):
    try:
        logger.info(x)
    except Exception as e:
        pass
    print(x)
    
#logger init
try:
    formatter = logging.Formatter('[%(asctime)s %(levelname)-8s] %(message)s')  
    logger.setLevel(logging.INFO)  

    logpath = __file__ + '.log'
    if os.path.exists(logpath): os.remove(logpath)
    handler = logging.FileHandler(logpath)
    handler.setFormatter(formatter)
    logger.addHandler(handler) 
except:
    exprint(traceback.format_exc())

def notify_zhimessenger(text, key):
    global node_name
    
    url = 'https://zhi200.com/api/messenger/push'
    data = '{"level":8,"type":"message","source":"%s","content":"%s","sign":"%s"}' % (node_name, text, key)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, data=data, headers=headers)

def notify_dingtalk_robot(text, key):
    global node_name
    
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (key)
    data = '{"msgtype": "text","text": {"content":"%s\n\n%s"}}' % (node_name, text)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, data=data, headers=headers)

def notify_wechat_webhook(text, key):
    global node_name
    
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s' % (key)
    data = '{"msgtype": "text","text": {"content":"%s\n\n%s"}}' % (node_name, text)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, data=data, headers=headers)

def notify(text, config):
    try:
        logger.info(text)

        channels = config['notify']['channels']
        if len(channels) <= 0: return

        channels = channels.split(',')
        for channel in channels:
            channel = channel.strip()
            if len(channel) <= 0: continue

            channel_type = config[channel]['type']
            key = config[channel]['key']
            
            if len(channel_type) <= 0: continue
            if len(key) <= 0: continue

            # type: zhimessenger / dingtalk_robot / wechat_webhook

            if channel_type == 'zhimessenger':
                notify_zhimessenger(text, key)
                continue

            if channel_type == 'dingtalk_robot':
                notify_dingtalk_robot(text, key)
                continue

            if channel_type == 'wechat_webhook':
                notify_wechat_webhook(text, key)
                continue
    except:
        exprint(traceback.format_exc())

def main():
    global node_name

    config = configparser.ConfigParser()
    config.read('config.ini')
    if len(config['main']['name']) > 0: node_name = config['main']['name']
    addr = (config['mysql']['host'], int(config['mysql']['port']))
    interval = int(int(config['mysql']['interval']))
    if interval <= 10: interval = 60
    if interval > 86400: interval = 86400
    
    while True:
        success = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(addr)
            success = True
        except:
            success = False
        finally:
            sock.close()

        if not success:
            try:
                notify("try to restart command: " + config['mysql']['restart'], config)
                os.system(config['mysql']['restart'])
            except:
                exprint(traceback.format_exc())

        time.sleep(interval)

if __name__ == "__main__":
    try:
        main()
    except:
        exprint(traceback.format_exc())
    os._exit(0)