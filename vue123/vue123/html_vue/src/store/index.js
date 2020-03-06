import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 设置属性
  state: {
    isAdmin: false,
    isLogin: false,
    aim_user: '',
    user: {}
  },

  // 获取属性的状态
  getters: {
    // 获取登录状态
    isLogin: state => state.isLogin,
	isAdmin: state => state.isAdmin
  },

  // 设置属性状态
  mutations: {
    // 保存登录状态
    userStatus (state, flag) {
      state.isLogin = flag
    },
	userAs (state, flag) {
	  state.isAdmin = flag
	},
    logout (state) {
      localStorage.setItem('Flag', 'not')
      state.isLogin = false
    },
    aim (state, flag) {
      state.aim_user = flag
    }
  },

  // 应用mutations
  actions: {
    // 获取登录状态
    userLogin ({commit}, flag) {
      commit('userStatus', flag)
    },
	userAdmin ({commit}, flag) {
	  commit('userAs', flag)
	},
    userLogout ({commit}) {
      commit('logout')
    },
    setaimuser ({commit}, flag) {
      commit('aim', flag)
    }
  }
})

export default store
