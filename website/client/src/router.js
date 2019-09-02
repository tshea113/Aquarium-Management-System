import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Dashboard from './views/Dashboard.vue';
import store from './store';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      meta: { requiresAuth: true },
      component: Dashboard,
    },
    {
      path: '*',
      redirect: '/',
    },
  ],
});

router.beforeEach((to, from, next) => {
  store.dispatch('fetchAccessToken')
    .then((res) => {
      if (to.matched.some(record => record.meta.requiresAuth)) {
        // For routes that require auth
        if (store.state.loggedIn) {
          if (to.path === '/') {
            next('/dashboard');
          } else {
            next();
          }
        } else {
          next('/');
        }
      } else {
        next();
      }
    })
    .catch((err) => {
      console.log(err);
      next('/');
    });
});

export default router;
