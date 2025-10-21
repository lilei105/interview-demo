"""
API module - FastAPI application and router configuration
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from ..config import settings, logger
from .routes import health, root


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    logger.info("Starting FastAPI application...")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Debug mode: {settings.debug}")
    logger.info(f"Host: {settings.host}:{settings.port}")
    yield
    logger.info("Shutting down FastAPI application...")


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""

    # Create FastAPI application
    app = FastAPI(
        title="基础项目框架API",
        description="FastAPI后端服务基础框架",
        version="1.0.0",
        lifespan=lifespan,
        debug=settings.debug,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health.router)
    app.include_router(root.router)

    logger.info("FastAPI application created successfully")
    return app