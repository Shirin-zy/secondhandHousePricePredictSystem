import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.min'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import * as echarts from 'echarts'
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$echarts = echarts

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount('#app')
