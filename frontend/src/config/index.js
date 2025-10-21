/**
 * Frontend configuration management
 */

// Default configuration
const defaultConfig = {
  // Development server
  host: '127.0.0.1',
  port: 3000,
  hot: true,

  // API configuration
  apiBaseUrl: 'http://127.0.0.1:8000',
  appEnv: 'development',
}

// Environment-based configuration
const envConfig = {
  development: {
    ...defaultConfig,
    debug: true,
  },
  production: {
    ...defaultConfig,
    debug: false,
  },
  testing: {
    ...defaultConfig,
    debug: true,
    port: 3001,
  },
}

// Current environment configuration
const currentEnv = import.meta.env?.MODE || 'development'
const config = envConfig[currentEnv] || envConfig.development

// Override with environment variables if available
if (import.meta.env) {
  config.apiBaseUrl = import.meta.env.VITE_API_BASE_URL || config.apiBaseUrl
  config.appEnv = import.meta.env.VITE_APP_ENV || config.appEnv
}

export default config