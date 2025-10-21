<template>
  <div id="app">
    <nav class="navbar">
      <h1>基础项目框架</h1>
      <div class="nav-links">
        <router-link to="/">首页</router-link>
      </div>
    </nav>

    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <p>&copy; 2025 基础项目框架 - Vue3 + FastAPI</p>
    </footer>
  </div>
</template>

<script>
import { defineComponent, onErrorCaptured } from 'vue'
import config from './config/index.js'

export default defineComponent({
  name: 'App',

  setup() {
    // Handle global errors
    onErrorCaptured((error, instance, info) => {
      console.error('Global error captured:', error)
      console.error('Component instance:', instance)
      console.error('Error info:', info)

      if (config.debug) {
        alert(`发生错误: ${error.message}`)
      }

      return false // Prevent error from propagating further
    })

    return {}
  }
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: #333;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  background-color: #2c3e50;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar h1 {
  font-size: 1.5rem;
  font-weight: 600;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  background-color: #34495e;
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.footer {
  background-color: #ecf0f1;
  padding: 1rem;
  text-align: center;
  color: #7f8c8d;
}

/* Responsive design */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .main-content {
    padding: 1rem;
  }
}
</style>