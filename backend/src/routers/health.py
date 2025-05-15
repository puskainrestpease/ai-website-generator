from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import requests
import logging

from ..db.database import get_db
from ..core.config import settings

router = APIRouter(tags=["health"])
logger = logging.getLogger("api.health")

def check_database(db: Session):
    try:
        db.execute("SELECT 1")
        return {"database": "ok"}
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return {"database": "unavailable"}

def check_ollama():
    try:
        response = requests.get(
            f"{settings.OLLAMA_URL}/version",
            timeout=3
        )
        return {"ollama": "ok" if response.ok else "unhealthy"}
    except Exception as e:
        logger.error(f"Ollama health check failed: {str(e)}")
        return {"ollama": "unavailable"}

@router.get("/health", summary="Basic health check")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "service": settings.PROJECT_NAME
    }

@router.get("/health/detailed", summary="Detailed system health check")
async def detailed_health_check(db: Session = Depends(get_db)):
    checks = {
        **check_database(db),
        **check_ollama(),
        "api": "ok"
    }
    
    status = "ok" if all(v == "ok" for v in checks.values()) else "degraded"
    
    return {
        "status": status,
        "timestamp": datetime.utcnow().isoformat(),
        "details": checks
    }

@router.get("/health/ready", summary="Readiness check")
async def readiness_check():
    return {"status": "ready"}

@router.get("/health/startup", summary="Startup check")
async def startup_check():
    return {"status": "started"}