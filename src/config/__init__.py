from pydantic import BaseSettings


class PathServer(BaseSettings):
    PATH_SERVER: str = '/rest/api'


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 7979


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "message-board"


class Settings(PathServer, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
