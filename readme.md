<p align="center">
  <a href="https://github.com/we-worker/BugBot"><img src="https://bkimg.cdn.bcebos.com/pic/8ad4b31c8701a18b45376361902f07082938fec4?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg" width="200" height="170" alt="go-cqhttp"></a>
</p>


<div align="center">

# Bug-QQ机器人

 基于[YesRot](https://github.com/Yang9999999/Go-CQHTTP-YesBot) [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，使用[OneBot](https://github.com/howmanybots/onebot)标准的插件 

</div>


---

感谢@[Go-CQHTTP-YesBot](https://github.com/Yang9999999/Go-CQHTTP-YesBot)项目，这个项目的大框架都是基于YesBot完成的。

## 在YesBot上的修改
- 修改群聊天方式，不需要@
- 修改端口监听为websocket(原始方式在我的服务器上出现端口占用问题)
- 加入一点新功能
- 调整setu API,为更新后的V2版本。
- 其他

## 目前拥有的功能

- 发送 "setu" 返回一张涩图
- 检测关键字禁言
- 私聊调教对话a+b
- 发送 "每日运势" 返回用户的每日运势
- 更多功能待开发....

## 配置

配置信息在**config.json**中

```json
{
    "ban_words":[], 
    "group":[],
    "self_qq":""
}
```

分别为 

- 禁言关键词
- 管理的群号
- 的QQ号

## API

- 机器人采用的[涩图API](https://api.lolicon.app/#/setu)

## 编写目的

用于python学习和交流
轰炸某一个莫名失踪的genius



## 文档




## 使用教程
- 首先需要先配置好[go-cqhttp](https://github.com/Mrs4s/go-cqhttp/releases)它的[使用教程](https://docs.go-cqhttp.org/guide/quick_start.html),请注意，配置时，请输入12，即http与正向websocket
- 再下载本项目可以git clone的形式下载。
- 配置好必要的文件**config.json**,
- 建立与**go-cqhttp**的websocker连接，需要配置**main.py**里的
  ```
    填写自己在go-cqhttp中设置的连接和端口
    ws = CG_Client('ws://127.0.0.1:6700')
  ```
- 如果报错，可能是python3里面的一些库您没有装过，要不您根据报错信息手动一下。
- 装完库应该就正常运行了吧,呜呜呜，要是出问题了，我也不是很清楚了，不要骂我。
