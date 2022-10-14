from typing import Dict, List
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from db import dpsDB, usersDB
from filter import filter_rankings
from utils import identify_dps_role

app = FastAPI()

# add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Cordy API v2"


@app.get("/dps")
def dps(res: Response):
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": True, "message": "Wallet is not defined."}


@app.get("/dps/{wallet}")
async def get_dps(wallet: str, res: Response):
    userQuery = usersDB.fetch(query={"wallet": wallet}, limit=1)
    if len(userQuery.items) == 0:
        return {
            "error": True,
            "data": None,
            "message": "Wallet does not exist in database.",
        }

    # get user
    user = userQuery.items[0]

    # fetch the user's dps
    dps = dpsDB.get(user["id"])

    dps_role = identify_dps_role(dps["dps"])

    return {
        "error": False,
        "data": {
            "wallet": user["wallet"],
            "id": user["id"],
            "dps": dps["dps"],
            "role": dps_role,
        },
        "message": None,
    }


@app.get("/leaderboard")
async def leaderboard():
    try:
        q = dpsDB.fetch()
        allitems: List[Dict] = q.items

        while q.last:
            q = dpsDB.fetch(last=q.last)
            allitems += q.items

    except Exception as e:
        return {"error": True, "data": None, "message": e}

    rankings = filter_rankings(allitems)

    return {"error": False, "data": rankings, "message": ""}
