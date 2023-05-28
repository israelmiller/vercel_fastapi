from time import time
from fastapi import FastAPI, __version__

app = FastAPI() # This is what will be refrenced in config

@app.get('/')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}

@app.get('/ping')
async def ping():
    return {'res': 'pong', 'version': __version__, "time": time()}