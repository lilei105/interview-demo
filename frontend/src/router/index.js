/**
 * Vue Router configuration
 */
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import config from '../config/index.js'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: '首页 - 基础项目框架'
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../components/Error404.vue'),
    meta: {
      title: '页面未找到'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guards
router.beforeEach((to, from, next) => {
  // Set page title
  if (to.meta.title) {
    document.title = to.meta.title
  } else {
    document.title = '基础项目框架'
  }

  // Log navigation in debug mode
  if (config.debug) {
    console.log(`Navigation: ${from.path} -> ${to.path}`)
  }

  next()
})

router.afterEach((to, from) => {
  // Log successful navigation in debug mode
  if (config.debug) {
    console.log(`Navigation completed: ${from.path} -> ${to.path}`)
  }
})

// Error handling
router.onError((error) => {
  console.error('Router error:', error)
  if (config.debug) {
    console.error('Router error details:', error)
  }
})

export default router