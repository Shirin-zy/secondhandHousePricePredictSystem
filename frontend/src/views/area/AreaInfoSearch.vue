<template>
  <div class="area-info-search">
    <div class="header">
      <span>首页 / </span
      ><span @click="$router.push('/index/areaprice')">小区房价数据查询 / </span
      ><span>{{ getId }}</span>
    </div>
    <div class="content">
      <h2>小区信息</h2>
      <div class="body">
        <div class="header-title">基本信息:</div>
        <div class="info">
          <hr />
          <div>
            <div>
              <span>小区名:</span><span>{{ this.info.name }}</span>
            </div>
            <div>
              <span>参考均价:</span
              ><span>{{ this.info.price_average }}元/平方米</span>
            </div>
          </div>
          <hr />
          <div>
            <div>
              <span>房屋年限:</span><span>{{ this.info.age }}</span>
            </div>
            <div><span>建筑类型:</span><span>板楼</span></div>
          </div>
          <hr />
          <div>
            <div><span>物业公司:</span><span>暂无信息</span></div>
            <div>
              <span>平均价格:</span
              ><span>{{ this.info.totalprice_average }}万元</span>
            </div>
          </div>
          <hr />
          <div>
            <div>
              <span>累计成交数:</span><span>{{ this.info.count }}套</span>
            </div>
            <div>
              <span>行政区:</span><span>{{ this.info.city }}</span>
            </div>
          </div>
          <hr />
          <div>
            <div>
              <span>所在街道:</span><span>{{ this.info.address }}</span>
            </div>
            <div>
              <span>平均关注度:</span
              ><span>{{ this.info.attention_average }}</span>
            </div>
          </div>
          <hr />
          <div>
            <div><span>建筑结构:</span><span>钢混结构</span></div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <h2>相关数据</h2>
      <div class="footer-content">
        <div class="photo">
          <div class="photo-title">房屋面积分布：</div>
          <div class="picture" id="areasection"></div>
        </div>
        <div class="photo">
          <div class="photo-title">房屋装修情况：</div>
          <div class="picture" id="decorate"></div>
        </div>
        <div class="photo">
          <div class="photo-title">房屋楼层信息：</div>
          <div class="picture" id="floor"></div>
        </div>
        <div class="photo">
          <div class="photo-title">房屋单价分布:</div>
          <div class="picture" id="pricesection"></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as echarts from 'echarts'
import {
  getAreaInfo,
  getAreaSection,
  getDecorate,
  getFloor,
  getPriceSection
} from '@/api/areainfoseaarch'
export default {
  data () {
    return {
      info: {},
      // 房屋面积分布数据
      count1: null,
      count2: null,
      count3: null,
      count4: null,
      count5: null,
      label1: '',
      label2: '',
      label3: '',
      label4: '',
      label5: '',
      // 房屋装修情况数据
      count6: 0,
      count7: 0,
      count8: 0,
      label6: '',
      label7: '',
      label8: '',
      // 装修楼层统计数据
      count9: 0,
      count10: 0,
      count11: 0,
      label9: '',
      label10: '',
      label11: '',
      // 房屋单价分布信息
      count12: null,
      count13: null,
      count14: null,
      count15: null,
      count16: null,
      label12: '',
      label13: '',
      label14: '',
      label15: '',
      label16: ''
    }
  },
  computed: {
    label () {
      return this.areasection.label
    },
    count () {
      return this.areasection.count
    },
    getId () {
      return this.$route.params.id
    }
  },
  methods: {
    // 绘制房屋面积分布的条形图
    drawAeraSection () {
      this.areasection = echarts.init(document.getElementById('areasection'))
      this.areasection.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            name: '面积(m²)',
            type: 'category',
            data: [
              this.label1,
              this.label2,
              this.label3,
              this.label4,
              this.label5
            ],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            name: '数量(套)',
            type: 'value'
          }
        ],
        series: [
          {
            name: '房屋数(套)',
            type: 'bar',
            barWidth: '50%',
            data: [
              this.count1,
              this.count2,
              this.count3,
              this.count4,
              this.count5
            ]
          }
        ]
      })
    },
    // 绘制房屋装修情况环形图
    drawDecorate () {
      this.decorate = echarts.init(document.getElementById('decorate'))
      this.decorate.setOption({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: '数量(套)',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 24,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: this.count6, name: this.label6 },
              { value: this.count7, name: this.label7 },
              { value: this.count8, name: this.label8 }
            ]
          }
        ]
      })
    },
    // 绘制楼层数据玫瑰图
    drawFloor () {
      this.floor = echarts.init(document.getElementById('floor'))
      this.floor.setOption({
        title: {},
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          top: 'bottom'
        },
        series: [
          {
            name: '占比',
            type: 'pie',
            radius: [50, 150],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 8
            },
            data: [
              { value: this.count9, name: this.label9 },
              { value: this.count10, name: this.label10 },
              { value: this.count11, name: this.label11 }
            ]
          }
        ]
      })
    },
    // 绘制房屋单价分布的折线图
    drawPriceSection () {
      this.priceSection = echarts.init(document.getElementById('pricesection'))
      this.priceSection.setOption({
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          name: '单价(元/m²)',
          type: 'category',
          data: [
            this.label12,
            this.label13,
            this.label14,
            this.label15,
            this.label16
          ],
          axisLabel: {
            rotate: 15
          }
        },
        yAxis: { type: 'value', name: '房屋数(套)' },
        series: [
          {
            nmae: '平均房价',
            data: [
              this.count12,
              this.count13,
              this.count14,
              this.count15,
              this.count16
            ],
            type: 'line'
          }
        ]
      })
    }
  },
  async created () {
    const data = await getAreaInfo(this.getId)
    this.info = data.data[0]
    // 获取房屋面积数据以及绘图
    const data2 = await getAreaSection(this.getId)
    this.count1 = data2.data[0].count[0]
    this.count2 = data2.data[0].count[1]
    this.count3 = data2.data[0].count[2]
    this.count4 = data2.data[0].count[3]
    this.count5 = data2.data[0].count[4]
    this.label1 = data2.data[0].label[0]
    this.label2 = data2.data[0].label[1]
    this.label3 = data2.data[0].label[2]
    this.label4 = data2.data[0].label[3]
    this.label5 = data2.data[0].label[4]
    this.drawAeraSection()
    // 获取房屋装修数据以及绘图
    const data3 = await getDecorate(this.getId)
    this.count6 = data3.data[0].count[0]
    this.count7 = data3.data[0].count[1]
    this.count8 = data3.data[0].count[2]
    this.label6 = data3.data[0].label[0]
    this.label7 = data3.data[0].label[1]
    this.label8 = data3.data[0].label[2]
    this.drawDecorate()
    // 获取楼层数据并绘图
    const data4 = await getFloor(this.getId)
    this.count9 = data4.data[0].count[0]
    this.count10 = data4.data[0].count[1]
    this.count11 = data4.data[0].count[2]
    this.label9 = data4.data[0].label[0]
    this.label10 = data4.data[0].label[1]
    this.label11 = data4.data[0].label[2]
    this.drawFloor()
    // 获取单价信息并绘制
    const data5 = await getPriceSection(this.getId)
    this.count12 = data5.data[0].count[0]
    this.count13 = data5.data[0].count[1]
    this.count14 = data5.data[0].count[2]
    this.count15 = data5.data[0].count[3]
    this.count16 = data5.data[0].count[4]
    this.label12 = data5.data[0].label[0]
    this.label13 = data5.data[0].label[1]
    this.label14 = data5.data[0].label[2]
    this.label15 = data5.data[0].label[3]
    this.label16 = data5.data[0].label[4]
    this.drawPriceSection()
  },
  mounted () {}
}
</script>
<style lang="less" scoped>
.area-info-search {
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
.content {
  margin-top: 40px;
  width: 1650px;
  height: 600px;
  .body {
    width: 1650px;
    height: 500px;
    background-color: #fff;
    border-radius: 10px;
    border: 1px solid rgba(0, 0, 0, 0.125);
    .header-title {
      width: 1650px;
      height: 50px;
      background-color: rgba(0, 0, 0, 0.03);
      border-radius: 10px 10px 0 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.125);
      line-height: 50px;
      font-size: 18px;
      padding: 0 20px;
    }
    .info {
      hr {
        width: 1600px;
        margin-left: 25px;
      }
      div {
        width: 1600px;
        height: 30px;
        margin-left: 25px;
        display: flex;
        justify-content: space-between;
        div {
          width: 500px;
          height: 30px;
          display: flex;
          justify-content: space-between;
        }
      }
    }
  }
}
.footer {
  .footer-content {
    width: 1650px;
    height: 1000px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-content: space-between;
    .photo {
      width: 800px;
      height: 485px;
      background-color: #e9ecef;
      border-radius: 10px;
      border: 1px solid rgba(0, 0, 0, 0.125);
      .photo-title {
        width: 100%;
        height: 50px;
        background-color: #f7f7f7;
        border-radius: 10px 10px 0 0;
        border-bottom: 1px solid rgba(0, 0, 0, 0.125);
        line-height: 50px;
        padding-left: 20px;
        font-size: 18px;
      }
      .picture {
        width: 100%;
        height: 433px;
        background-color: #fff;
        border-radius: 0 0 10px 10px;
      }
    }
  }
}
</style>
