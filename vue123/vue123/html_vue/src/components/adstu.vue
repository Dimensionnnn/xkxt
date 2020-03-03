<template>
  <div>
    <el-button type="text" @click="dialogFormVisible = true">新增学生</el-button>
    <el-dialog title="学生信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="学生学号" :label-width="formLabelWidth">
          <el-input v-model="form.sno" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="form.sname" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-input v-model="form.sex" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="年龄" :label-width="formLabelWidth">
          <el-input v-model.number="form.age" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="学院" :label-width="formLabelWidth">
          <el-input v-model="form.sdept" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="sendData">确 定</el-button>
      </div>
    </el-dialog>

    <el-table :data="d" style="width: 100%" @row-click="call">
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
          sno: '',
          sname: '',
          sex: '',
          age: '',
          sdept: ''
        },
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
          }
        )
    },
    methods: {
      sendData() {
        this.dialogFormVisible = false
        this.$axios.post('/api/adstu/in',
          {
            'sno': this.form.sno,
            'sname': this.form.sname,
            'sex': this.form.sex,
            'age': this.form.age,
            'sdept': this.form.sdept
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
        this.$axios.post('/api/adstu/de', {"sno": row.sno})
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
