<template>
  <v-dialog
    v-model="this.accountScreen"
    persistent
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
  >
    <v-card>
      <v-toolbar dark color="deep-orange darken-4">
        <v-btn icon dark @click="this.closeAccount">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-toolbar-title>Account Info</v-toolbar-title>
        <div class="flex-grow-1"></div>
        <v-toolbar-items>
          <v-btn dark text>Save</v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-card class="ma-3">
        <v-card-title>Profile</v-card-title>
        <v-list>
          <v-divider></v-divider>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                First Name
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ this.account.firstName }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
           <v-divider></v-divider>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                Last Name
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ this.account.lastName }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
                     <v-divider></v-divider>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                Email
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ this.account.email }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'Account',
  data() {
    return {
      err_msg: '',
      alert: false,
      profile: [
        {
          attribute: 'First Name',
          value: null,
        },
        {
          attribute: 'Last Name',
          value: null,
        },
        {
          attribute: 'Email',
          value: null,
        },
        {
          attribute: 'Password',
          value: null,
        },
      ],
    };
  },
  computed: {
    ...mapState([
      'accountScreen',
      'account'
    ]),
  },
  components: {
  },
  methods: {
    ...mapActions([
      'setAccessToken',
      'closeAccount',
    ]),
  },
};
</script>
