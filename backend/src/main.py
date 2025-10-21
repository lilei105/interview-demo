"""
FastAPI main application entry point
"""
import sys
import uvicorn
from .config import settings, logger
from .api import create_app


def main():
    """Main entry point for the application"""

    try:
        # Create FastAPI application
        app = create_app()

        logger.info(f"Starting server at http://{settings.host}:{settings.port}")
        logger.info(f"Documentation available at http://{settings.host}:{settings.port}/docs")

        # Run uvicorn server
        uvicorn.run(
            app,
            host=settings.host,
            port=settings.port,
            reload=settings.reload,
            log_level=settings.log_level
        )

    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        if settings.debug:
            logger.exception("Detailed error information:")
        sys.exit(1)


# Create app instance for direct import
app = create_app()


if __name__ == "__main__":
    main()