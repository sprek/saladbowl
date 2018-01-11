import socketio from 'socket.io-client';
import VueSocketio from 'vue-socket.io';
import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.css';
import App from './App';
import router from './router';
import store from './store';

Vue.use(Vuetify);
Vue.use(VueSocketio, socketio(`http://${location.host}`), store);

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App },
});


// render: h => h(App)
