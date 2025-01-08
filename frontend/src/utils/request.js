import axios from 'axios'

// 创建axios实例并对其进行自定义，这样可以避免影响到原始的axios实例
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8444',
  timeout: 5000,
  headers: { platform: 'h5' }
})

// 自定义配置-请求/响应拦截器
// 1.添加请求拦截器
instance.interceptors.request.use(
  function (config) {
    // 发起请求时添加loading效果并禁止其它操作以避免重复请求
    return config
  },
  function (error) {
    // 对请求错误做些什么
    return Promise.reject(error)
  }
)

// 2.添加响应拦截器
instance.interceptors.response.use(
  function (response) {
    // 对响应数据做点什么
    const res = response.data
    return res
  },
  function (error) {
    // 对响应错误做点什么
    return Promise.reject(error)
  }
)

export default instance
