<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-toolbar color="deep-orange darken-4" class="elevation-5" prominent dark>
        <v-toolbar-title class="display-1 mx-4">Login</v-toolbar-title>
      </v-toolbar>
      <v-alert
        class="ma-1"
        v-model="alert"
        type="error" 
        dense
      >
        {{ err_msg }}
      </v-alert>
      <v-alert
        class="ma-1"
        v-model="success"
        type="success" 
        dense
      >
        {{ succ_msg }}
      </v-alert>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="email"
                outlined
                label="Email"
                prepend-inner-icon="mdi-email"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="password"
                outlined
                label="Password"
                prepend-inner-icon="mdi-key"
                type="password"
                required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn color="deep-orange darken-1" text @click="closeLogin">Close</v-btn>
        <v-btn color="deep-orange darken-1" text @click="login">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
      err_msg: '',
      succ_msg: '',
      alert: false,
      success: false,
    };
  },
  props: {
    dialog: Boolean,
  },
  components: {
  },
  methods: {
    closeLogin() {
      this.$emit('closeLogin', false);
    },
    login() {
      this.alert = false;
      this.success = false;

      axios.post('http://127.0.0.1:5000/login', {
        email: this.email,
        password: this.password,
      })
        .then((res) => {
          this.succ_msg = "Logged in!"
          this.success = true;
          this.$router.push({ path : '/dashboard' });
          this.$emit('closeLogin', false);
          this.$cookies.set('token',res.data.token);
        })
        .catch((err) => {
          if (err.response)
          {
            this.err_msg = err.response.data.message;
            this.alert = true;
          }
        });
    }
  },
};
</script>
