/**
 * Vite configuration for Vue3 frontend
 */
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import config from './src/config/index.js'

export default defineConfig({
  plugins: [vue()],

  // Development server configuration
  server: {
    host: config.host,
    port: config.port,
    hot: config.hot,
    open: false,

    // Proxy API requests to backend
    proxy: {
      '/api': {
        target: config.apiBaseUrl,
        changeOrigin: true,
        secure: false
      },
      '/health': {
        target: config.apiBaseUrl,
        changeOrigin: true,
        secure: false
      }
    }
  },

  // Build configuration
  build: {
    outDir: 'dist',
    sourcemap: config.debug,
    minify: config.debug ? 'esbuild' : 'terser'
  },

  // Environment configuration
  define: {
    __APP_ENV__: JSON.stringify(config.appEnv)
  },

  // Resolve configuration
  resolve: {
    alias: {
      '@': '/src'
    }
  }
})