<template>
<v-card>
  <v-card-text>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12>
          <v-text-field v-model="reqUsername" label="User Name"></v-text-field>
          <v-select v-bind:items="numWordsOptions" v-model="numWordsPerPlayer"
                    label="Number of words per player"></v-select>
        </v-flex>
        <v-flex xs12>
          <v-btn block class="mt-3" @click.stop="createGame">Start Game</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card-text>
</v-card>
</template>

<script>
import { mapState, mapMutations} from 'vuex';
export default {
  name: 'create-form',
  data() {
    return {
      reqUsername: '',
      numWordsPerPlayer: 3,
      numWordsOptions: [1,2,3,4,5],
    };
  },
  computed: {
    ...mapState(['room_id', 'username', 'game']),
  },
  watch: {
    game() {
      console.log ("SETTING ROOM ID: " + this.room_id + " USER: " + this.username + " GAME: " + this.game.room_id + " GAME2: " + this.game.username);
      //this.set_room_id(this.room_id);
      this.$router.push({name: 'Game', params: {room_id: this.room_id } });
    },
  },
  methods: {
    createGame() {
      const params = {
        username: this.reqUsername,
        numWordsPerPlayer: this.numWordsPerPlayer,
      };
      this.$socket.emit('create', params);
    }
  }
}
</script>
<style>
</style>
