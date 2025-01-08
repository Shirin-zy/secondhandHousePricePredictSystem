<template>
  <div>
    <el-card class="login"
      ><template #header>
        <div>
          <span>登录|注册</span>
        </div>
      </template>
      <div>
        <!-- 登录UI界面 -->
        <el-tabs v-model="currentIndex" @tab-click="clickTabsHandle">
          <el-tab-pane label="登录" name="login">
            <el-form
              :model="loginForm"
              status-icon
              :rules="rules"
              ref="loginForm"
            >
              <el-form-item label="用户名" label-width="80px" prop="username">
                <el-input type="username" v-model="loginForm.username" />
              </el-form-item>
              <el-form-item label="密码" label-width="80px" prop="password">
                <el-input type="password" v-model="loginForm.password" />
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitLoginForm('loginForm')">
                  登录
                </el-button>
                <el-button @click="resetForm"> 重置 </el-button>
              </el-form-item>
            </el-form>
          </el-tab-pane>
          <!-- 注册UI界面 -->
          <el-tab-pane label="注册" name="register">
            <el-form
              :model="registerForm"
              status-icon
              :rules="rules"
              ref="registerForm"
            >
              <el-form-item label="用户名" label-width="80px" prop="username">
                <el-input type=" username" v-model="registerForm.username" />
              </el-form-item>
              <el-form-item label="密码" label-width="80px" prop="password">
                <el-input type=" password" v-model="registerForm.password" />
              </el-form-item>
              <el-form-item label="确认密码" label-width="80px" prop="confirm">
                <el-input type=" confirm" v-model="registerForm.confirm" />
              </el-form-item>
              <el-form-item>
                <el-button
                  type="primary"
                  @click="submitRegisterForm('registerForm')"
                >
                  提交
                </el-button>
              </el-form-item>
            </el-form>
          </el-tab-pane>
        </el-tabs>
      </div></el-card
    >
  </div>
</template>
<script>
import { login, register } from '@/api/areainfoseaarch'
// import { $refs, reactive } from "vue";
export default {
  data () {
    // 创建验证规则，注册与登录使用同一套验证规则
    const validateUsername = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        callback()
      }
    }
    const validateConfirm = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请确认密码'))
      } else if (value !== this.registerForm.password) {
        callback(new Error('两次密码不一致'))
      } else {
        callback()
      }
    }
    return {
      currentIndex: 'login',
      loginForm: {
        username: '',
        password: ''
      },
      registerForm: {
        username: '',
        password: '',
        confirm: ''
      },
      info: {
        token: '',
        userId: '',
        avatar: ''
      },
      // 验证规则
      rules: {
        username: [
          {
            validator: validateUsername,
            trigger: 'blur'
          }
        ],
        password: [
          {
            validator: validatePassword,
            trigger: 'blur'
          }
        ],
        confirm: [
          {
            validator: validateConfirm,
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    resetForm () {
      (this.loginForm.password = '')((this.loginForm.username = ''))
    },
    async submitLoginForm () {
      if (this.loginForm.username === '' || this.loginForm.password === '') {
        alert('请输入用户名或密码')
      } else {
        const data = await login(
          this.loginForm.username,
          this.loginForm.password
        )
        if (data.data[0].result === 'fail') {
          alert('用户名或密码错误')
        } else {
          this.info.token = data.data[0].token
          this.info.userId = this.loginForm.username
          this.info.avatar = data.data[0].avatar
          this.$store.commit('user/setInfo', this.info)
          const url = this.$route.query.backUrl || '/index/city'
          this.$router.push(url)
          alert('登录成功')
        }
      }
    },
    async submitRegisterForm () {
      if (
        this.registerForm.username === '' ||
        this.registerForm.password === '' ||
        this.registerForm.confirm === ''
      ) {
        alert('请输入完整信息')
      }
      if (this.registerForm.password !== this.registerForm.confirm) {
        alert('两次密码输入不一致')
      } else {
        const data = await register(
          this.registerForm.username,
          this.registerForm.password
        )
        if (data.data[0].result === 'fail') {
          alert('用户名已存在')
        }
        if (data.data[0].result === 'succeed') {
          alert('注册成功')
        }
      }
    }
  }
}
</script>
<style scoped>
.login {
  width: 600px;
  margin: 100px auto;
  text-align: center;
  .box-card {
    width: 600px;
    margin: 100px auto;
    .label {
      width: 480px;
      margin: 20px auto;
    }
  }
}
</style>
