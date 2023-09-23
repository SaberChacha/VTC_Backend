from fastapi import FastAPI
import redis
app = FastAPI()


@app.get("/get_channel")
async def get_location_channel(latitude : float, longitude : float):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    rounded_latitude = round(latitude,2)
    rounded_longitude = round(longitude,2)
    channel = r.get(f'{rounded_latitude},{rounded_longitude}')
    return {"channel": channel}

