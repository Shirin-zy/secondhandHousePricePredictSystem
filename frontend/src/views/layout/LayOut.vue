<template>
  <div>
    <div class="header">
      <h2>房知道</h2>
      <div>
        <div>
          <el-select v-model="value" placeholder="城市选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>
        <div @click="$router.push('/home')">首页</div>
        <div @click="changeAvatar">
          <el-avatar :size="50" :src="basephoto"></el-avatar>
        </div>
        <div @click="gologin">
          <p>{{ username }}</p>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="side">
        <el-col :span="24">
          <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-menu-item index="1">
              <template slot="title">
                <i class="el-icon-map-location"></i>
                <span @click="$router.push('/index/city')">区域房价概览</span>
              </template>
            </el-menu-item>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-office-building"></i>
                <span>小区数据查询</span>
              </template>
              <el-menu-item
                @click="$router.push('/index/areaprice')"
                index="2-1"
                >小区房价数据查询</el-menu-item
              >
              <el-menu-item
                @click="$router.push('/index/areahistory')"
                index="2-2"
                >小区历史房源数据</el-menu-item
              >
            </el-submenu>
            <el-menu-item index="3">
              <template slot="title">
                <i class="el-icon-data-line"></i>
                <span @click="$router.push('/index/predict')"
                  >房价评估预测</span
                >
              </template>
            </el-menu-item>
            <el-submenu index="4">
              <template slot="title">
                <i class="el-icon-setting"></i>
                <span>系统设置</span>
              </template>
              <el-menu-item index="4-1"
                ><el-popconfirm title="是否退出登录" @confirm="logout">
                  <el-button slot="reference">退出登录</el-button>
                </el-popconfirm></el-menu-item
              >
              <el-menu-item index="4-2">系统设置</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-col>
      </div>
      <div class="body"><router-view></router-view></div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      options: [
        {
          value: '选项1',
          label: '滨江'
        },
        {
          value: '选项2',
          label: '富阳'
        },
        {
          value: '选项3',
          label: '拱墅'
        },
        {
          value: '选项4',
          label: '临安'
        },
        {
          value: '选项5',
          label: '临平'
        },
        {
          value: '选项6',
          label: '钱塘'
        },
        {
          value: '选项7',
          label: '上城'
        },
        {
          value: '选项8',
          label: '萧山'
        },
        {
          value: '选项9',
          label: '西湖'
        },
        {
          value: '选项10',
          label: '余杭'
        }
      ],
      value: '',
      // 从veuex中获取用户头像信息，未读取到则使用默认值
      basephoto:
        this.$store.state.user.userInfo.avatar ||
        'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    logout () {
      console.log('退出登录')
      // 调用vuex的logout方法清除登录信息
      this.$store.dispatch('user/logout')
      this.basephoto =
        'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
    },
    gologin () {
      if (this.username === '请登录') {
        this.$router.push('/login')
      }
    },
    changeAvatar () {
      if (this.token) {
        this.$router.push('/index/avatar')
      }
    }
  },
  computed: {
    username () {
      return this.$store.state.user.userInfo.userId || '请登录'
    },
    token () {
      return this.$store.state.user.userInfo.token || ''
    }
  }
}
</script>
<style lang="less" scoped>
.header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 60px;
  background-color: #545c64;
  h2 {
    color: #fff;
    line-height: 60px;
    margin-left: 20px;
    font-style: italic;
  }
  div {
    width: 320px;
    height: 60px;
    display: flex;
    div:nth-child(1) {
      width: 120px;
      line-height: 60px;
      .el-input__inner {
        background-color: #007bff !important;
        border: none;
        color: #fff;
      }
    }
    div:nth-child(2) {
      width: 80px;
      line-height: 60px;
      padding: 0 20px;
      color: rgba(255, 255, 255, 0.5);
      &:hover {
        color: rgba(255, 255, 255);
      }
    }
    div:nth-child(3) {
      width: 60px;
      height: 60px;
      align-items: center;
    }
    div:nth-child(4) {
      width: 60px;
      height: 60px;
      p {
        line-height: 60px;
        color: #fff;
      }
    }
  }
}
.content {
  width: 100%;
  height: 914px;
  display: flex;
  .side {
    width: 200px;
    background-color: #545c64;
    .el-menu-item {
      &:hover {
        .el-button {
          background-color: #434a50;
        }
      }
      .el-button {
        border: none;
        background-color: #545c64;
        color: #fff;
        &:hover {
          background-color: #434a50;
          color: #fff;
        }
      }
    }
  }
  .body {
    flex: 1;
    overflow-y: auto;
  }
}
.router-link-active {
  text-decoration: none;
  color: #ffd04b;
}
</style>
