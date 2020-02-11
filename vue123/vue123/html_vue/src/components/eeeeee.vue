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
      return {
        da: {}
      }
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
            data: this.da.cname,
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
            data: this.da.grade
          }
        ]
      };
      myChart.setOption(option);
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
          'sno': localStorage.getItem('User')
        }
      )
        .then((response) => {
            if (response.data.errno === 'ok') {
              this.da = response.data.data
              console.log(this.da.grade)
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
