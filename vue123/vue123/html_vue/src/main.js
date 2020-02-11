// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import './element/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store'
import echarts from 'echarts'

Vue.prototype.$echarts = echarts

Vue.use(VueAxios, axios)
Vue.use(ElementUI)
// 将axios绑定
Vue.prototype.$axios = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
