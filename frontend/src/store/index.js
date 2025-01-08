import Vue from 'vue'
import Vuex from 'vuex'
import user from '@/store/modules/user'

Vue.use(Vuex)
Vue.config.devtools = true

export default new Vuex.Store({
  getters: {
    token (state) {
      return state.user.userInfo.token
    }
  },
  modules: {
    user
  }
})
