<template>
  <div class="predict-input">
    <div class="header">
      <span>首页 / </span>
      <span @click="$router.push('/index/predict')">房价评估预测 / </span>
      <span>房屋信息输入</span>
    </div>
    <div class="body">
      <div class="left">
        <div class="input">
          <input
            placeholder="小区名称"
            class="input-style"
            type="text"
            v-model="info.xiaoquming"
          />
        </div>
        <div class="input">
          <input
            placeholder="所在楼层"
            class="input-style"
            type="text"
            v-model="info.louceng"
          />
        </div>
        <div class="input">
          <input
            placeholder="建筑面积"
            class="input-style"
            type="text"
            v-model="info.mianji"
          />
        </div>
        <div class="input">
          <input
            placeholder="户型结构"
            class="input-style"
            type="text"
            v-model="info.huxing"
          />
        </div>
        <div class="input">
          <input
            placeholder="建筑类型"
            class="input-style"
            type="text"
            v-model="info.jianzhuleixing"
          />
        </div>
        <div class="input">
          <input
            placeholder="房屋朝向"
            class="input-style"
            type="text"
            v-model="info.chaoxiang"
          />
        </div>
        <div class="input">
          <input
            placeholder="建筑结构"
            class="input-style"
            type="text"
            v-model="info.jianzhujiegou"
          />
        </div>
        <div class="input">
          <input
            placeholder="装修情况"
            class="input-style"
            type="text"
            v-model="info.zhuangxiu"
          />
        </div>
        <div class="input">
          <input
            placeholder="电梯配备"
            class="input-style"
            type="text"
            v-model="info.dianti"
          />
        </div>
        <div class="input">
          <input
            placeholder="交易权属"
            class="input-style"
            type="text"
            v-model="info.jiaoyiquanshu"
          />
        </div>
        <div class="input">
          <input
            placeholder="房屋用途"
            class="input-style"
            type="text"
            v-model="info.yongtu"
          />
        </div>
        <div class="input">
          <input
            placeholder="房屋年限"
            class="input-style"
            type="text"
            v-model="info.age"
          />
        </div>
        <div class="input">
          <input
            placeholder="产权所属"
            class="input-style"
            type="text"
            v-model="info.chanquan"
          />
        </div>
        <div class="input">
          <input
            placeholder="所在城市"
            class="input-style"
            type="text"
            v-model="info.city"
          />
        </div>
        <div class="input">
          <input
            placeholder="卧室数量"
            class="input-style"
            type="text"
            v-model="info.bedroom"
          />
        </div>
        <div class="input">
          <input
            placeholder="客餐厅数"
            class="input-style"
            type="text"
            v-model="info.keting"
          />
        </div>
        <div class="input">
          <input
            placeholder="厨房数目"
            class="input-style"
            type="text"
            v-model="info.chufang"
          />
        </div>
        <div class="input">
          <input
            placeholder="厕所数量"
            class="input-style"
            type="text"
            v-model="info.cesuo"
          />
        </div>
      </div>
      <div class="right">
        <div class="button">
          <button class="submit" @click="submit">submit</button>
        </div>
        <div class="button">
          <button class="out">
            <span class="test" @click="fillData(test1)"> 测试数据1 </span>
          </button>
        </div>
        <div class="button">
          <button class="out">
            <span class="test" @click="fillData(test2)"> 测试数据2 </span>
          </button>
        </div>
        <div class="button">
          <button class="out">
            <span class="test" @click="fillData(test3)"> 测试数据3 </span>
          </button>
        </div>
        <div class="button">
          <button class="out">
            <span class="test" @click="fillData(test4)"> 测试数据4 </span>
          </button>
        </div>
      </div>
      <div class="result" v-show="price">
        <div class="reset" @click="reset"><i class="el-icon-refresh"></i></div>
        <img src="@/assets/images/price.png" alt="" /><span
          >{{ this.price }}W</span
        >
      </div>
    </div>
    <div class="footer">
      <p>@cqut重庆理工大学-计算机科学与工程学院</p>
      <p>
        本预测结果基于算法取得,具有一定的参考性,但非真实价格,具体情况请以实际为准
      </p>
    </div>
  </div>
</template>
<script>
import { predict } from '@/api/areainfoseaarch'
export default {
  data () {
    return {
      price: null,
      info: {
        xiaoquming: '',
        louceng: null,
        mianji: null,
        huxing: '',
        jianzhuleixing: '',
        chaoxiang: '',
        jianzhujiegou: '',
        zhuangxiu: '',
        dianti: '',
        jiaoyiquanshu: '',
        yongtu: '',
        age: null,
        chanquan: '',
        city: '',
        bedroom: null,
        keting: null,
        chufang: null,
        cesuo: null
      },
      test1: {
        xiaoquming: '欣盛东方郡西区',
        louceng: 18,
        mianji: 134.68,
        huxing: '平层',
        jianzhuleixing: '板塔结合',
        chaoxiang: '南 北',
        jianzhujiegou: '钢混结构',
        zhuangxiu: '精装',
        dianti: '有',
        jiaoyiquanshu: '商品房',
        yongtu: '普通住宅',
        age: '13',
        chanquan: '共有',
        city: '滨江',
        bedroom: 3,
        keting: 2,
        chufang: 1,
        cesuo: 2
      },
      test2: {
        xiaoquming: '彩虹城',
        louceng: 29,
        mianji: 126.91,
        huxing: '平层',
        jianzhuleixing: '板楼',
        chaoxiang: '南',
        jianzhujiegou: '钢混结构',
        zhuangxiu: '精装',
        dianti: '有',
        jiaoyiquanshu: '商品房',
        yongtu: '普通住宅',
        age: '13',
        chanquan: '共有',
        city: '滨江',
        bedroom: 3,
        keting: 1,
        chufang: 1,
        cesuo: 2
      },
      test3: {
        xiaoquming: '柳浪阁',
        louceng: 7,
        mianji: 34.73,
        huxing: '平层',
        jianzhuleixing: '板楼',
        chaoxiang: '南',
        jianzhujiegou: '砖混结构',
        zhuangxiu: '精装',
        dianti: '无',
        jiaoyiquanshu: '已购公房',
        yongtu: '普通住宅',
        age: '8',
        chanquan: '共有',
        city: '上城',
        bedroom: 1,
        keting: 1,
        chufang: 1,
        cesuo: 1
      },
      test4: {
        xiaoquming: '逸居城',
        louceng: 6,
        mianji: 90.69,
        huxing: '平层',
        jianzhuleixing: '板塔结合',
        chaoxiang: '东',
        jianzhujiegou: '钢混结构',
        zhuangxiu: '精装',
        dianti: '无',
        jiaoyiquanshu: '商品房',
        yongtu: '普通住宅',
        age: '13',
        chanquan: '共有',
        city: '余杭',
        bedroom: 3,
        keting: 2,
        chufang: 1,
        cesuo: 1
      }
    }
  },
  methods: {
    async submit () {
      console.log(this.info)
      const data = await predict(this.info)
      this.price = data.data[0].result
      console.log(this.price)
    },
    fillData (obj) {
      this.info = obj
    },
    reset () {
      this.price = null
      this.info = {}
    }
  }
}
</script>
<style lang="less" scoped>
.predict-input {
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
  span:nth-child(3) {
    color: #007bff;
  }
}
.body {
  width: 1650px;
  height: 650px;
  background-color: #e9ecef;
  margin-top: 40px;
  padding: 100px 0 100px 100px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-content: space-between;
  .left {
    overflow: hidden;
    height: 450px;
    width: 1200px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-content: space-between;
    .input {
      width: 400px;
      height: 50px;
      .input-style {
        width: 350px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        color: #555;
        outline: none;
        &:focus {
          border-color: #007bff;
          box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
        }
      }
    }
  }
  .right {
    overflow: hidden;
    height: 450px;
    width: 350px;
    padding: 20px 80px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-content: space-between;
    .button {
      height: 50px;
      width: 200px;
      overflow: hidden;
      align-items: center;
      text-align: center;
      .submit {
        display: flex;
        align-items: center;
        justify-content: center;
        outline: none;
        cursor: pointer;
        width: 150px;
        height: 50px;
        margin-left: 20px;
        background-image: linear-gradient(
          to top,
          #d8d9db 0%,
          #fff 80%,
          #fdfdfd 100%
        );
        border-radius: 30px;
        border: 1px solid #8f9092;
        transition: all 0.2s ease;
        font-family: "Source Sans Pro", sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #606060;
        text-shadow: 0 1px #fff;
        &:hover {
          box-shadow: 0 4px 3px 1px #fcfcfc, 0 6px 8px #d6d7d9,
            0 -4px 4px #cecfd1, 0 -6px 4px #fefefe, inset 0 0 3px 3px #cecfd1;
        }
        &:active {
          box-shadow: 0 4px 3px 1px #fcfcfc, 0 6px 8px #d6d7d9,
            0 -4px 4px #cecfd1, 0 -6px 4px #fefefe, inset 0 0 5px 3px #999,
            inset 0 0 30px #aaa;
        }
        &:focus {
          box-shadow: 0 4px 3px 1px #fcfcfc, 0 6px 8px #d6d7d9,
            0 -4px 4px #cecfd1, 0 -6px 4px #fefefe, inset 0 0 5px 3px #999,
            inset 0 0 30px #aaa;
        }
      }
      .out {
        color: black;
        text-decoration: none;
        cursor: pointer;
        outline: none;
        border: none;
        background: #fff;
        .test {
          width: 120px;
          height: 50px;
          float: left;
          transition: 0.5s linear;
          position: relative;
          display: block;
          overflow: hidden;
          padding: 15px;
          text-align: center;
          margin: 0 5px;
          background: transparent;
          text-transform: uppercase;
          font-weight: 900;
          &::before {
            position: absolute;
            content: "";
            left: 0;
            bottom: 0;
            height: 4px;
            width: 100%;
            border-bottom: 4px solid transparent;
            border-left: 4px solid transparent;
            box-sizing: border-box;
            transform: translateX(100%);
          }
          &::after {
            position: absolute;
            content: "";
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            border-top: 4px solid transparent;
            border-right: 4px solid transparent;
            box-sizing: border-box;
            transform: translateX(-100%);
          }
          &:hover {
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
          }
          &:hover::before {
            border-color: #262626;
            height: 100%;
            transform: translateX(0);
            transition: 0.3s transform linear, 0.3s height linear 0.3s;
          }
          &:hover::after {
            border-color: #262626;
            height: 100%;
            transform: translateX(0);
            transition: 0.3s transform linear, 0.3s height linear 0.5s;
          }
        }
      }
    }
  }
  .result {
    position: absolute;
    width: 400px;
    height: 200px;
    background-color: white;
    margin-left: 400px;
    margin-top: 100px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    align-items: center;
    text-align: center;
    .reset {
      position: absolute;
      width: 50px;
      height: 50px;
      top: 10px;
    }
    img {
      margin-top: -20px;
      width: 100px;
      height: 100px;
    }
    span {
      font-size: 48px;
      color: red;
      line-height: 200px;
    }
  }
}
.footer {
  margin-top: 80px;
  width: 1650px;
  height: 50px;
  text-align: center;
  align-items: center;
  p {
    margin: 0;
    color: #6c757d;
    &:nth-child(1) {
      font-size: 16px;
    }
    &:nth-child(2) {
      font-size: 14px;
    }
  }
}
</style>
