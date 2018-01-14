import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    connected: false,
    error: '',
    room_id: '',
    num_words_per_player: '',
    players: [],
    player_teams: [],
    username: '',
    word_list: [],
    game: {},
  },
  mutations: {
    SOCKET_CONNECT(state) {
      state.connected = true;
      console.log('CONNECT');
    },
    SOCKET_DISCONNECT(state) {
      state.connected = false;
      console.log('DISCONNECT');
    },
    SOCKET_MESSAGE(state, message) {
      state.game = message;
      state.room_id = message.room_id;
      state.players = message.players;
      state.player_teams = message.player_teams;
      state.word_list = message.word_list;
      state.error = null;

      console.log(`GOT MESSAGE ROOM2: ${message.room_id}`);
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.game = message;
      state.room_id = message.room_id;
      state.players = message.players;
      state.player_teams = message.player_teams;
      state.word_list = message.word_list;
      state.error = null;
      console.log(`GOT JOIN ROOM MSG: ${message.room_id}`);
    },
    SOCKET_ERROR(state, message) {
      console.log(`GOT ERROR: ${message}`);
      state.error = message.error;
    },
    set_room_id(state, room_id) {
      state.room_id = room_id;
    },
    set_username(state, username) {
      state.username = username;
    },
    set_game(state, game) {
      state.game = game;
    },
  },
});
