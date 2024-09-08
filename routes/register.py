from fastapi import APIRouter, FastAPI, Response, Form, Query
import utils
router = APIRouter(
)

@router.get("/register")
def Register(username = Query(..., alias="username"), password = Query(..., alias="password")):
    val = utils.create_user(username,password)
    if val:
        return Response("ok",200)
    else:
        return Response("Username taken",200)