<template>
<v-container fluid>
  <v-layout row wrap>
    <v-flex xs12>
      <h2>Waiting for:</h2>
    </v-flex>
    <v-flex xs12>
      <v-list>
        <template v-for="cur_player in waitingPlayers">
          <v-chip label :color="players[cur_player].team"><h2>{{cur_player}}</h2></v-chip>
        </template>
      </v-list>
    </v-flex>
    <h2>Ready:</h2>
    <v-flex xs12>
      <v-list>
        <template v-for="cur_player in readyPlayers">
          <v-chip label :color="players[cur_player].team"><h2>{{cur_player}}</h2></v-chip>
        </template>
      </v-list>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

export default {
  name: 'player-teams',
  data() {
    return {
      // items: ["test", "blah", "huh"],
    };
  },
  computed: {
    ...mapState(['username', 'players', 'ordered_players', 'game']),
    ...mapGetters(['waitingPlayers', 'readyPlayers']),
  },
  methods: {
    // ...mapMutations(['set_username']),
    // joinGame() {
    //   if (!this.valid) return;
    //   this.set_username(this.reqUsername);
    //   const params = {
    //     username: this.reqUsername,
    //     room_id: this.reqRoomId,
    //   };
    //   console.log(`JOINING ROOM: ${params.room_id}`);
    //   this.$socket.emit('join', params);
    // },
  },
};
</script>

<style>
</style>
