<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-toolbar color="deep-orange darken-4" class="elevation-5" prominent dark>
        <v-toolbar-title class="display-1 mx-4">Login</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field outlined label="Email" prepend-inner-icon="mdi-email" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field outlined label="Password" prepend-inner-icon="mdi-key" type="password" required></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn color="deep-orange darken-1" text @click="closeLogin">Close</v-btn>
        <v-btn color="deep-orange darken-1" text>Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
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
  },
};
</script>
