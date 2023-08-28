# AutoRestartMySQL

monitor and restart mysql process

Our Website: [https://zhi200.com/](https://zhi200.com/cms/kaiyuanxiangmu/164.html)

Author Email: [opensource@zhi200.com](mailto:opensource@zhi200.com)

## Config

Generate Configuration File: `cp config.ini.cf config.ini`

`config.ini` File Configuration

```
[main]
name=AutoRestartMySQL       # Service name, used to distinguish different servers during message notifications

[mysql]
interval=60            # Check interval
host=127.0.0.1          # The IP address of MySQL
port=3306             # The Port of MySQL
restart=service mysql restart  # MySQL restart command

[notify]
channels=zhimessenger_1,dingtalk_robot_1,wechat_webhook_1       # channels for message notifications, separated by a semicolon

[zhimessenger_1]
type=zhimessenger               # message notifications type: zhimessenger / dingtalk_robot / wechat_webhook
key=                     # message notifications key
```

## Run

Install Dependencies: `pip install -r requirements.txt`

Run: `python ./autorestartmysql.py`

## Autorun

### CentOS

`sudo vim /etc/rc.local `

Add as follows:

`cd /[path]/AutoRestartMySQL/src && nohup python ./autorestartmysql.py &`

