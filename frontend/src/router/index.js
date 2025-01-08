import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: () => import('@/views/layout/IndexPage.vue')
  },
  {
    path: '/login',
    component: () => import('@/views/login/LoginPage.vue')
  },
  {
    path: '/index',
    component: () => import('@/views/layout/LayOut.vue'),
    children: [
      {
        path: '/index/city',
        component: () => import('@/views/city/CityPrice.vue')
      },
      {
        path: '/index/areaprice',
        component: () => import('@/views/area/AreaPrice.vue')
      },
      {
        path: '/index/areahistory',
        component: () => import('@/views/area/AreaHistory.vue')
      },
      {
        path: '/index/areainfo/:id',
        component: () => import('@/views/area/AreaInfoSearch.vue')
      },
      {
        path: '/index/predict',
        component: () => import('@/views/predict/PricePredict.vue')
      },
      {
        path: '/index/predict/input',
        component: () => import('@/views/predict/PredictInput.vue')
      }
    ]
  },
  {
    path: '/index/avatar',
    component: () => import('@/views/login/AvatarChange.vue')
  }
]

const router = new VueRouter({
  routes
})

// 需要有权限的页面
const privtePage = ['/index/areaprice', '/index/areahistory', '/index/predict']
// 配置全局导航守卫
// (1)next() 直接放行
// (2)next(路径) 进行拦截_
router.beforeEach((to, from, next) => {
  // 非隐私页面直接可访问
  if (!privtePage.includes(to.path)) {
    next()
    return
  }
  // 隐私页面进行权限验证
  const token = store.state.user.userInfo.token
  if (token) {
    next()
  } else {
    next('/login')
  }
})

export default router
