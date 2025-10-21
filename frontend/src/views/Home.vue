<template>
  <div class="home">
    <div class="hero">
      <h1>欢迎使用基础项目框架</h1>
      <p class="subtitle">Vue3 + FastAPI 前后端分离架构</p>
    </div>

    <div class="features">
      <div class="feature-card">
        <h3>🚀 快速开发</h3>
        <p>热重载支持，开发效率提升</p>
      </div>

      <div class="feature-card">
        <h3>🎯 简洁设计</h3>
        <p>遵循简洁优先原则，避免过度工程化</p>
      </div>

      <div class="feature-card">
        <h3>🔧 易于配置</h3>
        <p>环境变量管理，配置简单明了</p>
      </div>
    </div>

    <div class="status-section">
      <h2>服务状态</h2>
      <div class="status-grid">
        <div class="status-item">
          <h3>前端服务</h3>
          <p :class="frontendStatus.class">{{ frontendStatus.text }}</p>
        </div>

        <div class="status-item">
          <h3>后端API</h3>
          <p :class="backendStatus.class">{{ backendStatus.text }}</p>
          <button @click="checkBackendStatus" class="check-btn">
            检查状态
          </button>
        </div>
      </div>
    </div>

    <div class="api-info" v-if="apiInfo">
      <h2>API信息</h2>
      <pre>{{ JSON.stringify(apiInfo, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import config from '../config/index.js'

export default defineComponent({
  name: 'Home',

  setup() {
    const frontendStatus = ref({
      text: '运行中',
      class: 'status-healthy'
    })

    const backendStatus = ref({
      text: '检查中...',
      class: 'status-checking'
    })

    const apiInfo = ref(null)

    const checkBackendStatus = async () => {
      try {
        backendStatus.value = {
          text: '检查中...',
          class: 'status-checking'
        }

        // Check health endpoint
        const healthResponse = await axios.get(`${config.apiBaseUrl}/health`)

        if (healthResponse.data.status === 'healthy') {
          backendStatus.value = {
            text: '健康',
            class: 'status-healthy'
          }
        } else {
          backendStatus.value = {
            text: '异常',
            class: 'status-unhealthy'
          }
        }

        // Get API info
        const rootResponse = await axios.get(`${config.apiBaseUrl}/`)
        apiInfo.value = rootResponse.data

      } catch (error) {
        console.error('Backend status check failed:', error)
        backendStatus.value = {
          text: '连接失败',
          class: 'status-unhealthy'
        }

        if (config.debug) {
          console.error('详细错误信息:', error.message)
        }
      }
    }

    onMounted(() => {
      // Auto-check backend status on mount
      checkBackendStatus()

      if (config.debug) {
        console.log('Frontend configuration:', config)
      }
    })

    return {
      frontendStatus,
      backendStatus,
      apiInfo,
      checkBackendStatus
    }
  }
})
</script>

<style scoped>
.home {
  text-align: center;
}

.hero {
  margin-bottom: 3rem;
}

.hero h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.feature-card {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  border: 1px solid #e9ecef;
  transition: transform 0.2s, box-shadow 0.2s;
}

.feature-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.feature-card h3 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.status-section {
  margin-bottom: 2rem;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin-top: 1rem;
}

.status-item {
  background-color: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #e9ecef;
}

.status-item h3 {
  margin-bottom: 1rem;
  color: #2c3e50;
}

.status-healthy {
  color: #27ae60;
  font-weight: 600;
}

.status-unhealthy {
  color: #e74c3c;
  font-weight: 600;
}

.status-checking {
  color: #f39c12;
  font-weight: 600;
}

.check-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 0.5rem;
  transition: background-color 0.2s;
}

.check-btn:hover {
  background-color: #2980b9;
}

.api-info {
  text-align: left;
  margin-top: 2rem;
}

.api-info pre {
  background-color: #f8f9fa;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  border: 1px solid #e9ecef;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }

  .features {
    grid-template-columns: 1fr;
  }

  .status-grid {
    grid-template-columns: 1fr;
  }
}
</style>