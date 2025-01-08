<template>
  <div>
    <!-- 导航栏 -->
    <div class="fixed-top">
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container">
          <a class="navbar-brand" href="#">
            <img src="@/assets/images/logo.png" alt="" />
            <h1>房知道</h1>
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" @click="$router.push('/index/city')">服务</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#about">关于</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" @click="$router.push('/login')">登录</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <!-- 轮播图 -->
    <div>
      <div id="carouselExampleIndicators" class="carousel slide">
        <div class="carousel-indicators">
          <button
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide-to="0"
            class="active"
            aria-current="true"
            aria-label="Slide 1"
          ></button>
          <button
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide-to="1"
            aria-label="Slide 2"
          ></button>
          <button
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide-to="2"
            aria-label="Slide 3"
          ></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="city">
              <div>滨江</div>
              <div>富阳</div>
              <div>拱墅</div>
              <div>临安</div>
              <div>临平</div>
              <div>钱塘</div>
              <div>上城</div>
              <div>萧山</div>
              <div>西湖</div>
              <div>余杭</div>
            </div>
          </div>
          <div class="carousel-item">
            <span>预测房价信息</span>
            <span>为您提供更多参考建议</span>
          </div>
          <div class="carousel-item">
            <span>分析房屋数据</span>
            <span>祝您掌握二手房市场</span>
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
    <!-- 我们的优势 -->
    <div class="container project">
      <a name="serve" href=""></a>
      <div>
        <span class="title">
          <span>Key Feature / </span>
          <span>我们的优势</span>
        </span>
        <span class="subtitle">了解房价信息，助您掌握二手房市场</span>
      </div>
      <div class="content">
        <!-- 使用格栅网布局，当视口小于768时一行排一个，大于768时一行排两个，大于992时一行排四个 -->
        <div class="row">
          <div class="col-lg-3 col-md-6">
            <a href="">
              <h4>小区信息</h4>
              <span>获取小区房屋数据，平均房价</span>
              <div></div>
            </a>
          </div>
          <div class="col-lg-3 col-md-6">
            <a href="">
              <h4>房价预测</h4>
              <span>预测房价信息，提供参考建议</span>
              <div></div>
            </a>
          </div>
          <div class="col-lg-3 col-md-6">
            <a href="">
              <h4>历史数据</h4>
              <span>真实历史数据，了解房屋信息</span>
              <div></div>
            </a>
          </div>
          <div class="col-lg-3 col-md-6">
            <a href="">
              <h4>数据分析</h4>
              <span>分析房屋数据，掌握市场行情</span>
              <div></div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <a name="about" href=""></a>
      <div class="container">
        <div class="left">
          <h2>房知道</h2>
          <p>房知道致力于帮助消费者跟清晰的了解房价市场</p>
          <a href="">下载APP</a>
        </div>
        <div class="right">
          <dl>
            <dt>关于房知道</dt>
            <dd>关于</dd>
            <dd>客户服务</dd>
            <dd>帮助</dd>
          </dl>
          <dl>
            <dt>新手指南</dt>
            <dd>如何注册</dd>
            <dd>使用攻略</dd>
            <dd>进阶技巧</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</template>
<script></script>
<style lang="less" scoped>
.container {
  margin: auto;
}
.bg-body-tertiary {
  .navbar-brand {
    display: flex;
    img {
      width: 50px;
      height: 50px;
    }
    h1 {
      color: #fff;
      font-style: italic;
    }
  }
  background-color: transparent !important;
  .navbar-collapse {
    flex-grow: 0;
    .nav-link {
      color: hsla(0, 0%, 100%, 0.65);
      font-size: 16px;
      :hover {
        color: #f2b535 !important;
      }
    }
    .active {
      color: #f2b535;
    }
  }
}
.carousel {
  // 媒体查询当视口小于768px时高度未250，类推
  @media (max-width: 768px) {
    .carousel-item {
      height: 250px;
    }
    .carousel-item:nth-child(1) {
      background-image: url("@/assets/uploads/banner_2.jpg");
    }
    .carousel-item:nth-child(2) {
      background-image: url("@/assets/uploads/banner_3.jpg");
      span {
        color: transparent;
      }
    }
    .carousel-item:nth-child(3) {
      background-image: url("@/assets/uploads/banner_4.jpg");
      span {
        color: transparent;
      }
    }
  }
  @media (min-width: 768px) {
    .carousel-item {
      height: 400px;
    }
    .carousel-item:nth-child(1) {
      background-image: url("@/assets/uploads/banner_2.jpg");
    }
    .carousel-item:nth-child(2) {
      background-image: url("@/assets/uploads/banner_3.jpg");
      span {
        color: transparent;
      }
    }
    .carousel-item:nth-child(3) {
      background-image: url("@/assets/uploads/banner_4.jpg");
      span {
        color: transparent;
      }
    }
  }
  @media (min-width: 992px) {
    .carousel-item {
      height: 500px;
    }
    .carousel-item:nth-child(2) {
      background-image: url("@/assets/uploads/banner_3.jpg");
      span {
        color: hsla(0, 0%, 100%, 0.9);
        position: absolute;
      }
      span:nth-child(1) {
        text-align: center;
        width: 600px;
        font-size: 40px;
        top: 40%;
        right: -800px;
        animation: moveleft 0.3s 0.5s linear forwards;
      }
      @keyframes moveleft {
        100% {
          right: 25%;
        }
      }
      span:nth-child(2) {
        font-size: 40px;
        bottom: 15%;
        left: -250px;
        animation: moveright 0.3s 0.5s linear forwards;
      }
      @keyframes moveright {
        100% {
          left: 30%;
        }
      }
    }
    .carousel-item:nth-child(3) {
      background-image: url("@/assets/uploads/banner_4.jpg");
      span {
        color: hsla(0, 0%, 100%, 0.9);

        position: absolute;
        left: 50%;
        transform: translateX(-50%);
      }
      span:nth-child(1) {
        font-size: 60px;
        top: -20%;
        animation: movedown 0.3s 0.5s linear forwards;
      }
      @keyframes movedown {
        100% {
          top: 35%;
        }
      }
      span:nth-child(2) {
        font-size: 40px;
        bottom: -20%;
        animation: moveup 0.3s 0.5s linear forwards;
      }
      @keyframes moveup {
        100% {
          bottom: 30%;
        }
      }
    }
  }
  .carousel-item {
    background-size: cover;
    background-position: center center;
  }
  .carousel-item:nth-child(1) {
    background-image: url("@/assets/uploads/banner_1.jpg");
    position: relative;
    .city {
      position: absolute;
      display: flex;
      flex-wrap: wrap;
      width: 400px;
      height: 80px;
      left: 50%;
      top: 70%;
      transform: translate(-50%, -50%);
      justify-content: space-evenly;
      text-align: center;
      div {
        background-color: #0095ff;
        height: 30px;
        width: 70px;
        border-radius: 10px;
        line-height: 30px;
        color: hsla(0, 0%, 100%, 0.7);
        transition: all 0.3s;
        &:hover {
          transform: translateY(-5px);
        }
      }
    }
  }
}
.project {
  margin-top: 60px;
  text-align: center;
  .title {
    display: block;
    font-family: Segoe UI Light, Microsoft YaHei, Arial, Helvetica, sans-serif;
    font-size: 30px;
    color: #494d55;
  }
  .subtitle {
    font-family: Microsoft YaHei, Arial, Helvetica, sans-serif;
    font-size: 16px;
    color: #919191;
    height: 50px;
    line-height: 50px;
  }
}
.content {
  .row {
    div {
      height: 200px;
      margin-bottom: 20px;
      a {
        position: relative;
        height: 200px;
        display: block;
        text-decoration: none;
        border-radius: 4px;
        transition: all 0.3s;
        overflow: hidden;
        &:hover {
          transform: translateY(-10px);
          box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
          div {
            animation: move 0.5s linear forwards;
          }
        }
        h4 {
          position: absolute;
          bottom: 60px;
          left: 50%;
          transform: translateX(-50%);
          color: white;
        }
        span {
          width: 100%;
          position: absolute;
          bottom: 35px;
          left: 50%;
          transform: translateX(-50%);
          color: white;
        }
        div {
          position: absolute;
          background-color: white;
          opacity: 0.2;
          width: 50px;
          height: 300px;
          top: -50px;
          left: -150px;
          transform: rotate(45deg);
        }
        @keyframes move {
          100% {
            transform: translateX(800px);
          }
        }
      }
      &:nth-child(1) a {
        background-color: #70c3ff;
        background-image: url("@/assets/images/1.png");
        background-repeat: no-repeat;
        background-position: center 20px;
        background-size: 60px;
      }
      &:nth-child(2) a {
        background-color: #fd6a7f;
        background-image: url("@/assets/images/2.png");
        background-repeat: no-repeat;
        background-position: center 20px;
        background-size: 60px;
      }
      &:nth-child(3) a {
        background-color: #7f8ea0;
        background-image: url("@/assets/images/3.png");
        background-repeat: no-repeat;
        background-position: center 20px;
        background-size: 60px;
      }
      &:nth-child(4) a {
        background-color: #89d04f;
        background-image: url("@/assets/images/4.png");
        background-repeat: no-repeat;
        background-position: center 20px;
        background-size: 60px;
      }
    }
  }
}
.footer {
  margin-top: 100px;
  background-color: #26282c;
  width: 100%;
  height: 200px;
  .container {
    display: flex;
    justify-content: space-between;
    div {
      margin-top: 25px;
      width: 200px;
      height: 150px;
    }
    .left {
      h2 {
        color: #fff;
        font-style: italic;
      }
      p {
        color: hsla(0, 0%, 100%, 0.4);
        font-size: 12px;
      }
      a {
        display: block;
        width: 120px;
        height: 36px;
        margin-top: 14px;
        border: solid 1px #fff;
        text-align: center;
        font-family: PingFangSC-Regular;
        font-size: 16px;
        font-weight: normal;
        line-height: 36px;
        color: hsla(0, 0%, 100%, 0.4);
        text-decoration: none;
      }
    }
    .right {
      display: flex;
      justify-content: space-between;
      dt {
        font-family: PingFangSC-Regular;
        font-size: 16px;
        font-weight: normal;
        line-height: 23px;
        color: hsla(0, 0%, 100%, 0.7);
        margin-bottom: 12px;
      }
      dd {
        font-family: PingFangSC-Regular;
        font-size: 14px;
        font-weight: normal;
        line-height: 24px;
        color: hsla(0, 0%, 100%, 0.4);
      }
    }
  }
}
</style>
