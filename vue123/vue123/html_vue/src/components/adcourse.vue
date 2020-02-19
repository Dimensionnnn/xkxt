<template>
  <el-table :data="d" style="width: 100%" fit="true">
    <el-table-column
      label="课号"
      prop="cno">
    </el-table-column>
    <el-table-column
      label="课程名称"
      prop="cname">
    </el-table-column>
    <el-table-column
      label="学分"
      prop="credit">
    </el-table-column>
    <el-table-column
      label="学院"
      prop="cdept">
    </el-table-column>
    <el-table-column
      label="任课教师"
      prop="tname">
    </el-table-column>
    <template slot-scope="scope">
      <el-button
        size="mini"
        @click="handleEdit(scope.$index, scope.row)">Edit
      </el-button>
      <el-button
        size="mini"
        type="danger"
        @click="handleDelete(scope.$index, scope.row)">Delete
      </el-button>
    </template>
  </el-table>
</template>

<script>
  export default {
    data() {
      return {
        data: {},
        d: [],
        search: ''
      }
    },
    created() {
      this.$axios.post('/api/adcourse')
        .then((response) => {
            if (response.data.errno === 'ok') {
              this.data = response.data.data
              console.log(this.data)
              for (var i = 0; i < this.data.length; i++) {
                this.d.push({
                  cno: this.data[i][0],
                  cname: this.data[i][1],
                  credit: this.data[i][2],
                  cdept: this.data[i][3],
                  tname: this.data[i][4]
                })
              }
              console.log(this.d)
            } else {
              console.log(response.data.data)
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
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    },
  }
</script>
