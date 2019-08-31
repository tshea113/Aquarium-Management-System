<template>
    <span>
        <v-navigation-drawer
          app v-model="drawer"
          class="deep-orange darken-4"
          dark
          disable-resize-watcher
        >
            <v-list nav>
                <template v-for="(item, index) in items">
                    <v-list-item
                      v-if="isLoggedIn(item.accountOnly)"
                      :key="index"
                      @click.stop="navbarClick(item.title)"
                      link
                    >
                        <v-list-item-icon>
                            <v-icon v-text="item.icon"></v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title v-text="item.title"></v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </template>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar app dense color="gray darken-4" class="elevation-5" dark>
            <v-app-bar-nav-icon
              class="hidden-md-and-up"
              @click="drawer=!drawer"
            ></v-app-bar-nav-icon>
            <v-spacer class="hidden-sm-and-down"></v-spacer>
            <v-btn
              v-if="isLoggedIn(false)"
              dark
              @click.stop="navbarClick('Login')"
              class="hidden-sm-and-down mx-2"
            >
              LOGIN
            </v-btn>
            <v-btn
              v-if="isLoggedIn(false)"
              dark
              @click.stop="navbarClick('Sign Up')"
              class="hidden-sm-and-down mx-2"
            >
              SIGN UP
            </v-btn>
            <v-btn
              v-if="isLoggedIn(true)"
              dark
              @click.stop="navbarClick('Account Info')"
              class="hidden-sm-and-down mx-2"
            >
              ACCOUNT
            </v-btn>
                        <v-btn
              v-if="isLoggedIn(true)"
              dark
              @click.stop="navbarClick('Logout')"
              class="hidden-sm-and-down mx-2"
            >
              LOGOUT
            </v-btn>
            <login/>
            <signup/>
        </v-app-bar>
    </span>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Login from './Login.vue';
import Signup from './Signup.vue';

export default {
  name: 'AppNavigation',
  data() {
    return {
      drawer: false,
      loginWindow: false,
      signupWindow: false,
      items: [
        {
          title: 'Login',
          icon: 'mdi-login',
          accountOnly: false,
        },
        {
          title: 'Sign Up',
          icon: 'mdi-account-plus',
          accountOnly: false,
        },
        {
          title: 'Logout',
          icon: 'mdi-logout',
          accountOnly: true,
        },
      ],
    };
  },
  computed: {
    ...mapState([
      'loginScreen',
      'signupScreen',
      'loggedIn',
    ]),
  },
  components: {
    Login, Signup,
  },
  methods: {
    ...mapActions([
      'openLogin',
      'openSignup',
      'logout',
    ]),
    navbarClick(title) {
      if (title === 'Login') {
        this.openLogin();
      } else if (title === 'Sign Up') {
        this.openSignup();
      } else if (title === 'Logout') {
        this.logout();
        this.$router.push({ path: '/' });
      }
    },
    isLoggedIn(accountOnly) {
      return (this.loggedIn && accountOnly) || (!this.loggedIn && !accountOnly);
    },
  },
};
</script>

<style scoped>
</style>
