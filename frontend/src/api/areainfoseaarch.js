import request from '@/utils/request'
// 查询小区基本信息
export const getAreaInfo = (area) => {
  return request.get('/info/area', {
    params: {
      area
    }
  })
}

// 查询小区房屋面积分布信息
export const getAreaSection = (area) => {
  return request.get('/info/area/areasection', {
    params: {
      area
    }
  })
}

// 查询装修情况
export const getDecorate = (area) => {
  return request.get('/info/area/decorate', {
    params: {
      area
    }
  })
}

// 查询楼层信息
export const getFloor = (area) => {
  return request.get('/info/area/floor', {
    params: {
      area
    }
  })
}

// 查询小区房屋单价分布信息
export const getPriceSection = (area) => {
  return request.get('/info/area/price', {
    params: {
      area
    }
  })
}

// 查询小区历史房源数据
export const getAreaHistory = (area) => {
  return request.get('/info/area/history', {
    params: {
      area
    }
  })
}

// 用户注册
export const register = (username, password) => {
  return request.get('/index/register', {
    params: {
      username,
      password
    }
  })
}

// 用户登录
export const login = (username, password) => {
  return request.get('/index/login', {
    params: {
      username,
      password
    }
  })
}

// 修改头像信息
export const updateAvatar = (username, avatar) => {
  return request.get('/index/avatar', {
    params: {
      username,
      avatar
    }
  })
}

// 房价预测接口
export const predict = (obj) => {
  return request.get('/index/perdict', {
    params: {
      xiaoquming: obj.xiaoquming,
      louceng: obj.louceng,
      mianji: obj.mianji,
      huxing: obj.huxing,
      jianzhuleixing: obj.jianzhuleixing,
      chaoxiang: obj.chaoxiang,
      jianzhujiegou: obj.jianzhujiegou,
      zhuangxiu: obj.zhuangxiu,
      dianti: obj.dianti,
      jiaoyiquanshu: obj.jiaoyiquanshu,
      yongtu: obj.yongtu,
      age: obj.age,
      chanquan: obj.chanquan,
      city: obj.city,
      bedroom: obj.bedroom,
      keting: obj.keting,
      chufang: obj.chufang,
      cesuo: obj.cesuo
    }
  })
}
