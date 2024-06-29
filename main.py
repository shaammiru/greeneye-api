from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from router import predict, detail, search
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(predict.router, prefix="/predict", tags=["predict"])
app.include_router(detail.router, prefix="/plants", tags=["plants"])
app.include_router(search.router, prefix="/search", tags=["search"])


@app.get("/favicon.ico")
async def favicon():
    return RedirectResponse("/static/favicon.png")
