from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
# mappings
from .mappings.router.board_mapping import router as BoardMapping

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event('startup')
async def start_db():
    app.mongo_db = AsyncIOMotorClient(settings.DB_URL)
    app.collection = app.mongo_db[settings.DB_NAME]


@app.on_event('shutdown')
async def shutdown_db():
    app.mongo_db.close()

app.include_router(BoardMapping, tags=["boards"], prefix=settings.PATH_SERVER)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello Python with mongodb!"}
