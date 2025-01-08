const INFO_KEY = 'hourse-info'
// 1.用户登录权证持久化到本地
// 获取用户信息
export const getUserInfo = () => {
  // 默认信息
  const defaultInfo = {
    token: '',
    userId: '',
    avatat: ''
  }
  // 如果获取到相关登录信息就返回，没有登录信息就返回默认信息，避免解析空信息导致错误
  const info = localStorage.getItem(INFO_KEY)
  return info ? JSON.parse(info) : defaultInfo
}

// 设置用户信息
export const setUserInfo = (obj) => {
  localStorage.setItem(INFO_KEY, JSON.stringify(obj))
}

// 移除用户信息
export const removeUserInfo = () => {
  localStorage.removeItem(INFO_KEY)
}
