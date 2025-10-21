<template>
  <div class="hello-world">
    <div class="message">
      <h2>{{ message }}</h2>
      <p>{{ description }}</p>
    </div>

    <div class="actions">
      <button @click="showAlert" class="action-btn">
        显示消息
      </button>
      <button @click="incrementCounter" class="action-btn">
        点击计数: {{ counter }}
      </button>
    </div>

    <div class="api-test" v-if="showApiTest">
      <h3>API测试</h3>
      <button @click="testApi" class="test-btn" :disabled="loading">
        {{ loading ? '测试中...' : '测试后端API' }}
      </button>
      <div v-if="apiResult" class="api-result">
        <h4>API响应:</h4>
        <pre>{{ JSON.stringify(apiResult, null, 2) }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import axios from 'axios'
import config from '../config/index.js'

export default defineComponent({
  name: 'HelloWorld',

  props: {
    msg: {
      type: String,
      default: 'Hello World!'
    }
  },

  setup(props) {
    const counter = ref(0)
    const loading = ref(false)
    const apiResult = ref(null)

    const message = computed(() => props.msg)
    const description = computed(() => '这是一个Vue3组件示例，展示基础功能')
    const showApiTest = computed(() => config.debug)

    const showAlert = () => {
      alert(`当前计数: ${counter.value}`)
    }

    const incrementCounter = () => {
      counter.value++
    }

    const testApi = async () => {
      try {
        loading.value = true
        const response = await axios.get(`${config.apiBaseUrl}/`)
        apiResult.value = response.data
      } catch (error) {
        console.error('API测试失败:', error)
        apiResult.value = {
          error: 'API请求失败',
          message: error.message
        }
      } finally {
        loading.value = false
      }
    }

    return {
      message,
      description,
      counter,
      loading,
      apiResult,
      showApiTest,
      showAlert,
      incrementCounter,
      testApi
    }
  }
})
</script>

<style scoped>
.hello-world {
  text-align: center;
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #e9ecef;
  margin: 1rem 0;
}

.message h2 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.message p {
  color: #7f8c8d;
  margin-bottom: 2rem;
}

.actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.action-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.action-btn:hover {
  background-color: #2980b9;
}

.api-test {
  margin-top: 2rem;
  text-align: left;
}

.api-test h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

.test-btn {
  background-color: #27ae60;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  display: block;
  margin: 0 auto 1rem;
  transition: background-color 0.2s;
}

.test-btn:hover:not(:disabled) {
  background-color: #229954;
}

.test-btn:disabled {
  background-color: #95a5a6;
  cursor: not-allowed;
}

.api-result {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
}

.api-result h4 {
  margin-bottom: 0.5rem;
}

.api-result pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
}

@media (max-width: 768px) {
  .actions {
    flex-direction: column;
    align-items: center;
  }

  .action-btn {
    width: 200px;
  }
}
</style>