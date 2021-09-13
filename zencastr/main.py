from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from database import db
from model import Podcast
from bson import ObjectId


app = FastAPI()


@app.get('/')
async def say_ok():
    return PlainTextResponse(content='OK')


@app.get('/health')
async def say_ok():
    return PlainTextResponse(content='OK')


@app.get('/podcasts')
async def list_podcasts():
    podcasts = []
    for podcast in db.find():
        podcasts.append(Podcast(**podcast))
    return {'podcasts': podcasts}


@app.get('/podcast/{podcast_id}')
async def get_podcast(podcast_id: str, q: Optional[str] = None):
    result = db.find_one({'_id': ObjectId(podcast_id)})
    if result is None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return Podcast(**result)
    

@app.post('/podcast')
async def create_podcast(podcast: Podcast):
    if hasattr(podcast, 'id'):
        delattr(podcast, 'id')
    ret = db.insert_one(podcast.dict(by_alias=True))
    podcast.id = ret.inserted_id
    return {'podcast': podcast}
