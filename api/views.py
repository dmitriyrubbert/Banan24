# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
import json
from api.models import User, Female, Message
# Create your views here.

def autoupdaters(request, *args, **kwargs):
	return render(request, "AutoUpdaterCharmDate.xml", {})

def login(request, *args, **kwargs):
	if request.method == 'POST':
		# backend post
		# {"Email":"krasnayasobaka6663@gmail.com","Password":"4691857331Adm","isApp":true}
		json_data = json.loads(request.body)
		try:
			email = json_data['Email']
			password = json_data['Password']
		except KeyError:
			return HttpResponseServerError("Malformed data!")
		qs = User.objects.filter(email__iexact=email)
		if qs.count() != 1 and not qs.exists():
			return HttpResponse("User not found! Bye")
			# raise Http404
		obj = qs.first()
		# print(obj.password)
		data_from_api = """
		{
			"tokenString":"created_by_goldlinux",
			"user":{
					"id":817,
					"email":"{}",
					"role":"{}",
					"lastActive":"",
					"isActive":{},
					"agencyId":{},
					"agency":null
					}
		}
		""".format( obj.email, 
					obj.role, 
					# obj.last_active.strftime('%Y-%m-%dT%H:%M:%S'), 
					obj.is_active, 
					obj.agency_id )
		print('data_from_api', data_from_api)
		j = json.loads(data_from_api)
		response = JsonResponse(j)
		print('response', response)
		response["Access-Control-Allow-Credentials"] = "true"
		response["Access-Control-Allow-Origin"] = "https://banan24.com"
		response["Vary"] = "Origin"
		return response
		# server responce 
		# {"tokenString":"eyJhbGciOiJIUzUx....","user":{"id":817,"email":"krasnayasobaka6663@gmail.com","role":"Translator","lastActive":"2018-10-18T12:44:45","isActive":true,"agencyId":99,"agency":null}}

