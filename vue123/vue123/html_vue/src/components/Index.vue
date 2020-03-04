<template>
<div class="bigbox">
  <el-row class="tac">
   <el-col>
     <el-menu
       default-active="2"
       class="el-menu-vertical-demo"
       @select="handleSelect">
       <el-menu-item-group>
         <div slot="title" style="font-size:18px;">学生操作</div>
         <el-menu-item index="1">
           <i class="el-icon-menu"></i>
           <span slot="title">学生选课</span>
         </el-menu-item>
         <el-menu-item index="2">
           <i class="el-icon-menu"></i>
           <span slot="title">成绩查询</span>
         </el-menu-item>
       </el-menu-item-group>
       <el-menu-item-group>
         <div slot="title" style="font-size:18px;">老师操作</div>
         <el-menu-item index="3">
           <i class="el-icon-document"></i>
           <span slot="title">成绩管理</span>
         </el-menu-item>
         <el-menu-item index="4">
           <i class="el-icon-setting"></i>
           <span slot="title">课程管理</span>
         </el-menu-item>
         <el-menu-item index="5">
           <i class="el-icon-setting"></i>
           <span slot="title">学生管理</span>
         </el-menu-item>
       </el-menu-item-group>
     </el-menu>
   </el-col>
 </el-row>
  <div class="content">
    <div v-if="Flag === '1'">
      <oooooo></oooooo>
    </div>
    <div v-if="Flag === '2'">
       <eeeeee></eeeeee>
    </div>
    <div v-if="Flag === '3'">
      <grade></grade>
    </div>
    <div v-if="Flag === '4'">
      <adcourse></adcourse>
    </div>
    <div v-if="Flag === '5'">
      <adstu></adstu>
    </div>
  </div>
</div>
</template>

<script>
  import oooooo from './oooooo.vue'
  import eeeeee from './eeeeee.vue'
  import adstu from "./adstu.vue";
  import adcourse from "./adcourse";
  import grade from './grade.vue';

  export default {
    name: 'Index',
    components: {
      eeeeee: eeeeee,
      oooooo: oooooo,
      adstu: adstu,
      adcourse: adcourse,
      grade: grade,

    },
    methods: {
      handleSelect(key, keyPath) {
      this.Flag = key
    },
    chooseModule (moduleName) {
      this.$axios.post('/api/task/findTaskByTags',
        {
          tags: moduleName
        }).then((response) => {
        if (response.data.Status === 'right') {
          this.taskList = response.data.task_omitinfo
        } else {
          alert(response.data.Details)
        }
      })
        .catch((error) => {
          console.log(error)
        })
    },
    gotoDetails (id) {
      let type = 'published'
      this.$axios.post('/addHistory', {
        'task_id': id,
        'user_name': localStorage.getItem('UserName')
      }).then((response) => {
        console.log(response.data)
      })
        .catch((error) => {
          console.log(error)
        })
      this.$router.push({
        path: `/taskdetails/${type}/${id}`
      })
    },
    Init () {
      this.$axios.post('/api/task/latest').then((response) => {
        this.taskList = response.data.latest
      })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  data () {
    return {
      Flag: '0'
    }
  }
}
</script>

<style scoped>
  .bigbox {
    width: 100%;
    padding: 50px;
  }
  .tac {
    float: left;
    width: 300px;
  }
  .tac span {
    font-size:20px;
  }
  .content {
    float: left;
    width: 800px;
  }
</style>
