
import json
from ws4py.client.threadedclient import WebSocketClient
from send_message.send_message import send_message
from massage_flide import msg_talker

talker = msg_talker()
print("start")

def decete(rev): #接受到后检测
    if rev["post_type"] == "message":
        #print(rev) #需要功能自己DIY
        if rev["message_type"] == "private": #私聊
            talker.private_msg(rev)
        elif rev["message_type"] == "group": #群聊
            talker.group_msg(rev)
        else:
            return 0
    elif rev["post_type"] == "notice":
        if rev["notice_type"] == "group_upload":  # 有人上传群文件
            return 0
        elif rev["notice_type"] == "group_decrease":  # 群成员减少
            return 0
        elif rev["notice_type"] == "group_increase":  # 群成员增加
            return 0
        else:
            return 0
    elif rev["post_type"] == "request":
        if rev["request_type"] == "friend":  # 添加好友请求
            pass
        if rev["request_type"] == "group":  # 加群请求
            pass
    else:  # rev["post_type"]=="meta_event":
        return 0

#解析接受到的信息，转化为json
def recv_to_json(msg):
    for i in range(len(msg)):
        if msg[i]=="{" :
            return json.loads(msg[i:])
    return None


#websocket大框架。
class CG_Client(WebSocketClient):
  #建立连接后发生的信息
  def opened(self):
    req = '{"event":"subscribe", "channel":"eth_usdt.deep"}'
    self.send(req)
  #关闭连接后
  def closed(self, code, reason=None):
    print("Closed down:", code, reason)

  #收到信息后
  def received_message(self, resp):
    rev_json = recv_to_json(str(resp))
    if rev_json !=None:
        if ("post_type" in rev_json) and (not ("interval" in rev_json)):
            print(rev_json)
            decete(rev_json)
        else:
            print("ws脉搏")
    else:
        print("None")


if __name__ == '__main__':
  ws = None
  try:
    ws = CG_Client('ws://127.0.0.1:6700')
    ws.connect()
    ws.run_forever()
  except KeyboardInterrupt:
    ws.close()
