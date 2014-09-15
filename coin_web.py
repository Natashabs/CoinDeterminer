#!/usr/bin/env python

__author__ = 'natasha'

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from coin import CoinDeterminer
import os
import uuid


def home(request):
    return Response("""\
    <form action="/result" method="post" accept-charset="utf-8"
    enctype="multipart/form-data">
    <label for="txt">Text file</label>
    <input id="txt" name="txt" type="file" value="" />
    <input type="submit" value="submit" /></form>""")   

def execute(request):
    input_file = request.POST['txt'].file
 
    with input_file as f:
        read_data = f.readlines()
    f.close
    list=""
    for line in read_data:
        list = list + str(int(line)) + " -> " + str(CoinDeterminer(int(line))) + "<br/>"
    return Response('The least number of coins for each input value is [value -> number of coins]: <br/> %s'%str(list))
    
if __name__ == '__main__':
    config = Configurator()
    
    config.add_route('home', '/')
    config.add_route('execute', '/result')

    config.add_view(home, route_name='home')
    config.add_view(execute, route_name='execute')
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()