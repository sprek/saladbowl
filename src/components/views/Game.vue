<template>
<v-container fluid text-xs-center>
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
    </v-flex>
    <v-flex xs12>
      <v-btn block v-if="game_state == this.$sb_helpers.getConst('GS_WAITING_TO_START')" :disabled="!players[username].submitted_words" class="mt-3" color="primary" @click="startClick">Start Game</v-btn>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import WordSubmitForm from '@/components/ui/WordSubmitForm';
import PlayerTeams from '@/components/ui/PlayerTeams';
import { mapState } from 'vuex';
//import sb from '../../SaladbowlUtils';
//import * as sb from '@/SaladbowlUtils';

export default {
  name: 'game-board',
  components: {
    WordSubmitForm,
    PlayerTeams,
  },
  data() {
    return {
      colorSwitch: true,
    };
  },
  watch: {
    game() {
      // if (this.game.players[this.username].submitted_words) {
      // }
    },
  },
  mounted() {
    if (!this.room_id) {
      this.$router.push({ name: 'JoinGame', params: { reqRoomId: this.$route.params.room_id } });
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
  },
};
</script>

<style>
</style>
