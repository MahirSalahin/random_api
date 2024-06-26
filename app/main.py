from fastapi import FastAPI, Response
from routers.random import router as randoom_router

app = FastAPI()
app.include_router(randoom_router)

@app.get("/")
def get_home() -> Response:
    """
    Return server status
    """
    return Response("Server is running")
