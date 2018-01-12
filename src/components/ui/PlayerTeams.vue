<template>
<v-container fluid>
  <v-layout row wrap>
    <v-flex xs12>
      <!-- <v-list v-for="player in players">
           {{ player }}
           </v-list> -->
      <v-list>
        <template v-for="n in players.length">
          <!-- <v-list-tile>
          <v-list-tile-content>
            <v-list-tile-title>{{n}}. {{players[n-1]}}</v-list-tile-title>
          </v-list-tile-content>
          </v-list-tile> -->
          <v-chip label :color="player_teams[n-1]"><h2>{{n}}. {{players[n-1]}}</h2></v-chip>
        </template>
      </v-list>
    </v-flex>
    <v-flex xs12>
      <v-btn block class="mt-3" @click.stop="ready">Ready</v-btn>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'player-teams',
  data() {
    return {
      // items: ["test", "blah", "huh"],
    };
  },
  computed: {
    ...mapState(['username', 'players', 'player_teams']),
  },
  watch: {
    // room_id() {
    //   console.log(`SETTING ROOM ID: ${this.room_id}`);
    //   // this.set_room_id(this.room_id);
    //   this.$router.push({ name: 'Game', params: { room_id: this.room_id } });
    // },
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
