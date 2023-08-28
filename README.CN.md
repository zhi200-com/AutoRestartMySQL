# AutoRestartMySQL

监控MySQL进程，并自动重启。

项目官网地址：[https://zhi200.com/](https://zhi200.com/cms/kaiyuanxiangmu/164.html)

作者邮箱：[opensource@zhi200.com](mailto:opensource@zhi200.com)

## 配置

生成配置文件：`cp config.ini.cf config.ini`

config.ini文件配置

```
[main]
name=AutoRestartMySQL       # 服务名称，用于消息通知时区分不同服务器

[mysql]
interval=60            # 检查时间间隔
host=127.0.0.1          # MySQL的IP地址
port=3306             # MySQL的端口
restart=service mysql restart  # MySQL重启命令

[notify]
channels=zhimessenger_1,dingtalk_robot_1,wechat_webhook_1       # 通知频道列表，以半角逗号分隔

[zhimessenger_1]
type=zhimessenger               # 通知类型: 支持 zhimessenger（信鸽通知） / dingtalk_robot（钉钉机器人） / wechat_webhook（微信群机器人）
key=                     # 通知密钥
```

## 运行

安装依赖项：`pip install -r requirements.txt`

运行：`python ./autorestartmysql.py`

## 开机自启

### CentOS

`sudo vim /etc/rc.local `

加入如下行：

`cd /[path]/AutoRestartMySQL/src && nohup python ./autorestartmysql.py &`

