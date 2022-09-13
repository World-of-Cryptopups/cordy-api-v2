from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from db import dpsDB, usersDB

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
            "data": {},
            "message": "Wallet does not exist in database.",
        }

    # get user
    user = userQuery.items[0]

    # fetch the user's dps
    dps = dpsDB.get(user["id"])

    return {"wallet": user["wallet"], "id": user["id"], "dps": dps["dps"]}
