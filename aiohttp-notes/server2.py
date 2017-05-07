#!/usr/bin/python3

from aiohttp import web
import asyncio
import datetime
import time

starttime = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.today())

'''
http://aiohttp.readthedocs.io/en/stable/t

'''
svc = []


@asyncio.coroutine
def handle(request):
    name = request.match_info.get('name', "Anonymous")
    currtime = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.today())
    text = starttime + "\n" + currtime + "\n" + "Hello, " + name
    return web.Response(text=text)



@asyncio.coroutine
def add_val(request):
    val = request.match_info.get('name','empty')
    svc.append(val)
    return web.Response(text='OK' + str(svc))



@asyncio.coroutine
def view(request):
    return web.json_response(svc)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/add/{name}', add_val)
app.router.add_get('/view', view)
app.router.add_get('/{name}', handle)



web.run_app(app)