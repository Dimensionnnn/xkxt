<template>
  <el-table :data="d" style="width: 100%" fit="true">
    <el-table-column
      label="学号"
      prop="sno">
    </el-table-column>
    <el-table-column
      label="姓名"
      prop="sname">
    </el-table-column>
    <el-table-column
      label="性别"
      prop="sex">
    </el-table-column>
    <el-table-column
      label="年龄"
      prop="age">
    </el-table-column>
    <el-table-column
      label="学院"
      prop="sdept">
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>


</template>

<script>
  export default {
    data() {
      return {
        data: {},
        d: [],
        search: '',
        formLabelWidth: '120px'
      }
    },
    created() {
      this.$axios.post('/api/adstu')
        .then((response) => {
            if (response.data.errno === 'ok') {
              this.data = response.data.data
              console.log(this.data)
              for (var i = 0; i < this.data.length; i++) {
                this.d.push({
                  sno: this.data[i][0],
                  sname: this.data[i][1],
                  sex: this.data[i][2],
                  age: this.data[i][3],
                  sdept: this.data[i][4]
                })
              }
              console.log(this.d)
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
      handleDelete(index, row) {
        this.$axios.post('/api/adstu_de',
          (index, row))
          .then((response) => {
            if (response.data.errno == 'ok')
              this.$message({
                type: 'success',
                message: '删除成功!'
              })
            else {
              this.$message.error('删除失败')
            }
          })
        console.log(index, row);
      },

    },
  }
</script>
