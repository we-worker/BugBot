import requests
import json
import os
import time
from random import choice
group = json.load(open("./config.json", encoding='utf-8'))["group"]
ban_words = json.load(open("./config.json", encoding='utf-8'))["ban_words"]

help_base = "这里是帮助菜单：\n"
help_base += "1.发送setu 返回一张图\n"
help_base += "2.私聊调教对话 例如aaa+bbb \n"
help_base += "那么发送aaa就会返回bbb啦~\n"
help_base += "可以发送rmaaa+bbb删除对话哦~\n"
help_base+="3.发送今日运势，运气 可以测运势\n"


def help_menu(msg):
	if msg[:4] != "help":
		return [False]
	if msg == "help":
		return [True, help_base]


def add_data(msg, all_data):
	if msg.count("+") != 1:
		return [False]
	if "/" in msg or "|" in msg:
		return [True, "不能含有/或|呀~"]
	if msg.split("+")[1] == "":
		return [False]
	msg = msg.split("+")
	if len(msg[0]) < 2:
		return [True, "长度要大于1呀~"]
	for row in all_data:
		if msg[0] == row[0]:
			if msg[1] in row[1]:
				return [True, "这句话我已经会辣，不用再教我啦~"]
			row[1].append(msg[1])
			save_words(all_data)
			return [True, "添加成功！"]
	all_data.append([msg[0], [msg[1]]])
	save_words(all_data)
	return [True, "添加成功！"]


def save_words(all_data):
	f = open("./data/talk_data/words", "w", encoding='UTF-8')
	for row in all_data:
		temp = row[0]+"|"+"".join([i+"/" for i in row[1]])
		f.writelines(temp+"\n")
	f.close()


def del_data(del_data, all_data):
	if del_data[:2] != "rm":
		return [False]
	msg = del_data[2:].split("+")
	for i in range(len(all_data)):
		if msg[0] == all_data[i][0]:
			#if len(all_data[i][1]) == 1:
			#	all_data.pop(i)
			#	save_words(all_data)
			#	return [True, "已经删除啦~"]
			all_data.pop(i)
			save_words(all_data)
			return [True, "已经删除啦~"]
	return [True, "已经删除啦~"]


def ghs_pic(msg):
	if msg in ["setu"]:
		try:
			req_url = "https://api.lolicon.app/setu/v2"
			params = {}
			res = requests.get(req_url, params=params)
			setu_title=res.json()['data'][0]['title']
			setu_url=res.json()['data'][0]['urls']['original']
			setu_pid=res.json()['data'][0]['pid']
			setu_author=res.json()['data'][0]['author']
			local_img_url = "title:"+setu_title+"[CQ:image,file="+setu_url+"]"+"pid:"+str(setu_pid)+" 画师:"+setu_author
			return [True, local_img_url]
		except Exception as e:
			print(e)
			return [True, "阿这，出了一点问题"]
	return [False]

def hs_pic(msg):
	if msg in ["huangse"]:
		try:
			req_url="https://api.lolicon.app/setu/v2"
			params = {"apikey":apikey,"r18":"1"}
			res=requests.get(req_url,params=params)
			setu_title=res.json()['data'][0]['title']
			setu_url=res.json()['data'][0]['urls']['original']
			setu_pid=res.json()['data'][0]['pid']
			setu_author=res.json()['data'][0]['author']


			local_img_url = "title:"+setu_title+"[CQ:image,file="+setu_url+"]"+"pid:"+str(setu_pid)+" 画师:"+setu_author
			return [True, local_img_url]
		except Exception as e:
			print(e)
			return [True, "阿这，出了一点问题"]
	return [False]

def mao_pic(msg):
	if msg in ["来张猫猫图", "来张猫图", "猫图", "喵图", "maomao","猫猫图","猫"]:
		setu_list = os.listdir(path)
		local_img_url = "[CQ:image,file=file://"+path+choice(setu_list)+"]"
		return [True, local_img_url]
	return [False]

def detect_ban(msg,user_id,group_id):
	if group_id not in group:
		return [False]
	if msg in ban_words:
		data = {
			'user_id':user_id,
			'group_id':group_id,
			'duration':60
		}
		cq_url = "http://127.0.0.1:5700/set_group_ban"
		requests.post(cq_url,data=data)
		return [True,"不要说不该说的话啦~"]
	return [False]
def save_lucky(lucky,user_id):
	f = open("./data/lucky/lucky","a+",encoding='UTF-8')
	temp = str(user_id)+"|"+lucky+"|"+str(time.time())
	f.writelines(temp+"\n")
	f.close()

def read_Lucky():
	data = []
	for line in enumerate(open("./data/lucky/lucky", 'r', encoding='UTF-8')):
		line=str(line)
		line=line.strip().split("'")[1]
		temp = line.strip().split("|")
		temp = [temp[0],temp[1],temp[2]]
		data.append(temp)
	return data


def getLucky(msg,user_id):
	if msg in ["今日运势", "运气", "运势", "算命"]:
		try:
			already=read_Lucky()
			for i in range(len(already)):
				if user_id == int(already[i][0]) and time.time()-float(already[i][2][:-2])<60*60*24:
					re="您今天已经测过了，是【{}】，要记住哦！".format(already[i][1][:-2])
					return [True,re]
		except:
			print("没测过")
		jsonPath = './send_message/Lucky/copywriting.json'
		with open(jsonPath,'r',encoding='UTF-8') as f: copywriting=json.load(f)
		luck=choice(copywriting['copywriting'])

		jsonPath = './send_message/Lucky/goodLuck.json'
		with open(jsonPath,'r',encoding='UTF-8') as f: goodLuck=json.load(f)

		for i in goodLuck['types_of']:
			if i['good-luck'] == luck['good-luck']:
				luck['good-luck']=i['name']
		re="您今日的运势是:{}。   给您的寄语是:{}.".format(luck['good-luck'],luck['content'])
		save_lucky(re,user_id)
		return [True,re]
	return [False]

