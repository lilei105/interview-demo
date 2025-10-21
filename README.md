# 基础项目框架

一个基于 **FastAPI + Vue3** 的前后端分离项目框架，专注于快速原型开发和高效的热重载开发环境。

## ✨ 特性

- 🚀 **快速开发**: 支持前后端热重载，秒级反馈
- 🎯 **简洁设计**: 遵循简洁优先原则，避免过度工程化
- 🔧 **易于配置**: 环境变量管理，配置简单明了
- 📱 **响应式设计**: 移动端友好的用户界面
- 🛡️ **错误处理**: 完善的错误处理和日志记录
- 📚 **完整文档**: 详细的API文档和开发指南

## 🏗️ 技术栈

### 后端
- **FastAPI**: 现代化的Python Web框架
- **Uvicorn**: ASGI服务器，支持热重载
- **Pydantic**: 数据验证和设置管理
- **Pytest**: 测试框架

### 前端
- **Vue 3**: 渐进式JavaScript框架
- **Vue Router 4**: 官方路由管理器
- **Vite**: 现代化构建工具
- **Axios**: HTTP客户端
- **Vitest**: 单元测试框架

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Node.js 16+
- npm 或 yarn

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/lilei105/interview-demo.git
   cd interview-demo
   ```

2. **设置环境变量**
   ```bash
   # 复制环境变量示例文件
   cp .env.example .env

   # 编辑配置文件（可选）
   # 修改端口、主机等配置
   ```

3. **启动后端服务**
   ```bash
   cd backend
   pip install -r requirements.txt
   python start.py
   ```

   后端服务将在 http://127.0.0.1:8000 启动

4. **启动前端服务**（新终端）
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

   前端服务将在 http://127.0.0.1:3000 启动

5. **访问应用**
   - 前端应用: http://127.0.0.1:3000
   - 后端API文档: http://127.0.0.1:8000/docs
   - 健康检查: http://127.0.0.1:8000/health

## 📁 项目结构

```
interview-demo/
├── backend/                 # FastAPI后端服务
│   ├── src/
│   │   ├── main.py         # 应用入口
│   │   ├── config/         # 配置管理
│   │   └── api/            # API路由
│   ├── requirements.txt    # Python依赖
│   └── README.md          # 后端说明
├── frontend/               # Vue3前端应用
│   ├── src/
│   │   ├── main.js        # 应用入口
│   │   ├── App.vue        # 根组件
│   │   ├── components/    # Vue组件
│   │   ├── views/         # 页面视图
│   │   └── router/        # 路由配置
│   ├── package.json       # Node.js依赖
│   └── README.md         # 前端说明
├── docs/                  # 项目文档
├── specs/                 # 功能规格文档
├── .env.example          # 环境变量示例
├── .gitignore            # Git忽略文件
└── README.md             # 项目说明
```

## ⚙️ 配置说明

### 环境变量

主要配置项：

```bash
# 应用配置
ENVIRONMENT=development
DEBUG=true

# 后端配置
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000
BACKEND_RELOAD=true
BACKEND_LOG_LEVEL=info

# 前端配置
FRONTEND_HOST=127.0.0.1
FRONTEND_PORT=3000
VITE_API_BASE_URL=http://127.0.0.1:8000

# 安全配置
SECRET_KEY=change-this-secret-key-in-production
```

### 配置优先级

1. 环境变量
2. `.env` 文件（项目根目录）
3. `.env` 文件（服务目录）
4. 默认配置值

## 🔧 开发指南

### 后端开发

1. **添加新路由**
   ```python
   # 在 backend/src/api/routes/ 创建新文件
   from fastapi import APIRouter

   router = APIRouter(tags=["new-feature"])

   @router.get("/new-endpoint")
   async def new_endpoint():
       return {"message": "Hello from new endpoint"}
   ```

2. **添加新配置**
   ```python
   # 在 backend/src/config/settings.py 中添加
   new_setting: str = Field(default="default_value")
   ```

3. **运行测试**
   ```bash
   cd backend
   pytest
   ```

### 前端开发

1. **添加新页面**
   ```javascript
   // 在 frontend/src/views/ 创建新组件
   // 在 frontend/src/router/index.js 中添加路由
   ```

2. **添加新组件**
   ```vue
   <!-- 在 frontend/src/components/ 创建新组件 -->
   <template>
     <div class="new-component">
       <h3>New Component</h3>
     </div>
   </template>
   ```

3. **运行测试**
   ```bash
   cd frontend
   npm test
   ```

## 📖 API文档

启动后端服务后，可以通过以下地址访问API文档：

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### 主要端点

- `GET /` - 根路由，返回服务信息
- `GET /health` - 健康检查
- `GET /api/v1/config` - 获取配置信息（开发模式）

## 🧪 测试

### 后端测试

```bash
cd backend

# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_main.py

# 生成覆盖率报告
pytest --cov=src tests/
```

### 前端测试

```bash
cd frontend

# 运行所有测试
npm test

# 运行测试UI
npm run test:ui

# 生成覆盖率报告
npm test -- --coverage
```

## 🚀 部署

### 开发环境

按照快速开始步骤启动服务即可。

### 生产环境

1. **后端部署**
   ```bash
   # 使用生产ASGI服务器
   pip install gunicorn
   gunicorn backend.src.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. **前端部署**
   ```bash
   cd frontend
   npm run build
   # 将 dist/ 目录部署到静态文件服务器
   ```

## 🤝 贡献指南

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🆘 常见问题

### Q: 后端启动失败，端口被占用
A: 修改 `.env` 文件中的 `BACKEND_PORT` 配置，或停止占用端口的进程。

### Q: 前端无法连接后端API
A: 检查 `VITE_API_BASE_URL` 配置是否正确，确保后端服务已启动。

### Q: 热重载不工作
A: 检查文件权限，确保开发服务器有文件监视权限。

### Q: 环境变量不生效
A: 重启服务使环境变量生效，确保 `.env` 文件格式正确。

## 📚 相关文档

- [功能规格文档](specs/001-project-framework-setup/spec.md)
- [实施计划](specs/001-project-framework-setup/plan.md)
- [数据模型](specs/001-project-framework-setup/data-model.md)
- [快速开始指南](specs/001-project-framework-setup/quickstart.md)
- [后端说明](backend/README.md)
- [前端说明](frontend/README.md)

---

**基础项目框架** - 让开发更简单，让创意更自由 ✨