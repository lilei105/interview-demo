"""
Backend logging configuration
"""
import logging
import sys
from rich.logging import RichHandler
from .settings import settings


def setup_logging():
    """Setup logging configuration"""

    # Configure logging level
    log_level = settings.log_level.upper()

    # Create logger
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

    # Configure uvicorn access log
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)

    return logging.getLogger(__name__)


# Setup logging on import
logger = setup_logging()