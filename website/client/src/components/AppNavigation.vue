<template>
    <span>
        <v-navigation-drawer app v-model="drawer" class="deep-orange darken-4" dark disable-resize-watcher>
            <v-list nav>
                <template v-for="(item, index) in items">
                    <v-list-item :key="index" @click.stop="closeWindow(item.title)" link>
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
            <v-app-bar-nav-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-spacer class="hidden-sm-and-down"></v-spacer>
            <v-btn dark @click.stop="loginWindow = true" class="hidden-sm-and-down mx-2">LOGIN</v-btn>
            <v-btn dark @click.stop="signupWindow = true" class="hidden-sm-and-down mx-2">SIGN UP</v-btn>
            <login v-bind:dialog='loginWindow' @closeLogin="closeLogin" />
            <signup v-bind:dialog='signupWindow' @closeSignup="closeSignup" />
        </v-app-bar>
    </span>
</template>

<script>
import Login from './Login';
import Signup from './Signup';

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
          icon: 'mdi-account-key',
        },
        {
          title: 'Sign Up',
          icon: 'mdi-account-plus',
        },
      ],
    };
  },
  components: {
    Login, Signup,
  },
  methods: {
    closeLogin(e) {
      this.loginWindow = e;
    },
    closeSignup(e) {
      this.signupWindow = e;
    },
    closeWindow(whichWindow) {
      if (whichWindow === 'Login') {
        this.loginWindow = true;
      } else if (whichWindow === 'Sign Up') {
        this.signupWindow = true;
      }
    },
  },
};
</script>

<style scoped>
</style>
