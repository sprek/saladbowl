<template>
<v-container v-if="this.room_id" fluid text-xs-center>
  <v-layout row wrap align-center>
    <v-flex xs12>
      <v-card>
        <v-container fluid>
          <v-layout row wrap>
            <v-flex xs4 text-xs-left>
              <h4>User: {{ username }}</h4>
            </v-flex>
            <v-flex xs4 text-xs-middle>
              <v-btn v-if="game_state == this.$sb_helpers.getConst('GS_WAITING_TO_START')" label :color="playerColor" @click.stop="changeTeam"><h4>Team {{playerColor}}</h4></v-btn>
            </v-flex>
            <v-flex xs4 text-xs-right>
              <h4># Players: {{Object.keys(players).length}}</h4>
            </v-flex>
            <v-flex xs4 offset-xs4 text-xs-middle>
              <h5 v-if="game_state == this.$sb_helpers.getConst('GS_WAITING_TO_START')">Click to change</h5>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
      <v-card class="mt-3" v-if="!players[username].submitted_words">
        <v-container fluid>
          <v-layout row wrap text-xs-left>
            <v-flex xs12>
              <h1 class="white--text">Submit Words / Phrases</h1>
              <word-submit-form></word-submit-form>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
      <v-card class="mt-3" v-if="players[username].submitted_words">
        <v-container fluid>
          <v-layout row wrap text-xs-left>
            <v-flex xs12>
              <v-btn block v-if="!showPassAndPlay" @click="passAndPlayClick">Add pass & play player</v-btn>
              <word-submit-form v-if="showPassAndPlay"></word-submit-form>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
      <v-card class="mt-3" v-if="game_state == this.$sb_helpers.getConst('GS_WAITING_TO_START')">
        <v-container fluid>
          <v-layout row wrap text-xs-left>
            <v-flex xs12>
              <h1 class="white--text">Players</h1>
              <player-teams></player-teams>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
      <v-card class="mt-3" v-if="game_state != this.$sb_helpers.getConst('GS_WAITING_TO_START')">
        <v-container fluid>
          <v-layout row wrap text-xs-left>
            <v-flex xs12>
              <h1 class="white--text">Round {{round}}</h1>
              <game-display></game-display>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
    </v-flex>
    <v-flex xs5>
      <v-btn block v-if="game_state == this.$sb_helpers.getConst('GS_WAITING_TO_START')" :disabled="!players[username].submitted_words" class="mt-3" color="primary" @click="startClick">Start Game</v-btn>
    </v-flex>
    <v-flex xs5 offset-xs2>
      <v-btn block v-if="game_state == this.$sb_helpers.getConst('GS_WAITING_TO_START')" class="mt-3" @click="leaveClick">Leave Game</v-btn>
    </v-flex>
    <v-flex xs12>
      <v-btn block v-if="game_state != this.$sb_helpers.getConst('GS_WAITING_TO_START')" class="mt-3" @click="leaveClick">Leave Game</v-btn>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import WordSubmitForm from '@/components/ui/WordSubmitForm';
import PlayerTeams from '@/components/ui/PlayerTeams';
import GameDisplay from '@/components/ui/GameDisplay';
import { mapState, mapMutations } from 'vuex';
//import sb from '../../SaladbowlUtils';
//import * as sb from '@/SaladbowlUtils';

export default {
  name: 'game-board',
  props: ['user'],
  components: {
    WordSubmitForm,
    PlayerTeams,
    GameDisplay,
  },
  data() {
    return {
      colorSwitch: true,
      round: 0,
      showPassAndPlay: false,
    };
  },
  watch: {
    game() {
      console.log ("GOT GAME UPDATE!");
      if (this.game.game_state != this.$sb_helpers.getConst('GS_WAITING_TO_START')) {
        this.round = this.game.round_num;
      }
      // if (this.game.game_state == this.$sb_helpers.getConst('GS_ROUND1')) {
      //   this.round = 1;
      // } else if (this.game.game_state == this.$sb_helpers.getConst('GS_ROUND2')) {
      //   this.round = 2;
      // } else if (this.game.game_state == this.$sb_helpers.getConst('GS_ROUND3')) {
      //   this.round = 3;
      // } else if (this.game.game_state == this.$sb_helpers.getConst('GS_ROUND4')) {
      //   this.round = 4;
      // } else {
      //   this.round = 0;
      // }
    },
  },
  mounted() {
    if (!this.room_id) {
      console.log ("DONT HAVE ROOM ID")
      console.log (`ROOM ID: ${this.$route.params.room_id} USER: ${this.user }`);
      this.set_username(this.user);
      const params = {
        username: this.user,
        room_id: this.$route.params.room_id,
      };
      this.$socket.emit('join', params);
      //this.$router.push({ name: 'JoinGame', params: { reqRoomId: this.$route.params.room_id } });
    }
  },
  computed: {
    ...mapState(['connected', 'room_id', 'error', 'players', 'username', 'game', 'ordered_players', 'game_state']),
    playerColor: function () {
      return this.players[this.username].team
    },
    playerColorLabel: function () {
      return `Team ${this.players[this.username].team}`;
    },
  },
  methods: {
    ...mapMutations(['set_username']),
    changeTeam() {
      const params = {
        username: this.username,
        room_id: this.room_id,
      };
      this.$socket.emit('change_team', params);
    },
    startClick() {
      const params = {
        room_id: this.room_id,
      };
      this.$socket.emit('start', params);
    },
    leaveClick() {
      const params = {
        room_id: this.room_id,
        username: this.username,
      };
      this.$socket.emit('leave', params);
      this.$router.push({ name: 'Home'});
    },
    passAndPlayClick() {
      this.showPassAndPlay = true;
      // this.$socket.emit('pass_and_play_add');
    }
  },
};
</script>

<style>
</style>
