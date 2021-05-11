import uvicorn
from src.config import settings

print(settings)

if __name__ == "__main__":
    uvicorn.run("src.app:app", host=settings.HOST,
                port=settings.PORT, reload=True, log_level="info",)
