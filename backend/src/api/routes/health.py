"""
Health check endpoint
"""
from fastapi import APIRouter, HTTPException
from datetime import datetime
import time
from typing import Dict, Any

from ...config import settings

router = APIRouter(tags=["monitoring"])

# Track application startup time
start_time = time.time()


@router.get("/health")
async def get_health() -> Dict[str, Any]:
    """
    Health check endpoint

    Returns service health status and dependency information
    """
    try:
        current_time = time.time()
        uptime = int(current_time - start_time)

        # Check dependencies
        dependencies = [
            {
                "name": "configuration",
                "status": "healthy" if settings else "unhealthy"
            },
            {
                "name": "logging",
                "status": "healthy"  # TODO: Add actual logging health check
            }
        ]

        # Determine overall status
        overall_status = "healthy"
        for dep in dependencies:
            if dep["status"] != "healthy":
                overall_status = "degraded"
                break

        return {
            "status": overall_status,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": "1.0.0",
            "uptime": uptime,
            "dependencies": dependencies
        }

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "health_check_failed",
                "message": "Health check encountered an error",
                "detail": str(e),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )