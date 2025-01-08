<template>
  <div class="avatar-change">
    <div class="card">
      <div @click="$router.push('/index/city')" class="back"><i class="el-icon-back"></i></div>
      <div class="avatar">
        <el-avatar :size="80" :src="basephoto"></el-avatar>
      </div>
      <span>新头像地址</span>
      <input
        type="text"
        autocomplete="off"
        name="text"
        class="input"
        placeholder="URL of new avatar"
        v-model="avatar"
      />
      <p class="info"></p>
      <button @click="changeAvatar">submint</button>
    </div>
  </div>
</template>
<script>
import { updateAvatar } from '@/api/areainfoseaarch'
export default {
  data () {
    return {
      basephoto: this.$store.state.user.userInfo.avatar,
      avatar: '',
      info: {
        token: '',
        userId: '',
        avatar: ''
      }
    }
  },
  methods: {
    async changeAvatar () {
      if (this.avatar === '') {
        alert('请输入图片地址')
      } else {
        const data = await updateAvatar(
          this.$store.state.user.userInfo.userId,
          this.avatar
        )
        if (data.data[0].result === 'succeed') {
          alert('更新成功')
          // 更新vuex中的用户信息
          this.info.token = this.$store.state.user.userInfo.token
          this.info.userId = this.$store.state.user.userInfo.userId
          this.info.avatar = this.avatar
          this.$store.commit('user/setInfo', this.info)
        }
      }
    }
  }
}
</script>
<style lang="less" scoped>
/* From Uiverse.io by Praashoo7 */
.card {
  width: 280px;
  height: 400px;
  background: #acabab;
  transition: 1s ease-in-out;
  clip-path: polygon(
    30px 0%,
    100% 0,
    100% calc(100% - 30px),
    calc(100% - 30px) 100%,
    0 100%,
    0% 30px
  );
  border-top-right-radius: 20px;
  border-bottom-left-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  .back{
    position: absolute;
    left: 30px;
    top: 20px;
  }
  .avatar {
    margin-top: 20px;
  }
  span {
    font-size: 16px;
    color: #ffffff;
    font-weight: 700;
    margin-top: 20px;
  }
  .input {
    height: 40px;
    border: none;
    outline: none;
    border-radius: 15px;
    padding: 1em;
    background-color: #ccc;
    box-shadow: inset 2px 5px 10px rgba(0, 0, 0, 0.3);
    transition: 300ms ease-in-out;
    margin-top: 20px;
    &:focus {
      background-color: white;
      transform: scale(1.05);
      box-shadow: 13px 13px 100px #969696, -13px -13px 100px #ffffff;
    }
  }
  button {
    padding: 0.8em 1.7em;
    display: block;
    margin: auto;
    border-radius: 25px;
    border: none;
    font-weight: bold;
    background: #ffffff;
    color: rgb(0, 0, 0);
    transition: 0.4s ease-in-out;
    &:hover {
      background: red;
      color: white;
      cursor: pointer;
    }
  }
}
.avatar-change {
  margin-left: 50%;
  transform: translate(-140px, 100px);
}
</style>
