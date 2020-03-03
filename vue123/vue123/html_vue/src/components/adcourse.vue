<template>
  <div>
    <el-button type="text" @click="dialogFormVisible = true">新增课程</el-button>
    <el-dialog title="课程信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="课程号" :label-width="formLabelWidth">
          <el-input v-model="form.cno" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="课程名称" :label-width="formLabelWidth">
          <el-input v-model="form.cname" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="学分" :label-width="formLabelWidth">
          <el-input v-model.number="form.credit" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="院系" :label-width="formLabelWidth">
          <el-input v-model="form.cdept" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="任课教师" :label-width="formLabelWidth">
          <el-input v-model="form.tname" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="sendData">确 定</el-button>
      </div>
    </el-dialog>

    <el-table :data="d" style="width: 100%" @row-click="call">
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
      <el-table-column label="操作">
        <template>
          <el-button
            size="mini"
            type="danger"
          >删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        data: {},
        d: [],
        search: '',
        dialogTableVisible: false,
        dialogFormVisible: false,
        form: {
          cno: '',
          cname: '',
          credit: '',
          cdept: '',
          tname: ''
        },
        formLabelWidth: '120px'
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
              this.$message.error({
                message: '获取失败',
                showClose: true,
                type: 'error'
              })
            }
          },
        )
    },
    methods: {
      sendData() {
        this.dialogFormVisible = false
        this.$axios.post('/api/adcourse/in',
          {
            'cno': this.form.cno,
            'cname': this.form.cname,
            'credit': this.form.credit,
            'cdept': this.form.cdept,
            'tname': this.form.tname
          })
          .then((response) => {
            if (response.data.errno == 'ok')
              this.$message({
                type: 'success',
                message: '添加成功!'
              })
            else {
              this.$message.error('添加失败')
            }
          })
        console.log(this.form)

      },
      call(row, column, event) {
        this.$axios.post('/api/adcourse/de', {"cno": row.cno})
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
        console.log(row)
      },
    },
  }
</script>
