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
            data: js.cname,
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
            data: js.grade
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
      getData() {
        this.$axios.post('api/query', {
          'sno': localStorage.getItem('User')
        }).then((response) => {
          let js = response.data.data
          print(js)
          console.log(response.data)
        })
      }
    },
    watch: {},
    created() {

    }
  }
</script>
