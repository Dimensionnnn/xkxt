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
        da: {
          cname:[],
          grade:[]
        }
      }
    },
    mounted() {

      let myChart = echarts.init(document.getElementById('chart_example'))

      window.addEventListener('resize', function () {
        myChart.resize()
      })
      this.$axios.post('/api/query',
        {
          'sno': localStorage.getItem('User')
        }
      )
        .then((response) => {
            if (response.data.errno === 'ok') {
              this.da = response.data.data
              myChart.setOption({
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
                },
                axisLabel: {
                  interval: 0
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
              })
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
