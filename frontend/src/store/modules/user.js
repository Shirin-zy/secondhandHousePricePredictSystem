import { getUserInfo, setUserInfo } from '@/utils/storage'
export default {
  namespaced: true,
  state () {
    return {
      // 从本地获取个人权证信息
      userInfo: getUserInfo()
    }
  },
  mutations: {
    setInfo (state, obj) {
      // 修改vuex的状态
      state.userInfo = obj
      // 修改本地存储的信息
      setUserInfo(obj)
    }
  },
  actions: {
    // 清除vuex的登录信息并下线
    logout (context) {
      context.commit('setInfo', {})
    }
  },
  getters: {}
}
