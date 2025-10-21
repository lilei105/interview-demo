"""
Root route endpoint
"""
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(tags=["basic"])


@router.get("/")
async def get_root():
    """
    Root endpoint - return basic service information
    """
    return {
        "name": "基础项目框架API",
        "version": "1.0.0",
        "description": "FastAPI后端服务",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }