import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: null,
    loginScreen: false,
    signupScreen: false,
    loggedIn: false,
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
    },
  },
  actions: {
    setAccessToken({ commit }, token) {
      localStorage.setItem('token', token);
      this.state.loggedIn = true;
      commit('updateAccessToken', token);
    },
    fetchAccessToken({ commit }) {
      if (localStorage.getItem('token')) {
        this.state.loggedIn = true;
      } else {
        this.state.loggedIn = false;
      }
      commit('updateAccessToken', localStorage.getItem('token'));
    },
    logout({ commit }) {
      localStorage.clear();
      this.state.loggedIn = false;
      commit('updateAccessToken', null);
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
  },
});
