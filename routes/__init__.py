from . import api, register
from fastapi import Request, APIRouter


router = APIRouter()
router.include_router(api.router)
router.include_router(register.router)