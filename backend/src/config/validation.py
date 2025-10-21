"""
Configuration validation utilities
"""
import re
from typing import List, Optional
from ipaddress import ip_address, AddressValueError
from urllib.parse import urlparse


def validate_host(host: str) -> bool:
    """Validate host address (IP or hostname)"""
    try:
        # Try to validate as IP address
        ip_address(host)
        return True
    except AddressValueError:
        # Validate as hostname
        hostname_regex = r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$'
        return bool(re.match(hostname_regex, host))


def validate_port(port: int) -> bool:
    """Validate port number"""
    return 1024 <= port <= 65535


def validate_log_level(level: str) -> bool:
    """Validate log level"""
    valid_levels = ["debug", "info", "warning", "error", "critical"]
    return level.lower() in valid_levels


def validate_cors_origins(origins: List[str]) -> List[str]:
    """Validate and normalize CORS origins"""
    validated_origins = []

    for origin in origins:
        if isinstance(origin, str):
            # Remove trailing slash if present
            origin = origin.rstrip('/')

            # Basic URL validation
            if origin.startswith(('http://', 'https://')):
                validated_origins.append(origin)
            elif origin in ['localhost', '127.0.0.1']:
                # Add http protocol for localhost
                validated_origins.append(f'http://{origin}')
            else:
                raise ValueError(f"Invalid CORS origin: {origin}")
        else:
            raise ValueError(f"CORS origin must be string, got {type(origin)}")

    return validated_origins


def validate_secret_key(key: str) -> bool:
    """Validate secret key"""
    return len(key) >= 8  # Basic length validation


def validate_environment(env: str) -> bool:
    """Validate environment name"""
    valid_envs = ["development", "testing", "staging", "production"]
    return env.lower() in valid_envs


def validate_url(url: str) -> bool:
    """Validate URL format"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False