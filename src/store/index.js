import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    connected: false,
    error: '',
    room_id: '',
    num_words_per_player: '',
    players: {},
    ordered_players: [],
    username: '',
    word_list: [],
    game_state: '',
    game: {},
    round_num: 0,
  },
  getters: {
    readyPlayers: state => {
      var readyPlayers = [];
      state.ordered_players.forEach(function(user, index) {
        if (state.players[user].submitted_words) {
          readyPlayers.push(user);
          //console.log (`SUBMITTED: ${this.game.players[user].submitted_words}`);
        }
      });
      return readyPlayers;
    },
    waitingPlayers: state => {
      var waitingPlayers = [];
      state.ordered_players.forEach(function(user, index) {
        if (!state.players[user].submitted_words) {
          waitingPlayers.push(user);
          //console.log (`SUBMITTED: ${this.game.players[user].submitted_words}`);
        }
      });
      return waitingPlayers;
    }
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
      state.ordered_players = message.ordered_players;
      state.game_state = message.game_state;
      // state.player_teams = message.player_teams;
      // state.player_statuses = message.player_statuses;
      state.word_list = message.word_list;
      state.error = null;
      state.round_num = message.round_num;
      console.log(`GOT MESSAGE ROOM2: ${message.room_id}`);
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.game = message;
      state.room_id = message.room_id;
      state.players = message.players;
      state.ordered_players = message.ordered_players;
      state.game_state = message.game_state;
      state.round_num = message.round_num;
      // state.player_teams = message.player_teams;
      // state.player_statuses = message.player_statuses;
      state.word_list = message.word_list;
      state.error = null;
      //console.log (`GOT TEST: ${message.test['user1']['team']}`);
      //console.log (`GOT TEST: ${message.players['asdf']['team']}`);
      console.log (`GOT ORDERED PLAYERS: ${message.ordered_players}`);
      console.log(`GOT JOIN ROOM MSG: ${message.room_id}`);
    },
    //SOCKET_JOIN_ROOM_CAST(state, message) {
    //  state.game = message;
    //  state.room_id = message.room_id;
    //  state.players = message.players;
    //  state.ordered_players = message.ordered_players;
    //  state.game_state = message.game_state;
    //  state.word_list = message.word_list;
    //  state.error = null;
    //  console.log(`GOT JOIN ROOM CAST MSG: ${message.room_id}`);
    //},
    SOCKET_GAME_UPDATE_CAST(state, message) {
      state.game = message;
      state.room_id = message.room_id;
      state.players = message.players;
      state.ordered_players = message.ordered_players;
      state.game_state = message.game_state;
      state.word_list = message.word_list;
      state.round_num = message.round_num;
      state.error = null;
      console.log(`GOT GAME UPDATE CAST MSG: ${message.room_id}`);
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
