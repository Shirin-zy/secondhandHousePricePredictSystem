<template>
  <div class="city-price">
    <div class="header"><span>首页 / </span><span>区域房价概览</span></div>
    <div class="content">
      <div class="photo" id="priceofciry"></div>
      <div class="photo" id="houseage"></div>
      <div class="photo" id="housearea"></div>
      <div class="photo" id="houseprice"></div>
    </div>
  </div>
</template>
<script>
import * as echarts from 'echarts'
export default {
  data () {
    return {
    }
  },
  mounted () {
    this.priceofciry = echarts.init(document.getElementById('priceofciry'))
    this.houseage = echarts.init(document.getElementById('houseage'))
    this.housearea = echarts.init(document.getElementById('housearea'))
    this.houseprice = echarts.init(document.getElementById('houseprice'))
    this.priceofciry.setOption({
      title: {
        text: '城市房价概览'
      },
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: ['平均房价', '最高房价', '最低房价']
      },
      xAxis: {
        type: 'category',
        data: ['滨江', '富阳', '拱墅', '临安', '临平', '钱塘', '上城', '萧山', '西湖', '余杭']
      },
      yAxis: { type: 'value' },
      series: [
        {
          nmae: '平均房价',
          data: [46915, 24173, 45123, 20669, 24028, 26558, 45542, 32588, 57627, 37775],
          type: 'line'
        }, {
          nmae: '最高房价',
          data: [13652, 10549, 14143, 4348, 8006, 9150, 12298, 8558, 14890, 12370],
          type: 'line'
        }, {
          nmae: '最低房价',
          data: [128968, 101833, 119959, 76396, 97535, 76669, 124965, 112409, 119980, 129760],
          type: 'line'
        }
      ]
    })
    this.houseage.setOption({
      title: {
        text: '房屋年龄结构'
      },
      tooltip: {
        trigger: 'item'
      },
      legend: {
        top: '5%',
        left: 'center'
      },
      series: [
        {
          name: '房屋数',
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
            { value: 14360, name: '满5年' },
            { value: 10080, name: '满2年' },
            { value: 5560, name: '不满2年' }
          ]
        }
      ]
    })
    this.housearea.setOption({
      title: {
        text: '房屋面积分布'
      },
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
          type: 'category',
          data: ['小于30平方', '30-60', '30-90', '90-120', '120-150', '150-180', '180-210', '210-240', '240-270', '270-300', '大于300平方'],
          axisTick: {
            alignWithLabel: true
          }
        }
      ],
      yAxis: [
        {
          type: 'value'
        }
      ],
      series: [
        {
          name: '房屋数',
          type: 'bar',
          barWidth: '60%',
          data: [20, 1440, 10670, 5420, 7690, 2100, 970, 690, 430, 300, 280]
        }
      ]
    })
    this.houseprice.setOption({
      title: {
        text: '房屋价格区间分布'
      },
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
            { value: 2630, name: '200w以下' },
            { value: 14460, name: '200-400w' },
            { value: 8010, name: '400-600w' },
            { value: 2160, name: '600-800w' },
            { value: 960, name: '800-1000w' },
            { value: 580, name: '1000-1200w' },
            { value: 490, name: '1200-1400w' },
            { value: 310, name: '1400-1600w' },
            { value: 120, name: '1600-1800w' },
            { value: 90, name: '1800-2000w' },
            { value: 190, name: '2000w以上' }
          ]
        }
      ]
    })
  }
}
</script>
<style lang="less" scoped>
.city-price {
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
  margin-top: 20px;
  width: 1650px;
  height: 800px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-content: space-between;
  .photo {
    width: 810px;    height: 385px;
    background-color: #e9ecef;
  }
}
</style>
