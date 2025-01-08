<template>
  <div class="price-predict">
    <div class="header">
      <span>首页 / </span>
      <span>房价评估预测</span>
    </div>
    <div class="body">
      <img src="@/assets/images/predict.png" alt="" />
      <h1>房价预测</h1>
      <span class="title">杭州二手房房价预测</span>
      <span class="subtitle"
        >-提供房价预测服务,作为参考依据,让更多人对房价有大致的了解</span
      >
      <div class="gopredict">
        <button @click="$router.push('/index/predict/input')" class="btn">
          Go Predict
        </button>
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
<script></script>
<style lang="less" scoped>
.price-predict {
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
.body {
  position: relative;
  width: 1650px;
  height: 500px;
  background-color: #e9ecef;
  margin-top: 40px;
  border-radius: 10px;
  text-align: center;
  align-items: center;
  img {
    margin-top: 40px;
  }
  h1 {
    position: absolute;
    top: 120px;
    left: 50%;
    transform: translate(-50%);
    font-size: 50px;
    font-style: italic;
    color: gray;
  }
  .title {
    margin-top: 20px;
    display: block;
    font-size: 36px;
  }
  .subtitle {
    display: block;
    font-size: 18px;
  }
  .gopredict {
    position: relative;
    width: 200px;
    height: 100px;
    background-color: transparent;
    margin-top: 20px;
    margin-left: 50%;
    transform: translate(-50%);
    .btn {
      --color1: #007bff;
      --color2: #007bff;
      perspective: 1000px;
      padding: 1em 1em;
      background: linear-gradient(var(--color1), var(--color2));
      border: none;
      outline: none;
      font-size: 20px;
      text-transform: uppercase;
      letter-spacing: 4px;
      color: #fff;
      text-shadow: 0 10px 10px #000;
      cursor: pointer;
      transform: rotateX(70deg) rotateZ(30deg);
      transform-style: preserve-3d;
      transition: transform 0.5s;
    }

    .btn::before {
      content: "";
      width: 100%;
      height: 15px;
      background-color: var(--color2);
      position: absolute;
      bottom: 0;
      right: 0;
      transform: rotateX(90deg);
      transform-origin: bottom;
    }

    .btn::after {
      content: "";
      width: 15px;
      height: 100%;
      background-color: var(--color1);
      position: absolute;
      top: 0;
      right: 0;
      transform: rotateY(-90deg);
      transform-origin: right;
    }

    .btn:hover {
      transform: rotateX(30deg) rotateZ(0);
    }
  }
}
.footer {
  width: 1650px;
  height: 80px;
  margin-top: 200px;
  align-items: center;
  text-align: center;
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
