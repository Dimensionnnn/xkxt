<template>
  <div>
     <p style="text-align: center; margin: 0 0 20px">选课表</p>
      <div style="text-align: center">
        <el-transfer
          style="text-align: left; display: inline-block"
          v-model="value"
          filterable
          filter-placeholder="请输入课号"
          :titles="['已选课程', '可选课程']"
          :button-texts="['选课', '取消选课']"
          @change="handleChange"
          :format="{
            noChecked: '${total}',
            hasChecked: '${checked}/${total}'
          }"
          :data="d">
          <el-tooltip class="item" open-delay="400" effect="light" v-bind:content="option.label" placement="top" slot-scope="{ option }">
            <span >{{ option.cno }} {{ option.cname }} {{ option.credit }} {{ option.cdept }} {{ option.tname }}</span>
          </el-tooltip>
        </el-transfer>
      </div>
      <el-button @click="optionsubmit()()">提交选课</el-button>
      </div>
</template>
<style>
  .transfer-footer {
    margin-left: 20px;
    padding: 6px 5px;
  }
  .el-transfer-panel {
    width:300px;
  }
</style>

<script>
  export default {
    name: 'oooooo',
    data() {
      return {
        d: [],
        value: [],
        len: 0
      }
    },
    created () {
      this.$axios.post('/api/getallcourse',
        {
          'sno': localStorage.getItem('User')
        }
      )
        .then((response) => {
          if (response.data.errno === 'ok') {
            this.d = []
            let da = response.data.data
            this.len = da.length
            for(var i = 0;i<da.length;i++){
              this.d.push({
                key: i,
                label: da[i][0]+' '+da[i][1]+' '+da[i][2]+' '+da[i][3]+' '+da[i][4],
                cno: da[i][0],
                cname: da[i][1],
                credit: da[i][2],
                cdept: da[i][3],
                tname: da[i][4]
              })
            }
            this.value = response.data.cho
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
      handleChange(value, direction, movedKeys) {
        this.$axios.post('/api/optioncourse',
          {
            'direction': direction,
            'keys': movedKeys,
            'sno': localStorage.getItem('User')
          }
        )
          .then((response) => {
            if (response.data.errno === 'ok') {
              this.$message({
                showClose: true,
                message: '成功',
                type: 'success'
              })
            } else {
              this.$message.error({
                message: '失败',
                showClose: true,
                type: 'error'
              })
            }
          },
          (response) => {
            this.$message.error({
              message: '失败',
              showClose: true,
              type: 'error'
            })
          }
          )
      }
    }
  }
</script>
