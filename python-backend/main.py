from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Code that runs every request before it reaches my endpoint
# Allows all frontend apps to talk to this backend
app.add_middleware(
    CORSMiddleware,
    # Later restricted when an actual site is deployed
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Runs on http://localhost:8000


data = ["apple", "banana", "grape", "orange", "pineapple"]

@app.get("/search")
def search(q: str = ""):
    results = [item for item in data if q.lower() in item.lower()]
    return results