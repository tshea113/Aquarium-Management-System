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
  },
};
</script>
