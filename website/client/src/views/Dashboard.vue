<template>
    <span>
        <h1>Hello, {{ this.account.firstName }}</h1>
    </span>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'dashboard',
  data() {
    return {
      message: '',
    };
  },
  computed: {
    ...mapState([
      'account',
    ]),
  },
  components: {
  },
  methods: {
    ...mapActions([
      'fetchAccessToken',
      'setAccount',
    ]),
    getInfo() {
      this.fetchAccessToken();
      this.$http.get('http://127.0.0.1:5000/getUser', {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      })
        .then((res) => {
          this.setAccount(res.data);
        });
    },
  },
  beforeMount() {
    this.getInfo();
  },
};
</script>
