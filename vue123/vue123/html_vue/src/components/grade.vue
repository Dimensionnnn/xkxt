<template>
  <div>

    <el-select v-model="value" placeholder="请选择" @change="getgrade">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <!--    <el-button type="text" @click="dialogFormVisible = true">新增选课</el-button>-->
    <!--    <el-dialog title="选课信息" :visible.sync="dialogFormVisible">-->
    <!--      <el-form :model="form">-->
    <!--        <el-form-item label="学生学号" :label-width="formLabelWidth">-->
    <!--          <el-input v-model="form.sno" autocomplete="off"></el-input>-->
    <!--        </el-form-item>-->
    <!--        <el-form-item label="课号" :label-width="formLabelWidth">-->
    <!--          <el-input v-model="form.cno" autocomplete="off"></el-input>-->
    <!--        </el-form-item>-->
    <!--        <el-form-item label="成绩" :label-width="formLabelWidth">-->
    <!--          <el-input v-model.number="form.grade" autocomplete="off"></el-input>-->
    <!--        </el-form-item>-->

    <!--      </el-form>-->
    <!--      <div slot="footer" class="dialog-footer">-->
    <!--        <el-button @click="dialogFormVisible = false">取 消</el-button>-->
    <!--        <el-button type="primary" @click="sendData">确 定</el-button>-->
    <!--      </div>-->
    <!--    </el-dialog>-->

    <el-table :data="d" style="width: 100%" @row-click="call">
      <el-table-column label="更改">
        <template>
          <el-button type="primary" icon="el-icon-edit" @click="open"></el-button>
        </template>
      </el-table-column>
      <el-table-column
        label="学号"
        prop="sno">
      </el-table-column>
      <el-table-column
        label="成绩"
        prop="grade">
      </el-table-column>
      <el-table-column label="删除">
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
        options: [{
          value: '',
          label: '',
          cno: '',
          cname: ''
        }],
        dialogTableVisible: false,
        dialogFormVisible: false,
        form: {
          sno: '',
          cno: '',
          grade: '',
        },
        formLabelWidth: '120px',
        d: [],
        len: 0,
        value: '',
        loading: true,
        x: [],
        grade: 0
      }
    },
    created() {
      this.$axios.post('/api/grade/course')
        .then((response) => {
          if (response.data.errno === 'ok') {
            let da = response.data.data
            this.len = da.length
            for (var i = 0; i < da.length; i++) {
              this.options.push({
                value: da[i][0],
                label: da[i][1],
              })
            }
            this.loading = false
          } else {
            this.$message.error({
              message: '获取失败',
              showClose: true,
              type: 'error'
            })
          }
        })
    },
    methods: {

      open() {
        this.$prompt('输入成绩', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).then(({value}) => {
          this.$axios.post("/api/grade/update",
            {
              "sno": this.x.sno,
              "cno": this.value,
              "grade": value
            })
            .then((response) => {
                if (response.data.errno == 'ok')
                  this.$message({
                    type: 'success',
                    message: '更新成功!'
                  })
                else {
                  this.$message.error('更新失败')
                }
              }
            )
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });
        });
      },
      getgrade() {
        this.$axios.post('/api//grade', {
          'cno': this.value
        })
          .then((response) => {
            console.log(this.value)
            if (response.data.errno === 'ok') {
              let da = response.data.data
              this.d.splice(0, this.len)
              this.len = da.length
              for (var i = 0; i < da.length; i++) {
                this.d.push({
                  sno: da[i][0],
                  grade: da[i][1],
                })
              }
            } else {
              this.$message.error({
                message: '获取失败',
                showClose: true,
                type: 'error'
              })
            }

          })
      },
      call(row, column, event) {
        if (column.label == '删除') {
          this.$axios.post('/api/grade/de', {
            "sno": row.sno,
            "cno": this.value
          })
            .then((response) => {
              console.log(row.sno)
              console.log(response.data.errno)
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
        }
        if (column.label == '更改') {
          this.x = row
        }
      }

    }
  }
</script>
