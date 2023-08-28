# AutoRestartMySQL

monitor and restart mysql process

## Run

Install Dependencies: `pip install -r requirements.txt`
Run: `python ./AutoRestartMySQL.py`

## Config

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

## Autorun

### CentOS

`sudo vim /etc/rc.local `
Add as follows:
`cd /[path]/AutoRestartMySQL/src && python ./AutoRestartMySQL.py`

