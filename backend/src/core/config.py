class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Website Generator"
    OLLAMA_URL: str = "http://ollama:11434"
    
    class Config:
        env_file = ".env"

settings = Settings()