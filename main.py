from fastapi.responses import RedirectResponse  
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
from datetime import datetime

app = FastAPI(title="LinkSnap URL Shortener")

# Temporary storage (like a simple database)
url_database = {}

class URLInput(BaseModel):
    long_url: str

def generate_short_code(long_url: str) -> str:
    """Convert long URL to a 6-character unique code"""
    return hashlib.md5(long_url.encode()).hexdigest()[:6]

@app.post("/shorten")
def shorten_url(data: URLInput):
    # Generate short code
    short_code = generate_short_code(data.long_url)
    
    # Store in our temporary database
    url_database[short_code] = {
        "long_url": data.long_url,
        "created_at": datetime.now(),
        "clicks": 0
    }
    
    return {
        "short_code": short_code,
        "short_url": f"http://localhost:8000/{short_code}",
        "created_at": datetime.now()
    }

@app.get("/{short_code}")
def redirect_to_long(short_code: str):
    # Look up the short code
    if short_code not in url_database:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    # Increment click count
    url_database[short_code]["clicks"] += 1
    
    # ACTUALLY REDIRECT to the long URL
    return RedirectResponse(url=url_database[short_code]["long_url"])
    url_database[short_code]["clicks"] += 1
    
    # Return redirect response
    return {
        "message": "Redirecting...",
        "long_url": url_database[short_code]["long_url"],
        "clicks": url_database[short_code]["clicks"]
    }

@app.get("/stats/{short_code}")
def get_stats(short_code: str):
    if short_code not in url_database:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    data = url_database[short_code]
    return {
        "short_code": short_code,
        "long_url": data["long_url"],
        "created_at": data["created_at"],
        "total_clicks": data["clicks"]
    }

@app.get("/")
def root():
    return {"message": "Welcome to LinkSnap URL Shortener API", "docs": "/docs"}