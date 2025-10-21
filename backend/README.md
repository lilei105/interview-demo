# Backend Service

FastAPI后端服务，提供RESTful API和热重载开发环境。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑配置文件（可选）
# 修改端口、主机等配置
```

### 3. 启动服务

```bash
# 方式1：使用启动脚本
python start.py

# 方式2：使用uvicorn直接启动
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload

# 方式3：使用Python模块启动
cd src && python -m main
```

### 4. 访问服务

- **API服务**: http://127.0.0.1:8000
- **API文档**: http://127.0.0.1:8000/docs
- **健康检查**: http://127.0.0.1:8000/health

## API端点

### 根路由
```
GET /
```
返回服务基本信息。

### 健康检查
```
GET /health
```
检查服务健康状态和依赖情况。

## 项目结构

```
backend/
├── src/
│   ├── main.py              # 应用入口
│   ├── config/              # 配置管理
│   │   ├── settings.py      # 环境配置
│   │   ├── logging.py       # 日志配置
│   │   └── validation.py    # 配置验证
│   ├── api/                 # API路由
│   │   ├── __init__.py      # 应用工厂
│   │   └── routes/          # 路由定义
│   │       ├── health.py    # 健康检查
│   │       └── root.py      # 根路由
│   └── tests/               # 测试文件
├── requirements.txt         # Python依赖
├── .env.example            # 环境变量示例
├── start.py                # 启动脚本
└── README.md               # 说明文档
```

## 配置说明

主要配置项（通过环境变量设置）：

- `BACKEND_HOST`: 服务器主机地址 (默认: 127.0.0.1)
- `BACKEND_PORT`: 服务器端口 (默认: 8000)
- `BACKEND_RELOAD`: 热重载开关 (默认: true)
- `BACKEND_LOG_LEVEL`: 日志级别 (默认: info)
- `CORS_ORIGINS`: CORS允许的源地址
- `SECRET_KEY`: 应用密钥
- `DEBUG`: 调试模式

## 开发说明

### 添加新路由

1. 在 `src/api/routes/` 目录下创建新的路由文件
2. 使用 `APIRouter` 定义路由
3. 在 `src/api/__init__.py` 中包含新路由

### 添加新配置

1. 在 `src/config/settings.py` 中添加新的配置字段
2. 在 `src/config/validation.py` 中添加验证逻辑
3. 在 `.env.example` 中添加示例配置

### 测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_main.py

# 运行测试并生成覆盖率报告
pytest --cov=src tests/
```