<template>
  <div id="app">
    <div id="login" v-if="Flag"><login></login></div>
    <div id="other" v-else>
      <div style="width:100%; height:50px;"><el-button id="logout" :plain="true" @click="logout">登出</el-button></div>
      <index></index>
      </div>
  </div>
</template>
<script>
import index from './components/index.vue'
import login from './components/loginform.vue'
let moment = require('moment')
export default {
  name: 'App',
  data () {
    return {
      Flag: true,
    }
  },
  components: {
    index: index,
    login: login
  },
  computed: {
    listenFlag () {
      return this.$store.state.isLogin
    },
    notices () {
      return this.gridData.length
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('userLogout')
      this.$message({
        showClose: true,
        message: '登出成功',
        type: 'success'
      })
      localStorage.removeItem('User')
      localStorage.removeItem('UserName')
      localStorage.removeItem('userType')
      localStorage.removeItem('userId')
      localStorage.removeItem('User_avatar')
    }
  },
  watch: {
    listenFlag: function (thenew, theold) {
      if (theold === false && thenew === true) {
        this.Flag = false
      } else {
        this.Flag = true
      }
    }
  },
  mounted () {
    this.user = localStorage.getItem('UserName')
    let islogin = this.$store.state.isLogin
    if (islogin === true) {
      let User = localStorage.getItem('UserName')
      this.Flag = false
    } else {
      this.Flag = true
    }
  }
}
</script>

<style>
  body{
    margin: 0;
    min-width: 1200px;
  }
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100%;
}
#login {
  width: 50%;
  margin: auto;
  margin-top: 200px;
}
#other {
  margin-top: 30px;
  width: 100%;
}
#logout {
  float: left;
  margin-left: 230px;
}
</style>
