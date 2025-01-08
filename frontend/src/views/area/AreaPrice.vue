<template>
  <div class="area-price">
    <div class="header"><span>首页 / </span><span>小区房价数据查询</span></div>
    <div class="content">
      <div class="body">
        <img src="@/assets/images/logo.png" alt="" />
        <h1>房知道</h1>
        <span class="title">杭州二手房数据查询</span>
        <span class="subtitle"
          >-旨在提供历史成交房价和网签数据，帮助用户更好的评估房产和预测未来的走势</span
        >
        <div class="search">
          <input v-model="area" type="text" placeholder="请输小区名称" />
          <button @click="search">搜索</button>
        </div>
        <div class="hot">
          <strong>热门搜索：</strong>
          <p @click="hotkey('万和国际')">万和国际</p>
          <p @click="hotkey('万泰城章')">万泰城章</p>
          <p @click="hotkey('潘水南苑')">潘水南苑</p>
          <p @click="hotkey('玉都枫景')">玉都枫景</p>
          <p @click="hotkey('玲珑府')">玲珑府</p>
        </div>
      </div>
      <div class="footer">
        <div><p>热门小区房价数据：</p></div>
        <table>
          <thead>
            <tr>
              <th>小区名称</th>
              <th>平均成交价格(万元)</th>
              <th>每平方均价(元)</th>
              <th>平均关注度</th>
              <th>历史成交数(套)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>丁郡</td>
              <td>491</td>
              <td>39940</td>
              <td>19</td>
              <td>11</td>
            </tr>
            <tr>
              <td>龙华府公寓</td>
              <td>394</td>
              <td>30937</td>
              <td>17</td>
              <td>14</td>
            </tr>
            <tr>
              <td>都西花庭</td>
              <td>497</td>
              <td>40451</td>
              <td>17</td>
              <td>15</td>
            </tr>
            <tr>
              <td>科郡西澜山</td>
              <td>699</td>
              <td>46041</td>
              <td>21</td>
              <td>15</td>
            </tr>
            <tr>
              <td>渚文化村白鹭郡北</td>
              <td>491</td>
              <td>29108</td>
              <td>40</td>
              <td>13</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      area: ''
    }
  },
  methods: {
    search () {
      if (!this.area) {
        this.$message.error('请输入小区名称')
        return
      }
      this.$router.push(`/index/areainfo/${this.area}`)
    },
    hotkey (key) {
      this.area = key
    }
  }
}
</script>
<style lang="less" scoped>
.area-price {
  padding: 20px;
  box-sizing: border-box;
}
.header {
  width: 1650px;
  height: 50px;
  background-color: #e9ecef;
  border-radius: 10px;
  line-height: 50px;
  padding-left: 20px;
  span:nth-child(2) {
    color: #007bff;
  }
}
.content {
  margin-top: 40px;
  .body {
    position: relative;
    width: 1650px;
    height: 420px;
    background-color: #e9ecef;
    border-radius: 10px;
    text-align: center;
    padding: 50px auto;
    h1 {
      position: absolute;
      top: 100px;
      left: 50%;
      transform: translate(-50%);
      font-size: 50px;
      font-style: italic;
      color: gray;
    }
    .title {
      display: block;
      font-size: 36px;
    }
    .subtitle {
      display: block;
      font-size: 18px;
    }
    .search {
      margin-top: 10px;
      width: 300px;
      height: 50px;
      display: inline-block;
      input {
        border-radius: 5px;
        height: 40px;
        border: 1px;
      }
      button {
        border-radius: 5px;
        height: 40px;
        background-color: #007bff;
        border-color: #007bff;
        color: #fff;
      }
    }
    .hot {
      margin-top: 20px;
      width: 500px;
      height: 50px;
      margin-left: 50%;
      transform: translate(-50%);
      display: flex;
      justify-content: space-between;
      line-height: 50px;
      p {
        &:hover {
          color: #007bff;
        }
      }
    }
  }
  .footer {
    width: 1650px;
    height: 340px;
    margin-top: 20px;
    border-radius: 10px;
    border: 1px solid rgba(0, 0, 0, 0.125);
    div:nth-child(1) {
      width: 1650px;
      height: 60px;
      background-color: rgba(0, 0, 0, 0.03);
      border-bottom: 1px solid rgba(0, 0, 0, 0.125);
      border-radius: 10px 10px 0 0;
      p {
        line-height: 60px;
        padding-left: 20px;
        font-size: 18px;
      }
    }
    table {
      margin-top: 15px;
      margin-left: 25px;
      border-collapse: collapse;
      width: 1600px;
      height: 250px;
      th,
      td {
        border: 1px solid rgba(0, 0, 0, 0.125);
      }
    }
  }
}
</style>
