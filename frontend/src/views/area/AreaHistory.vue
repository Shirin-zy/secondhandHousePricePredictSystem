<template>
  <div class="area-history">
    <div class="header">
      <span>首页 / </span>
      <span>小区历史房源数据</span>
    </div>
    <div class="search-box">
      <div class="search-content">小区历史房源数据:</div>
      <div class="search">
        <input
          v-model="area"
          type="text"
          placeholder="输入小区名称(如万和国际)"
        />
        <button @click="search">搜索</button>
      </div>
    </div>
    <div class="content">
      <div class="table-header">
        <span>总价(万元)</span>
        <span>单价(元/㎡)</span>
        <span>关注度</span>
        <span>所在楼层</span>
        <span>建筑面积(㎡)</span>
        <span>户型结构</span>
        <span>装修情况</span>
        <span>配备电梯</span>
        <span>······</span>
      </div>
      <div v-if="history.length <= 0">
        <el-empty description="暂无数据"></el-empty>
      </div>
      <div
        v-for="(item, index) in history"
        :key="index"
        :class="['table-body', { active: index % 2 === 1 }]"
      >
        <span>{{ item.column2 }}万</span>
        <span>{{ item.column3 }}元/㎡</span>
        <span>{{ item.column4 }}</span>
        <span>{{ item.column5 }}</span>
        <span>{{ item.column6 }}㎡</span>
        <span>{{ item.column7 }}</span>
        <span>{{ item.column11 }}</span>
        <span>{{ item.column12 }}</span>
        <span>
          <el-popover placement="bottom" width="400" trigger="click">
            <div>
              <tr>
                <td>
                  <ol>
                    <li>小区名称:</li>
                    <li>总价:</li>
                    <li>单价</li>
                    <li>关注度:</li>
                    <li>所在楼层:</li>
                    <li>建筑面积:</li>
                    <li>户型结构:</li>
                    <li>建筑类型:</li>
                    <li>房屋朝向:</li>
                    <li>建筑结构:</li>
                    <li>装修情况:</li>
                    <li>配备电梯:</li>
                    <li>交易权属:</li>
                    <li>房屋用途:</li>
                    <li>房屋年限:</li>
                    <li>产权所属:</li>
                    <li>抵押信息:</li>
                    <li>所在城市:</li>
                    <li>所在街道:</li>
                  </ol>
                </td>
                <td>
                  <ol style="list-style-type: none">
                    <li>{{ item.column1 }}</li>
                    <li>{{ item.column2 }}万元</li>
                    <li>{{ item.column3 }}元/㎡</li>
                    <li>{{ item.column4 }}</li>
                    <li>{{ item.column5 }}</li>
                    <li>{{ item.column6 }}㎡</li>
                    <li>{{ item.column7 }}</li>
                    <li>{{ item.column8 }}</li>
                    <li>{{ item.column9 }}</li>
                    <li>{{ item.column10 }}</li>
                    <li>{{ item.column11 }}</li>
                    <li>{{ item.column12 }}</li>
                    <li>{{ item.column13 }}</li>
                    <li>{{ item.column14 }}</li>
                    <li>{{ item.column15 }}</li>
                    <li>{{ item.column16 }}</li>
                    <li>{{ item.column17 }}</li>
                    <li>{{ item.column18 }}</li>
                    <li>{{ item.column19 }}</li>
                  </ol>
                </td>
              </tr>
            </div>
            <el-button slot="reference">详情</el-button>
          </el-popover>
        </span>
      </div>
    </div>
  </div>
</template>
<script>
import { getAreaHistory } from '@/api/areainfoseaarch'
export default {
  data () {
    return {
      area: '',
      areaname: '',
      history: []
    }
  },
  methods: {
    search () {
      if (!this.area) {
        this.$message.error('请输入小区名称')
        return
      }
      this.areaname = this.area
    }
  },
  watch: {
    async areaname (newValue) {
      const data = await getAreaHistory(newValue)
      this.history = data.data[0].data
      console.log(this.history[0].column1)
    }
  }
}
</script>
<style lang="less" scoped>
.area-history {
  padding: 20px 20px 0;
  box-sizing: border-box;
}
.fixed {
  position: fixed;
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
.search-box {
  width: 1650px;
  height: 50px;
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  .search-content {
    padding-left: 20px;
    line-height: 50px;
    font-size: 24px;
  }
  .search {
    width: 250px;
    height: 50px;

    input {
      margin-top: 5px;
      border-radius: 5px;
      height: 40px;
      width: 200px;
      border: 1px;
      border: 1px solid rgba(0, 0, 0, 0.5);
    }
    button {
      margin-top: 5px;
      border-radius: 5px;
      height: 40px;
      width: 50px;
      background-color: #007bff;
      border-color: #007bff;
      color: #fff;
    }
  }
}
.content {
  .table-header {
    width: 1650px;
    height: 50px;
    background-color: #007bff;
    display: flex;
    justify-content: space-around;
    border-radius: 10px;
    span {
      color: #fff;
      line-height: 50px;
      font-size: 18px;
    }
  }
  .table-body {
    width: 1650px;
    height: 40px;
    background-color: #f7f7f7;
    display: flex;
    justify-content: space-around;
    span {
      color: #000;
      width: 183.3px;
      line-height: 40px;
      font-size: 16px;
      text-align: center;
    }
    button {
      background-color: #85ce61;
      color: #fff;
      border: none;
      border-radius: 5px;
      height: 30px;
      margin-top: 5px;
      span {
        line-height: 30px;
      }
    }
  }
  .active {
    background-color: #fff;
  }
}
</style>
