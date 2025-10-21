# Quick Start Guide: 基础项目框架搭建

**Purpose**: 快速搭建和运行前后端基础框架
**Date**: 2025-10-21
**Prerequisites**: Python 3.8+, Node.js 16+

## 环境准备

### 1. 克隆项目
```bash
git clone https://github.com/lilei105/interview-demo.git
cd interview-demo
```

### 2. 创建环境配置文件
```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑配置文件（可选）
# 修改端口、主机等配置
```

## 后端服务启动

### 1. 安装Python依赖
```bash
cd backend
pip install -r requirements.txt
```

### 2. 启动开发服务器
```bash
# 方式1：使用uvicorn直接启动
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload

# 方式2：使用Python模块启动
python -m src.main

# 方式3：使用启动脚本（如果存在）
python start.py
```

### 3. 验证后端服务
```bash
# 测试根路由
curl http://127.0.0.1:8000/

# 测试健康检查
curl http://127.0.0.1:8000/health

# 测试配置信息
curl http://127.0.0.1:8000/api/v1/config
```

**预期响应**:
```json
{
  "name": "基础项目框架API",
  "version": "1.0.0",
  "description": "FastAPI后端服务",
  "status": "running",
  "timestamp": "2025-10-21T10:00:00Z"
}
```

## 前端服务启动

### 1. 安装Node.js依赖
```bash
cd frontend
npm install
```

### 2. 启动开发服务器
```bash
# 启动Vite开发服务器
npm run dev

# 或使用yarn
yarn dev
```

### 3. 验证前端服务
- 打开浏览器访问: http://127.0.0.1:3000
- 应该看到Vue3欢迎页面
- 修改代码后页面应自动热重载

## 同时运行前后端

### 方式1：分别启动（推荐）
```bash
# 终端1：启动后端
cd backend
uvicorn src.main:app --reload

# 终端2：启动前端
cd frontend
npm run dev
```

### 方式2：使用进程管理工具
```bash
# 安装tmux或screen（可选）
# 创建两个会话分别运行前后端
```

## 端口配置

### 默认端口
- 后端API: 8000
- 前端开发服务器: 3000

### 修改端口
```bash
# 后端端口
export BACKEND_PORT=8001
uvicorn src.main:app --port 8001

# 前端端口
export FRONTEND_PORT=3001
npm run dev -- --port 3001
```

### 端口冲突处理
如果默认端口被占用：
1. 系统自动选择下一个可用端口
2. 控制台会显示实际使用的端口
3. 更新前端API配置指向新端口

## 环境配置

### 开发环境变量
```bash
# 后端配置
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000
BACKEND_RELOAD=true
BACKEND_LOG_LEVEL=info

# 前端配置
FRONTEND_HOST=127.0.0.1
FRONTEND_PORT=3000
FRONTEND_HOT=true
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 配置文件位置
- 全局配置: `/.env`
- 后端配置: `/backend/.env`
- 前端配置: `/frontend/.env`

## 测试验证

### 后端测试
```bash
cd backend
pytest

# 运行特定测试
pytest tests/test_main.py
pytest tests/test_routes/
```

### 前端测试
```bash
cd frontend
npm test

# 运行特定测试文件
npm test -- --run HelloWorld.test.js
```

## 常见问题

### Q: 后端启动失败
**A**: 检查端口是否被占用，查看错误日志，确认Python依赖已安装

### Q: 前端热重载不工作
**A**: 检查文件路径，确认Vite配置正确，查看浏览器控制台错误

### Q: API调用失败
**A**: 确认前后端端口配置匹配，检查CORS设置，查看网络请求详情

### Q: 环境变量不生效
**A**: 确认.env文件存在且格式正确，重启服务使配置生效

## 开发工作流

### 1. 日常开发
```bash
# 启动后端
cd backend && uvicorn src.main:app --reload

# 启动前端
cd frontend && npm run dev

# 开始编码...
```

### 2. 添加新功能
```bash
# 后端：添加新路由
cd backend/src/api/routes/
# 创建新路由文件

# 前端：添加新组件
cd frontend/src/components/
# 创建新Vue组件
```

### 3. 提交代码
```bash
# 运行测试
cd backend && pytest
cd frontend && npm test

# 提交代码
git add .
git commit -m "feat: 添加新功能"
```

## 性能优化

### 开发环境优化
- 使用 `--reload-dir` 限制监视目录
- 配置适当的日志级别避免过多输出
- 使用浏览器开发者工具分析性能

### 构建优化（生产环境）
```bash
# 前端构建
npm run build

# 后端优化
# 使用生产ASGI服务器
```

## 下一步

基础框架搭建完成后，您可以：
1. 实现具体的业务逻辑
2. 添加数据库集成
3. 集成外部API
4. 添加用户认证
5. 部署到生产环境

参考完整文档：
- [功能规格](spec.md)
- [数据模型](data-model.md)
- [API文档](contracts/openapi.yaml)