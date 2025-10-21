<template>
  <div class="error-404">
    <div class="error-content">
      <h1 class="error-code">404</h1>
      <h2 class="error-title">页面未找到</h2>
      <p class="error-message">
        抱歉，您访问的页面不存在。请检查URL是否正确。
      </p>

      <div class="error-actions">
        <button @click="goHome" class="home-btn">
          返回首页
        </button>
        <button @click="goBack" class="back-btn">
          返回上一页
        </button>
      </div>

      <div class="error-details" v-if="showDetails">
        <h3>错误详情</h3>
        <p><strong>当前路径:</strong> ${{ currentPath }}</p>
        <p><strong>时间:</strong> {{ timestamp }}</p>
        <p><strong>用户代理:</strong> {{ userAgent }}</p>
      </div>

      <button
        v-if="!showDetails"
        @click="showDetails = true"
        class="toggle-details"
      >
        显示详细信息
      </button>
      <button
        v-else
        @click="showDetails = false"
        class="toggle-details"
      >
        隐藏详细信息
      </button>
    </div>

    <div class="error-illustration">
      <div class="lost-emoji">🔍</div>
      <p>看起来这个页面迷路了...</p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import config from '../config/index.js'

export default defineComponent({
  name: 'Error404',

  setup() {
    const router = useRouter()
    const route = useRoute()
    const showDetails = ref(false)

    const currentPath = computed(() => route.path)
    const timestamp = computed(() => new Date().toLocaleString())
    const userAgent = computed(() => navigator.userAgent)

    const goHome = () => {
      router.push('/')
    }

    const goBack = () => {
      if (window.history.length > 1) {
        router.go(-1)
      } else {
        router.push('/')
      }
    }

    return {
      currentPath,
      timestamp,
      userAgent,
      showDetails,
      goHome,
      goBack
    }
  }
})
</script>

<style scoped>
.error-404 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  padding: 2rem;
}

.error-content {
  max-width: 600px;
  margin-bottom: 3rem;
}

.error-code {
  font-size: 8rem;
  font-weight: 700;
  color: #e74c3c;
  margin: 0;
  line-height: 1;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.error-title {
  font-size: 2.5rem;
  color: #2c3e50;
  margin: 1rem 0;
  font-weight: 600;
}

.error-message {
  font-size: 1.2rem;
  color: #7f8c8d;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.error-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.home-btn, .back-btn {
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
  display: inline-block;
}

.home-btn {
  background-color: #3498db;
  color: white;
}

.home-btn:hover {
  background-color: #2980b9;
  transform: translateY(-1px);
}

.back-btn {
  background-color: #95a5a6;
  color: white;
}

.back-btn:hover {
  background-color: #7f8c8d;
  transform: translateY(-1px);
}

.toggle-details {
  background-color: transparent;
  color: #3498db;
  border: 1px solid #3498db;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.toggle-details:hover {
  background-color: #3498db;
  color: white;
}

.error-details {
  background-color: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 1.5rem;
  margin: 2rem 0;
  text-align: left;
}

.error-details h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

.error-details p {
  margin: 0.5rem 0;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 0.9rem;
}

.error-illustration {
  text-align: center;
  color: #7f8c8d;
}

.lost-emoji {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.error-illustration p {
  font-size: 1.1rem;
  font-style: italic;
}

@media (max-width: 768px) {
  .error-code {
    font-size: 6rem;
  }

  .error-title {
    font-size: 2rem;
  }

  .error-message {
    font-size: 1rem;
  }

  .error-actions {
    flex-direction: column;
    align-items: center;
  }

  .home-btn, .back-btn {
    width: 200px;
  }
}
</style>