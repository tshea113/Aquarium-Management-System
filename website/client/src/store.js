import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    loginScreen: false,
    signupScreen: false,
  },
  mutations: {
    updateAccessToken: (state, accessToken) => {
      state.accessToken = accessToken;
    },
    toggleLogin: (state, action) => {
      state.loginScreen = action;
    },
    toggleSignup: (state, action) => {
      state.signupScreen = action;
    }
  },
  actions: {
    setAccessToken({ commit }, token) {
      localStorage.setItem('token', token);
      commit('updateAccessToken', token);
    },
    fetchAccessToken({ commit }) {
      commit('updateAccessToken', localStorage.getItem('token'));
    },
    openLogin({ commit }) {
      commit('toggleLogin', true);
    },
    closeLogin({ commit }) {
      commit('toggleLogin', false);
    },
    openSignup({ commit }) {
      commit('toggleSignup', true);
    },
    closeSignup({ commit }) {
      commit('toggleSignup', false);
    },
  }
});
