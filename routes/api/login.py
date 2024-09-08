from fastapi import APIRouter, FastAPI, Response, Form, Query
import utils
app = APIRouter(
)

@app.post("/api/login.php")
async def Login(username: str = Form(...,), password: str = Form(...)):
    print(f"Login attempt by {username} ({password})")
    return Response(utils.get_user(username,password))