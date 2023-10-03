# Import necessary FastAPI modules and classes
from fastapi import FastAPI, Depends
from app.cache import cache  # Import the cache object from app.cache module
from app.PostClasses import UserSession  # Import UserSession from app.PostClasses module
from app.authorize import authorize  # Import the authorize function from app.authorize module

# Create an instance of the FastAPI app
app = FastAPI()

active_users = []

@app.post("/active_users")
async def get_active_users(session: UserSession = Depends(lambda: authorize("admin", sessionid, roles))):
    if session:
        keys = cache.keys()
        users = []

        for key in keys:
            key_str = key.decode('utf-8')
            if "-sessionid" in key_str:
                users.append(key_str.replace("-sessionid", "") + "-sessionid")
        return {"active-users": users}
    return {"msg": "Not authorized"}
