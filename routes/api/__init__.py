from fastapi import FastAPI, APIRouter
from . import login, submit

router = APIRouter()
router.include_router(login.app)
router.include_router(submit.app)