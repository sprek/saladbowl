import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    connected: false,
    room_id: '',
    error: '',
    num_words_per_player: '',
    players: [],
    cur_player: '',
    word_list: [],
    game: {},
  },
  getters: {
  },
  mutations: {
    SOCKET_CONNECT(state) {
      state.connected = true;
      console.log("CONNECT");
    },
    SOCKET_DISCONNECT(state) {
      state.connected = false;
      console.log("DISCONNECT");
    },
    SOCKET_MESSAGE(state, message) {
      // state.num_people = message.num_people;
      state.room_id = message.room_id;
      state.error = null;
      console.log("GOT MESSAGE ROOM: " + state.room_id);
      //console.log("GOT MESSAGE ERROR: " + state.error);
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.error = null;
      state.room_id = message.room_id;
      console.log("GOT JOIN ROOM: " + message.room_id);
    },
    SOCKET_ERROR(state, message) {
      console.log("GOT ERROR: " + message.error);
      state.error = message.error;
    },
    set_room_id(state, room_id) {
      state.room_id = room_id;
    },
  },
});
