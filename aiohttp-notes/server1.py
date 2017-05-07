#!/usr/bin/python3

from aiohttp import web
import asyncio

'''
http://aiohttp.readthedocs.io/en/stable/
'''

svc = []

@asyncio.coroutine
def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
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