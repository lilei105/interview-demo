# Frontend Application

Vue3前端应用，提供现代化的用户界面和热重载开发环境。

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 配置环境变量

```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑配置文件（可选）
# 修改端口、API地址等配置
```

### 3. 启动开发服务器

```bash
# 启动Vite开发服务器
npm run dev

# 或使用yarn
yarn dev
```

### 4. 访问应用

- **前端应用**: http://127.0.0.1:3000
- **API代理**: http://127.0.0.1:3000/api/* (自动代理到后端)

## 可用脚本

```bash
# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 运行测试
npm test

# 运行测试UI
npm run test:ui
```

## 项目结构

```
frontend/
├── src/
│   ├── main.js              # 应用入口
│   ├── App.vue              # 根组件
│   ├── config/              # 配置管理
│   │   └── index.js         # 前端配置
│   ├── router/              # 路由配置
│   │   └── index.js         # Vue Router设置
│   ├── components/          # Vue组件
│   │   ├── HelloWorld.vue   # 示例组件
│   │   └── Error404.vue     # 404错误页面
│   ├── views/               # 页面视图
│   │   └── Home.vue         # 首页
│   └── tests/               # 测试文件
├── public/                  # 静态资源
├── index.html              # HTML模板
├── package.json            # 依赖配置
├── vite.config.js          # Vite配置
└── README.md               # 说明文档
```

## 配置说明

主要配置项（通过环境变量设置）：

- `FRONTEND_HOST`: 开发服务器主机 (默认: 127.0.0.1)
- `FRONTEND_PORT`: 开发服务器端口 (默认: 3000)
- `FRONTEND_HOT`: 热模块替换开关 (默认: true)
- `VITE_API_BASE_URL`: 后端API地址 (默认: http://127.0.0.1:8000)
- `VITE_APP_ENV`: 应用环境 (默认: development)

## 开发功能

### 热重载
- 代码修改自动刷新页面
- 组件状态保持
- 快速反馈循环

### API代理
- 前端自动代理API请求到后端
- 避免CORS问题
- 开发环境友好

### 错误处理
- 全局错误捕获
- 开发模式详细错误信息
- 用户友好的错误页面

### 路由系统
- Vue Router 4
- 动态路由加载
- 404错误处理
- 路由守卫

## 开发说明

### 添加新页面

1. 在 `src/views/` 目录下创建新的Vue组件
2. 在 `src/router/index.js` 中添加路由配置
3. 通过 `router-link` 导航到新页面

### 添加新组件

1. 在 `src/components/` 目录下创建Vue组件
2. 在页面组件中导入和使用
3. 遵循Vue3 Composition API最佳实践

### API集成

```javascript
import axios from 'axios'
import config from './config/index.js'

// GET请求
const response = await axios.get(`${config.apiBaseUrl}/api/data`)

// POST请求
const result = await axios.post(`${config.apiBaseUrl}/api/create`, data)
```

### 样式管理

- 使用CSS Scoped避免样式冲突
- 响应式设计支持
- CSS变量定义主题颜色

## 测试

```bash
# 运行所有测试
npm test

# 运行测试并生成覆盖率报告
npm test -- --coverage

# 运行特定测试文件
npm test -- HelloWorld.test.js
```

## 构建部署

```bash
# 构建生产版本
npm run build

# 预览构建结果
npm run preview
```

构建文件将生成在 `dist/` 目录中，可以部署到任何静态文件服务器。

## 技术栈

- **Vue 3**: 渐进式JavaScript框架
- **Vue Router 4**: 官方路由管理器
- **Vite**: 现代化构建工具
- **Axios**: HTTP客户端
- **Vitest**: 单元测试框架