from fastapi import APIRouter, FastAPI,Query, Response
import routes
import uvicorn
import utils
app = FastAPI()
app.include_router(routes.router)


uvicorn.run(
    app,
    port=80
)