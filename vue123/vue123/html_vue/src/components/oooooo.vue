<template>
  <div>
     <p style="text-align: center; margin: 0 0 20px">选课表</p>
      <div style="text-align: center">
        <el-transfer
          style="text-align: left; display: inline-block"
          v-model="value"
          :titles="['已选课程', '可选课程']"
          :button-texts="['选课', '取消选课']"
          :format="{
            noChecked: '${total}',
            hasChecked: '${checked}/${total}'
          }"
          :data="d">
        </el-transfer>
      </div>
      <el-button @click="get()">提交选课</el-button>
      </div>
</template>
<style>
  .transfer-footer {
    margin-left: 20px;
    padding: 6px 5px;
  }
</style>

<script>
  export default {
    name: 'oooooo',
    data() {
      return {
        d: [],
        value: []
      }
    },
    created () {
      this.$axios.post('/api/option',
        {
          'logn': '11'
        }
      )
        .then((response) => {
          if (response.data.errno === 'ok') {
            this.d = []
            let da = response.data.data
            for(var i = 0;i<da.length;i++){
              this.d.push({
                label: da[i][0]+' '+da[i][1]+' '+da[i][2]+' '+da[i][3]+' '+da[i][4],
                key: i
              })
            }
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
    },
    methods: {
      get () {
        this.$axios.post('/api/option',
          {
            'logn': '11'
          }
        )
          .then((response) => {
            if (response.data.errno === 'ok') {
              for(var i = 0;i<response.data.data.length;i++){
                this.d.push({label: response.data.data[i]}
                )
              }
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
  }
</script>
