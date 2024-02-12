from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from config.database import collection_name
from models.models import UrlMappingModel
from schema.schema import UrlMappingSchema
from utils.utils import create_short_url, DNS as dns
import sys

router = APIRouter()

db = UrlMappingModel(collection_name)

@router.get("/")
async def ping():
    return {"ping": "pong"}

@router.post("/longurl")
# async def shorten_url(request: Request, data: UrlMappingSchema):  
# async def shorten_url(request: Request):  
    # data = await request.json()
    # long_url = data.get("long_url")
async def shorten_url(url_mapping: UrlMappingSchema):  
    long_url = url_mapping.long_url
    print("long_url", long_url)
    # long_url = data.long_url  # Access the long_url attribute of the UrlMappingSchema object
    short_url = db.get_short_url(long_url)
    if not short_url: 
        short_url = create_short_url()
        # if the short URL already in DB, keep creating new ones
        while db.get_long_url(short_url):
            short_url = create_short_url()
        print("new short= ", short_url)
        db.insert_url_mapping(short_url, long_url)
    print("dns", dns)
    short_url = f"http://{dns}/{short_url}"
    return {"shortenedUrl": short_url}

    
@router.get("/{short_url}")
async def redirect_to_long_url(short_url: str):
    long_url = db.get_long_url(short_url)
    print("for short_url", short_url, "Redirect to long url", long_url)
    if long_url:
        return RedirectResponse(url=long_url, status_code=307)
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")