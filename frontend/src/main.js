/**
 * Vue3 application entry point
 */
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import config from './config/index.js'

// Create Vue app
const app = createApp(App)

// Use router
app.use(router)

// Global error handler
app.config.errorHandler = (error, instance, info) => {
  console.error('Global Vue error:', error)
  console.error('Component instance:', instance)
  console.error('Error info:', info)

  if (config.debug) {
    // Show detailed error in development
    console.error('Full error details:', error.stack)
  }
}

// Mount app
app.mount('#app')

// Log configuration in development
if (config.debug) {
  console.log('Frontend configuration:', config)
  console.log('Vue3 app mounted successfully')
  console.log('Debug mode enabled')
}