<template>
    <span>
        <h1>{{ message }}</h1>
    </span>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'dashboard',
  data() {
    return {
      message: '',
    };
  },
  components: {
  },
  methods: {
    ...mapActions([
      'fetchAccessToken',
    ]),
    getInfo() {
      this.fetchAccessToken();
      this.$http.get('http://127.0.0.1:5000/getDashboard', {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      })
        .then((res) => {
          this.message = res.data.message;
        })
        .catch((err) => {
          this.message = err.response.data;
        });
    },
  },
  beforeMount() {
    this.getInfo();
  },
};
</script>
