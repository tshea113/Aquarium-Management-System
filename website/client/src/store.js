import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    account: {
      firstName: null,
      lastName: null,
      email: null,
    },
    accessToken: null,
    loginScreen: false,
    signupScreen: false,
    accountScreen: false,
    loggedIn: false,
  },
  mutations: {
    updateAccount: (state, accountInfo) => {
      state.account.firstName = accountInfo.firstName;
      state.account.lastName = accountInfo.lastName;
      state.account.email = accountInfo.email;
    },
    updateAccessToken: (state, accessToken) => {
      state.accessToken = accessToken;
    },
    toggleLogin: (state, action) => {
      state.loginScreen = action;
    },
    toggleSignup: (state, action) => {
      state.signupScreen = action;
    },
    toggleAccount: (state, action) => {
      state.accountScreen = action;
    }
  },
  actions: {
    setAccount({ commit }, accountInfo) {
      commit('updateAccount', accountInfo);
    },
    deleteAccount({ commit }) {
      commit('updateAccount', {
        firstName: null,
        lastName: null,
        email: null,
      });
    },
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
    openAccount({ commit }) {
      commit('toggleAccount', true);
    },
    closeAccount({ commit }) {
      commit('toggleAccount', false);
    },
  },
});
