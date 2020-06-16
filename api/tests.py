# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

var params = JSON.stringify({"Email":"admin@1cps.ru","Password":"4691857331Adm","isApp":true});
var http = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/api/auth/admin/login";
http.open("POST", url, true);
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
        console.log( http.responseText );
    }
};
http.send(params);