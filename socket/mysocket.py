#!/usr/bin/env python3

# websockets
# https://websockets.readthedocs.io/en/stable/
# https://aiohttp.readthedocs.io/en/stable/web_quickstart.html#aiohttp-web-websockets

# Deploying nginx + django + python 3
# https://tutos.readthedocs.io/en/latest/source/ndg.html

# import asyncio
# import websockets
import aiohttp
from aiohttp import web
import json

async def hello(request):
	return web.Response(text="Hello, world")

	
async def websocket_handler(request):

	ws = web.WebSocketResponse()
	print('ws.init()')
	i = 0
	await ws.prepare(request)
	async for msg in ws:
		print('FROM CLIENT:',msg.data)
		
		if msg.type == aiohttp.WSMsgType.TEXT:
			if msg.data == 'close':
				await ws.close()
				print('ws.close()')
			# else:
			# 	await ws.send_str(msg.data + '/answer')
			j=json.loads(msg.data)
			cmd = j['cmd']
			# print(cmd)
			if cmd == 1:
				string = '{"cmd":1,"req":%s,"data":true}' % i
				await ws.send_str(string)
				print('FROM SERVER:', string)
				i += 1

			if cmd == 101:
				# {"cmd":101,"req":2,"data":"[{\"siteId\":\"C846349\",\"siteLogin\":null,\"sitePassword\":\"w704l215\",\"endActivation\":\"2018-11-11T20:13:33\",\"endMailActivation\":\"0001-01-01T00:00:00\"},{\"siteId\":\"C705185\",\"siteLogin\":null,\"sitePassword\":\"w7pyiira\",\"endActivation\":\"2018-11-11T20:13:33\",\"endMailActivation\":\"0001-01-01T00:00:00\"},{\"siteId\":\"C178782\",\"siteLogin\":null,\"sitePassword\":\"123123123\",\"endActivation\":\"2018-11-11T20:13:33\",\"endMailActivation\":\"0001-01-01T00:00:00\"}]"}
				# string = """{"cmd":101,"req":2,"data":"[{\\"siteId\\":\\"C846349\\",\\"siteLogin\\":null,\\"sitePassword\\":\\"w704l215\\",\\"endActivation\\":\\"2028-11-11T20:13:33\\",\\"endMailActivation\\":\\"0001-01-01T00:00:00\\"}]"}"""
				string = """{"cmd":101,"req":2,"data":"[{\\"siteId\\":\\"C705185\\",\\"siteLogin\\":null,\\"sitePassword\\":\\"w7pyiira\\",\\"endActivation\\":\\"2028-11-11T20:13:33\\",\\"endMailActivation\\":\\"0001-01-01T00:00:00\\"}]"}"""
				# string = '{"cmd":101,"req":%s,"data":[]}' % i
				await ws.send_str(string)
				print('FROM SERVER:', string)
				i += 1

			if cmd == 108:
				# {"cmd":108,"req":3,"data":{"WomanId":"C846349","LastUpdate":1539826404391}}
				# {"cmd":108,"req":3,"data":{"WomanId":"C705185","LastUpdate":1539826403250}}
				string = '{"cmd":108,"req":%s,"data":[]}' % i
				await ws.send_str(string)
				print('FROM SERVER:', string)
				i += 1

			# FROM CLIENT: {"cmd":111,"req":1,"data":"3.1.4.8"} socket version
			# FROM CLIENT: {"cmd":107,"req":4,"data":{"WomanId":"C705185","Messages":[{"Id":5,"Guid":"420ba569-d9d1-4fab-be5c-6d1fc23c7922","WomanId":"C705185","Message":"What is your barrel caliber?","Type":2,"WithPrefix":true,"AgeFrom":30,"AgeTo":99,"Country":null,"CountryKey":null,"Purpose":1,"LastUpdate":1542482696893,"IsDeleted":false,"IsBlocked":false,"MessageId":35139},{"Id":6,"Guid":"26cbca9f-0356-4a97-ace3-46b99055c301","WomanId":"C705185","Message":"You want to climb a mountain? [img:15]","Type":2,"WithPrefix":true,"AgeFrom":30,"AgeTo":99,"Country":null,"CountryKey":null,"Purpose":1,"LastUpdate":1542482696971,"IsDeleted":false,"IsBlocked":false,"MessageId":35140},{"Id":7,"Guid":"83842f50-5729-4830-9317-7427cf7d9b2a","WomanId":"C705185","Message":"I attended strip-dancing courses once in a while","Type":2,"WithPrefix":true,"AgeFrom":30,"AgeTo":99,"Country":null,"CountryKey":null,"Purpose":1,"LastUpdate":1542482697034,"IsDeleted":false,"IsBlocked":false,"MessageId":35141},{"Id":8,"Guid":"5ba2879e-0a15-47ff-9e09-dedec357eca5","WomanId":"C705185","Message":"W68","Type":3,"WithPrefix":false,"AgeFrom":30,"AgeTo":99,"Country":"United States","CountryKey":"US","Purpose":1,"LastUpdate":1542482697112,"IsDeleted":false,"IsBlocked":false,"MessageId":null}]}}
			
			# FROM CLIENT: {"cmd":102,"req":6,"data":{"WomanId":"C705185","ManId":"CM66184761","Message":null,"MessageId":35139,"Prefix":null}}
			# FROM CLIENT: {"cmd":102,"req":7,"data":{"WomanId":"C705185","ManId":"CM20465968","Message":null,"MessageId":35139,"Prefix":null}}
			# FROM CLIENT: {"cmd":102,"req":8,"data":{"WomanId":"C705185","ManId":"CM96873264","Message":"W68","MessageId":null,"Prefix":"False"}}
			# FROM CLIENT: {"cmd":102,"req":9,"data":{"WomanId":"C705185","ManId":"CM744699","Message":null,"MessageId":35141,"Prefix":null}}
			# FROM CLIENT: {"cmd":102,"req":10,"data":{"WomanId":"C705185","ManId":"CM49716738","Message":null,"MessageId":35141,"Prefix":null}}
			# FROM CLIENT: {"cmd":102,"req":11,"data":{"WomanId":"C705185","ManId":"CM47274779","Message":null,"MessageId":35140,"Prefix":null}}

		elif msg.type == aiohttp.WSMsgType.PING:
			print('WSMsgType.PING received from client')
			# string = '{"cmd":0,"req":%s,"data":""}' % i
			# await ws.send_str(string)
			# print('FROM SERVER:', string)
			# i += 1

		elif msg.type == aiohttp.WSMsgType.ERROR:
			print('ws connection closed with exception %s' %
				  ws.exception())

	print('websocket connection closed')

	return ws


app = web.Application()
app.add_routes([web.get('/', hello)])
app.add_routes([web.get('/charmdatehub', websocket_handler)])

web.run_app(app, host='0.0.0.0', port=8082)