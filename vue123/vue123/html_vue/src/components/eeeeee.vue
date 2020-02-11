<style scoped>
  h2 {
    text-align: center;
    padding: 30px;
    font-size: 18px;
  }

  #chart_example {
    width: 800px;
    height: 500px;
    margin: 0 auto;
  }
</style>
<template>
  <div>
    <h2>成绩分布</h2>
    <div id="chart_example">
    </div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    data() {
      d: [];
      return {}
    },
    mounted() {
      let myChart = echarts.init(document.getElementById('chart_example'));
      let option = {
        color: ['#ff9c61'],
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: [
          {
            type: 'category',
            data: ['1', '2'],
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
            name: '成绩',
            type: 'bar',
            barWidth: '60%',
            data: [33, 22]
          }
        ]
      };
      myChart.setOption(option);
      //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
      window.addEventListener('resize', function () {
        myChart.resize()
      });
    },
    methods: {

    },
    watch: {},
    created() {

      this.$axios.post('/api/query',
        {
          // 'sno': localStorage.getItem('User')
          'sno': "100000"
        }
      )
        .then((response) => {
            if (response.data.errno === 'ok') {
              this.d = []
              let da = response.data.data
              print(da)
            } else {
              this.$message.error({
                message: '获取失败',
                showClose: true,
                type: 'error'
              })
            }
          },
          (response) => {
            this.$message.error({
              message: '获取失败',
              showClose: true,
              type: 'error'
            })
          }
        )
    }
  }
</script>
