# Data Model: 基础项目框架搭建

**Purpose**: Define entities and configurations for the project framework setup
**Date**: 2025-10-21
**Feature**: [基础项目框架搭建](spec.md)

## Entities

### Backend Service Configuration
**Purpose**: Configuration settings for FastAPI backend service

**Fields**:
- `host` (string): Server host address, default: "127.0.0.1"
- `port` (integer): Server port, default: 8000
- `reload` (boolean): Enable hot reload, default: true
- `log_level` (string): Logging level, default: "info"
- `cors_origins` (list[string]): CORS allowed origins, default: ["http://localhost:3000"]

**Validation Rules**:
- Port must be between 1024-65535
- Host must be valid IP address or hostname
- Log level must be one of: debug, info, warning, error, critical

### Frontend Service Configuration
**Purpose**: Configuration settings for Vue3 frontend service

**Fields**:
- `host` (string): Development server host, default: "127.0.0.1"
- `port` (integer): Development server port, default: 3000
- `hot` (boolean): Enable HMR, default: true
- `open` (boolean): Auto-open browser, default: false
- `proxy` (object): API proxy configuration

**Validation Rules**:
- Port must be between 1024-65535
- Proxy target must be valid URL

### Environment Configuration
**Purpose**: Environment variables and settings

**Fields**:
- `environment` (string): Current environment, default: "development"
- `debug` (boolean): Debug mode, default: true
- `secret_key` (string): Application secret key
- `api_base_url` (string): Backend API base URL
- `frontend_url` (string): Frontend application URL

**Validation Rules**:
- Environment must be one of: development, testing, staging, production
- Secret key must be at least 32 characters in production
- URLs must be valid format

### Health Status
**Purpose**: Service health check information

**Fields**:
- `status` (string): Service status, values: "healthy", "degraded", "unhealthy"
- `timestamp` (datetime): Check timestamp
- `version` (string): Application version
- `uptime` (integer): Service uptime in seconds
- `dependencies` (list[object]): Dependency status list

**Validation Rules**:
- Status must be one of predefined values
- Timestamp must be valid ISO format
- Uptime must be non-negative integer

## Configuration Files

### Backend Configuration (.env)
```
# Server Settings
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000
BACKEND_RELOAD=true
BACKEND_LOG_LEVEL=info

# CORS Settings
CORS_ORIGINS=["http://localhost:3000"]

# Security
SECRET_KEY=your-secret-key-here
DEBUG=true
```

### Frontend Configuration (.env)
```
# Development Server
FRONTEND_HOST=127.0.0.1
FRONTEND_PORT=3000
FRONTEND_HOT=true

# API Configuration
VITE_API_BASE_URL=http://127.0.0.1:8000
VITE_APP_ENV=development
```

### Global Configuration (.env.example)
```
# Application
ENVIRONMENT=development
DEBUG=true

# Backend
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000

# Frontend
FRONTEND_HOST=127.0.0.1
FRONTEND_PORT=3000

# Security
SECRET_KEY=change-this-secret-key-in-production
```

## State Management

### Service States
- **INITIALIZING**: Service starting up
- **RUNNING**: Service operational
- **RELOADING**: Hot reload in progress
- **ERROR**: Service encountered error
- **STOPPED**: Service stopped

### Configuration Loading Priority
1. Environment variables
2. .env file in project root
3. .env file in service directory
4. Default configuration values

## Validation Rules

### Port Validation
- Must be integer between 1024-65535
- Cannot be privileged ports (<1024)
- Must be available (not in use)

### Host Validation
- Must be valid IP address or hostname
- Localhost aliases allowed (127.0.0.1, localhost)
- No protocol prefix (http://, https://)

### URL Validation
- Must be valid URL format
- Must include protocol (http:// or https://)
- Must be accessible (for CORS origins)

## Error Handling

### Configuration Errors
- Missing required fields → Default values with warnings
- Invalid format → Clear error messages with examples
- Port conflicts → Automatic port selection with notification
- File not found → Graceful fallback to defaults

### Service Errors
- Startup failures → Detailed error logs
- Runtime errors → Health check status update
- Configuration changes → Hot reload with validation